#!/usr/bin/env python3
"""Build the Trio shortcut for one locale.

Usage:  python3 src/build_trio.py <lang>
Output: dist/<lang>/Trio.shortcut  (unsigned; tools/build.sh signs it)

Trio is the Critique pair plus a third voice from a third company:
  1. ChatGPT answers (Ask ChatGPT, the person's own app);
  2. Claude checks and writes the final answer (Ask Claude, prompt critique.txt) — exactly as in Poly;
  3. a third model, reached with «Get Contents of URL» on a FREE key, names only the errors and gaps
     that BOTH missed (prompt trio.txt). Its words come back as a separate block, never merged.

The third voice speaks the OpenAI chat-completions dialect, so one request template serves both
providers: Google AI Studio (Gemini Flash, the default) and Groq (Qwen). Keys are told apart by their
shape: a Groq key starts with «gsk_», any other long token is Google's. With both keys saved, Qwen on
Groq stands in when Gemini is out for the day (quota) or still overloaded after one retry, and the
block header says so.

The keys are NOT in the shortcut. They are read from iCloud Drive → Shortcuts → poly-key.txt; on the
first run the shortcut asks for them (Gemini, then Groq — optional) and saves them there. A shared
shortcut therefore never carries a key.

Locales without locales/<lang>/trio.json are skipped: Trio ships where its words exist.
"""
import json
import os
import plistlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_shortcut import (  # noqa: E402
    ROOT, Locale, new_uuid, text_token, attachment, variable, validate,
    act_ask, act_gpt, act_claude, act_text, act_set_variable, act_get_variable,
    act_comment, act_clipboard, act_quick_look, act_get_file, act_save_file,
    if_has_value, if_else, if_close,
)

GEMINI_URL = 'https://generativelanguage.googleapis.com/v1beta/openai/chat/completions'
GEMINI_MODEL = 'gemini-3.8-flash'      # checked against /v1beta/openai/models on 2026-10-01
GROQ_URL = 'https://api.groq.com/openai/v1/chat/completions'
GROQ_MODEL = 'qwen/qwen3.8-27b'        # checked against /openai/v1/models on 2026-10-01
# Keys are picked out of poly-key.txt by their shape, so the person may paste one key or both, in any
# order, with any spaces or line breaks around them. Groq keys start with gsk_; a Google AI Studio key
# is any other long token (AIza… in the old format, AQ.… in the new one).
GROQ_KEY_RE = r'gsk_[A-Za-z0-9]+'
GOOGLE_KEY_RE = r'(?<![A-Za-z0-9_.-])(?!gsk_)[A-Za-z0-9][A-Za-z0-9._-]{19,}'
# Gemini answered «no» for reasons that pass by tomorrow or in a minute: the free quota or overload.
GEMINI_DOWN_RE = r'quota|UNAVAILABLE|RESOURCE_EXHAUSTED'
# Groq's free tier allows 1000 OUTPUT tokens a minute; a request that may exceed it is refused
# outright, so the answer is capped below that. 900 is ample for «only what both missed».
MAX_TOKENS = '900'


# ---------------------------------------------------------------- actions this shortcut adds

def act_notify(title, body):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.notification',
            'WFWorkflowActionParameters': {'WFNotificationActionTitle': title,
                                           'WFNotificationActionBody': body,
                                           'WFNotificationActionSound': False}}


def act_match(pattern, src_uid, src_name, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.text.match',
            'WFWorkflowActionParameters': {'WFMatchTextPattern': pattern,
                                           'WFMatchTextCaseSensitive': True,
                                           'text': text_token('{T}', {'T': (src_uid, src_name)}),
                                           'UUID': uid}}


def if_contains(group, var_name, needle):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.conditional',
            'WFWorkflowActionParameters': {'GroupingIdentifier': group, 'WFControlFlowMode': 0,
                                           'WFCondition': 99,  # «contains»
                                           'WFConditionalActionString': needle,
                                           'WFInput': {'Type': 'Variable',
                                                       'Variable': variable(var_name)}}}


def plain(text):
    return {'Value': {'string': text, 'attachmentsByRange': {}},
            'WFSerializationType': 'WFTextTokenString'}


def item_text(key, value):
    return {'WFItemType': 0, 'WFKey': plain(key), 'WFValue': value}


def item_number(key, number):
    return {'WFItemType': 3, 'WFKey': plain(key), 'WFValue': plain(number)}


def nested_dict(items):
    # a dictionary inside a dictionary or a list is wrapped twice — that is how Shortcuts writes it
    return {'Value': {'Value': {'WFDictionaryFieldValueItems': items},
                      'WFSerializationType': 'WFDictionaryFieldValue'},
            'WFSerializationType': 'WFDictionaryFieldValue'}


def top_dict(items):
    return {'Value': {'WFDictionaryFieldValueItems': items},
            'WFSerializationType': 'WFDictionaryFieldValue'}


def act_post_json(url_uid, key_uid, model_uid, prompt_uid, uid):
    """POST {model, messages:[{role:user, content:prompt}], max_tokens} with a Bearer key."""
    body = top_dict([
        item_text('model', text_token('{M}', {'M': (model_uid, 'Variable')})),
        {'WFItemType': 2, 'WFKey': plain('messages'),
         'WFValue': {'Value': [{'WFItemType': 1, 'WFValue': nested_dict([
             item_text('role', plain('user')),
             item_text('content', text_token('{P}', {'P': (prompt_uid, 'Text')})),
         ])}], 'WFSerializationType': 'WFArrayParameterState'}},
        item_number('max_tokens', MAX_TOKENS),
    ])
    headers = top_dict([
        item_text('Authorization', text_token('Bearer {K}', {'K': (key_uid, 'Variable')})),
        item_text('Content-Type', plain('application/json')),
    ])
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.downloadurl',
            'WFWorkflowActionParameters': {'WFURL': text_token('{U}', {'U': (url_uid, 'Variable')}),
                                           'WFHTTPMethod': 'POST',
                                           'ShowHeaders': True,
                                           'WFHTTPHeaders': headers,
                                           'WFHTTPBodyType': 'JSON',
                                           'WFJSONValues': body,
                                           'UUID': uid}}


def act_value(key, src_uid, src_name, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.getvalueforkey',
            'WFWorkflowActionParameters': {'WFGetDictionaryValueType': 'Value',
                                           'WFDictionaryKey': key,
                                           'WFInput': attachment(src_uid, src_name),
                                           'UUID': uid}}


def act_first_item(src_uid, src_name, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.getitemfromlist',
            'WFWorkflowActionParameters': {'WFItemSpecifier': 'First Item',
                                           'WFInput': attachment(src_uid, src_name),
                                           'UUID': uid}}


def set_text(var_name, template, uid, refs=None):
    return [act_text(text_token(template, refs or {}), uid),
            act_set_variable(var_name, uid, 'Text')]


def act_wait(seconds):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.delay',
            'WFWorkflowActionParameters': {'WFDelayTime': seconds}}


def third_voice(T, V, prompt_uid):
    """From the finished trio prompt to the variable V['third'] holding the third voice's words.

    Expects V['url'], V['model'], V['key'] to be set. Shared with the Mac probe, so what is tested
    on a Mac is exactly what ships.
    """
    ids = lambda n: [new_uuid() for _ in range(n)]
    url, model, key, post, raw = ids(5)
    url2, model2, key2, post2, raw2 = ids(5)
    data, choices, first, message, content, raw_var = ids(6)
    g_busy, g_ok, g_down, g_groq = ids(4)
    url3, model3, key3, post3, raw3, raw_check, down, groq_key = ids(8)

    def request(u_url, u_model, u_key, u_post, u_raw):
        return [act_get_variable(V['url'], u_url),
                act_get_variable(V['model'], u_model),
                act_get_variable(V['key'], u_key),
                act_post_json(u_url, u_key, u_model, prompt_uid, u_post),
                act_set_variable(V['data'], u_post, 'Contents of URL'),
                act_text(text_token('{R}', {'R': (u_post, 'Contents of URL')}), u_raw),
                act_set_variable(V['raw'], u_raw, 'Text')]

    # error branch: the reply did not carry «choices». Gemini wraps errors in a list, Groq in a dict,
    # and «Get Contents of URL» hands back no status code — so the reply's own words decide.
    errors = [  # (needle, message) — first match wins
        ('quota', T['error.limit']),            # Gemini 429: per-minute or daily free quota
        ('rate_limit', T['error.limit']),       # Groq 429 / request too large for the free tier
        ('API key', T['error.key']),            # Gemini 400 «Please pass a valid API key»
        ('API Key', T['error.key']),            # Groq 401 «Invalid API Key»
        ('API_KEY', T['error.key']),            # Gemini «API_KEY_INVALID»
        ('UNAVAILABLE', T['error.busy']),       # Gemini 503 «high demand»
        ('over capacity', T['error.busy']),     # Groq 503
        ('NOT_FOUND', T['error.model']),        # model renamed or withdrawn
        ('model_not_found', T['error.model']),
    ]
    error_actions, groups = [], []
    for needle, text in errors:
        group = new_uuid()
        groups.append(group)
        error_actions += [if_contains(group, V['raw'], needle),
                          *set_text(V['third'], text, new_uuid()),
                          if_else(group)]
    error_actions += [act_get_variable(V['raw'], raw_var),
                      *set_text(V['third'], T['error.other'] + '\n{R}', new_uuid(),
                                {'R': (raw_var, 'Variable')})]
    error_actions += [if_close(group) for group in reversed(groups)]

    return [
        *request(url, model, key, post, raw),
        # Gemini's free Flash answers «high demand» (503) often enough in autumn 2026 that one quiet
        # retry after a pause turns most of those into an answer.
        if_contains(g_busy, V['raw'], 'UNAVAILABLE'),
        act_notify(T['name'], T['notify.retry']),
        act_wait(10),
        *request(url2, model2, key2, post2, raw2),
        if_close(g_busy),
        act_get_variable(V['raw'], raw_check),
        # Gemini is out for today (quota) or still overloaded, and the person also saved a Groq key:
        # the third voice moves to Qwen on Groq instead of falling silent, and says so in its header.
        act_match(GEMINI_DOWN_RE, raw_check, 'Variable', down),
        act_set_variable(V['gemini_down'], down, 'Matches'),
        if_has_value(g_down, V['gemini_down']),
        if_has_value(g_groq, V['groq_key']),
        act_notify(T['name'], T['notify.fallback']),
        act_get_variable(V['groq_key'], groq_key),
        *set_text(V['key'], '{K}', new_uuid(), {'K': (groq_key, 'Variable')}),
        *set_text(V['url'], GROQ_URL, new_uuid()),
        *set_text(V['model'], GROQ_MODEL, new_uuid()),
        *set_text(V['provider'], T['provider.groq_fallback'], new_uuid()),
        *request(url3, model3, key3, post3, raw3),
        if_close(g_groq),
        if_close(g_down),
        if_contains(g_ok, V['raw'], 'choices'),
        act_get_variable(V['data'], data),
        act_value('choices', data, 'Variable', choices),
        act_first_item(choices, 'Dictionary Value', first),
        act_value('message', first, 'Item from List', message),
        act_value('content', message, 'Dictionary Value', content),
        act_set_variable(V['third'], content, 'Dictionary Value'),
        if_else(g_ok),
        *error_actions,
        if_close(g_ok),
    ]


# ---------------------------------------------------------------- build

def build(lang):
    trio_file = ROOT / 'locales' / lang / 'trio.json'
    if not trio_file.exists():
        print(f'{lang}: no trio.json — Trio not built for this language')
        return
    L = Locale(lang)
    T = json.loads(trio_file.read_text(encoding='utf-8'))
    NAME = T['name']
    V = T['variables']

    ids = lambda n: [new_uuid() for _ in range(n)]
    k_get, k_file, k_ask, k_ask2, k_both, k_save, k_var = ids(7)
    k_groq_m, k_groq_1, k_groq, k_gem_m, k_gem_1, k_gem = ids(6)
    p_g_key, p_g_key2, p_q_key, p_q_key2 = ids(4)
    p_g_url, p_g_model, p_g_name, p_q_url, p_q_model, p_q_name = ids(6)
    question, wrap, gpt, critique, claude = ids(5)
    t_prompt, = ids(1)
    f_third, f_provider, f_claude, f_out = ids(4)
    g_key, g_provider = ids(2)
    Q = {'Q': (question, 'Provided Input')}

    actions = [
        act_comment(T['comment']),

        # ---- the keys: from iCloud Drive → Shortcuts → poly-key.txt, or asked once and saved there.
        # The first run offers both free keys: Gemini (the third voice) and, if the person wants,
        # Groq (the stand-in when Gemini is out for the day or overloaded).
        act_get_file(T['files.key'], k_get),
        act_set_variable(V['key_file'], k_get, 'File'),
        if_has_value(g_key, V['key_file']),
        *set_text(V['keys'], '{F}', k_file, {'F': (k_get, 'File')}),
        if_else(g_key),
        act_ask(T['ask.key'], k_ask),
        act_ask(T['ask.key2'], k_ask2, default='-'),
        act_text(text_token('{A}\n{B}\n', {'A': (k_ask, 'Provided Input'),
                                            'B': (k_ask2, 'Provided Input')}), k_both),
        act_save_file(T['files.key'], k_both, k_save),
        act_set_variable(V['keys'], k_both, 'Text'),
        if_close(g_key),
        act_get_variable(V['keys'], k_var),
        act_match(GROQ_KEY_RE, k_var, 'Variable', k_groq_m),
        act_first_item(k_groq_m, 'Matches', k_groq_1),
        *set_text(V['groq_key'], '{K}', k_groq, {'K': (k_groq_1, 'Item from List')}),
        act_match(GOOGLE_KEY_RE, k_var, 'Variable', k_gem_m),
        act_first_item(k_gem_m, 'Matches', k_gem_1),
        *set_text(V['gemini_key'], '{K}', k_gem, {'K': (k_gem_1, 'Item from List')}),

        # ---- Gemini speaks third when its key is there; with only a Groq key, Qwen does
        if_has_value(g_provider, V['gemini_key']),
        act_get_variable(V['gemini_key'], p_g_key),
        *set_text(V['key'], '{K}', p_g_key2, {'K': (p_g_key, 'Variable')}),
        *set_text(V['url'], GEMINI_URL, p_g_url),
        *set_text(V['model'], GEMINI_MODEL, p_g_model),
        *set_text(V['provider'], T['provider.gemini'], p_g_name),
        if_else(g_provider),
        act_get_variable(V['groq_key'], p_q_key),
        *set_text(V['key'], '{K}', p_q_key2, {'K': (p_q_key, 'Variable')}),
        *set_text(V['url'], GROQ_URL, p_q_url),
        *set_text(V['model'], GROQ_MODEL, p_q_model),
        *set_text(V['provider'], T['provider.groq'], p_q_name),
        if_close(g_provider),

        # ---- the pair, exactly as Critique in Poly: ChatGPT answers, Claude checks
        act_ask(T['ask.question'], question, prefill_from_share=True),
        act_notify(NAME, T['notify.start']),
        act_text(text_token(L.prompt('wrap'), Q), wrap),
        act_gpt(text_token('{P}', {'P': (wrap, 'Text')}), gpt),
        act_text(text_token(L.prompt('critique'),
                            {'QUESTION': (question, 'Provided Input'),
                             'GPT_ANSWER': (gpt, 'Ask ChatGPT')}), critique),
        act_notify(NAME, T['notify.step2']),
        act_claude(text_token('{P}', {'P': (critique, 'Text')}), claude),
        # Claude's answer reaches the clipboard before the network call: if the third voice fails
        # in any way, the person still holds the checked answer.
        act_clipboard(attachment(claude, 'Ask Claude')),

        # ---- the third voice
        act_notify(NAME, T['notify.step3']),
        act_text(text_token(L.prompt('trio'),
                            {'QUESTION': (question, 'Provided Input'),
                             'GPT_ANSWER': (gpt, 'Ask ChatGPT'),
                             'CLAUDE_ANSWER': (claude, 'Ask Claude')}), t_prompt),
        *third_voice(T, V, t_prompt),

        # ---- one document: Claude's checked answer, then the third voice as its own block
        act_get_variable(V['third'], f_third),
        act_get_variable(V['provider'], f_provider),
        act_text(text_token(T['output'], {'C': (claude, 'Ask Claude'),
                                          'P': (f_provider, 'Variable'),
                                          'T': (f_third, 'Variable')}), f_out),
        act_clipboard(attachment(f_out, 'Text')),
        act_notify(NAME, T['notify.done']),
        act_quick_look(attachment(f_out, 'Text')),
    ]

    validate(actions)
    workflow = plistlib.loads((ROOT / 'src' / 'metadata.plist').read_bytes())
    workflow['WFWorkflowIcon'] = {'WFWorkflowIconStartColor': 2071128575,
                                  'WFWorkflowIconGlyphNumber': 61440}
    workflow['WFWorkflowTypes'] = ['ActionExtension']
    workflow['WFWorkflowInputContentItemClasses'] = ['WFStringContentItem', 'WFURLContentItem',
                                                     'WFRichTextContentItem', 'WFArticleContentItem']
    workflow['WFWorkflowHasShortcutInputVariables'] = True
    workflow['WFQuickActionSurfaces'] = ['ShareSheet']
    workflow['WFWorkflowActions'] = actions

    out_dir = Path(os.environ.get('C1_DIST', ROOT / 'dist')) / lang
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f'{NAME}.shortcut'
    with out.open('wb') as f:
        plistlib.dump(workflow, f, fmt=plistlib.FMT_BINARY)
    print(f'{lang}: {out.name} — {len(actions)} actions')


if __name__ == '__main__':
    languages = sys.argv[1:] or [d.name for d in sorted((ROOT / 'locales').iterdir()) if d.is_dir()]
    for language in languages:
        build(language)
