#!/usr/bin/env python3
"""Build the Trio shortcut for one locale.

Usage:  python3 src/build_trio.py <lang>
Output: dist/<lang>/Trio.shortcut  (unsigned; tools/build.sh signs it)

Trio is the Critique pair plus a third voice from a third company:
  1. ChatGPT answers (Ask ChatGPT, the person's own app);
  2. Claude checks and writes the final answer (Ask Claude, prompt critique.txt) — exactly as in Poly;
  3. a third model, reached with «Get Contents of URL» on a FREE key, names only the errors and gaps
     that BOTH missed (prompt trio.txt). Its words come back as a separate block, never merged.

The third voice speaks the OpenAI chat-completions dialect, so one request template serves every
free provider: NVIDIA build (Kimi K3, GLM-5.3, DeepSeek V4.1), Google AI Studio (Gemini Flash),
OpenRouter (its `:free` models) and Groq. The person may save any number of free keys; each is
recognised by how it begins (nvapi- → NVIDIA, AIza/AQ. → Google, sk-or- → OpenRouter, gsk_ → Groq). Trio walks every model of every key until one answers: a busy model (503)
or a spent daily limit (429) moves to the next model, a key with no money (402) or an invalid key (401)
is not asked again. Only when all of them failed does the block say what each one answered and what
to do — never «invalid key» for a key that merely ran out of money or was busy.

The keys are NOT in the shortcut. They are read from iCloud Drive → Shortcuts → poly-key.txt (one per
line); on the first run the shortcut asks for them and saves them there. A shared shortcut therefore
never carries a key.

PAID keys (owner, 2026-10-01: «a well-off person may paste their own paid API keys»). Free keys stay the
first thing a newcomer is asked for; a paid key is optional and recognised the same way, by how it begins:
sk-ant- → Anthropic, xai- → xAI, sk-<32 hex> → DeepSeek, any other sk- (sk-proj-, sk-svcacct-…) → OpenAI.
The person pays their provider directly; nothing passes through us. The third voice must come from a THIRD
company — ChatGPT (OpenAI) and Claude (Anthropic) already spoke — so a paid xAI (Grok) or DeepSeek key goes
first, ahead of every free key; a paid OpenAI or Anthropic key goes last, after the free chain: a third
company on a free key adds more than a second word from the same company. Models checked against the
providers' docs on 2026-10-01: grok-4.7 → grok-4.6 (docs.x.ai), deepseek-v4-pro → deepseek-flash
(api-docs.deepseek.com), claude-opus-5 → claude-sonnet-5 (native Messages API, thinking off so the first
content block is the text), gpt-6-astra → gpt-6.1-sol (Chat Completions, `max_completion_tokens`).

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

# NVIDIA build first: the strongest free models today, three companies on one key without a card
# (Kimi K3 — Moonshot, DeepSeek V4.1 — DeepSeek, GLM-5.3 — Zhipu; integrate.api.nvidia.com/v1/models,
# 2026-10-01). About 40 requests a minute per key, no daily cap. Sign-up asks for a phone (SMS).
NVIDIA_URL = 'https://integrate.api.nvidia.com/v1/chat/completions'
# Order Kimi → GLM → DeepSeek: live on 2026-10-01 GLM-5.3 answered in 12 s, DeepSeek V4.1 stayed
# silent for 90–120 s — the slow one goes last. «Get Contents of URL» has no timeout setting, so a
# silent model holds Trio until the system gives up; only order protects the person.
NVIDIA_MODELS = ['moonshotai/kimi-k3', 'z-ai/glm-5.3', 'deepseek-ai/deepseek-v4.1-flash']
# Service tokens a model may leak into its text: Kimi K3 on NVIDIA ended a live answer (2026-10-01)
# with `<|close|>message`. A trailing «token + word» goes whole, any other token alone.
TOKEN_TAIL_RE = r'(?:<\|[^|>\n]{1,40}\|>[A-Za-z_]{0,20}\s*)+$'
TOKEN_RE = r'<\|[^|>\n]{1,40}\|>'
NVIDIA_KEY_RE = r'nvapi-[0-9A-Za-z_-]{20,}'
GEMINI_URL = 'https://generativelanguage.googleapis.com/v1beta/openai/chat/completions'
# Free quota is counted per model (~20 a day each), and a model may be «high demand» (503) while the
# next one answers — so one key walks a chain. Checked live 2026-10-01: 3.8 answered 503, 3.6 and 2.5
# answered; a key with a spent prepaid balance answers 402 on every model.
# Gemini Pro is not free any more (3.1-pro: 429 «limit 0», 2.5-pro: 404 «no longer available to new
# users» — live, 2026-10-01), so every free Flash, each with its own daily quota.
GEMINI_MODELS = ['gemini-3.8-flash', 'gemini-3.7-flash', 'gemini-3.6-flash', 'gemini-3.5-flash',
                 'gemini-2.5-flash']
OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions'
# OpenRouter's free models (`:free`, price 0), four companies; checked against /api/v1/models and
# with real requests on 2026-10-01. `openrouter/free` is OpenRouter's own router over whichever free
# model is up — the last resort. Nemotron Ultra (empty replies) and Inkling (agent apps only) left out.
OPENROUTER_MODELS = ['nvidia/nemotron-3-super-120b-a12b:free', 'qwen/qwen3.8-27b:free',
                     'google/gemma-4-31b-it:free', 'openrouter/free']
GROQ_URL = 'https://api.groq.com/openai/v1/chat/completions'
GROQ_MODELS = ['qwen/qwen3.8-27b', 'openai/gpt-oss-120b']   # checked against /openai/v1/models
# Keys are picked out of poly-key.txt by how they begin, so the person may paste any number of keys,
# in any order, with any spaces or line breaks around them: nvapi-… → NVIDIA, AIza… / AQ.… → Google
# AI Studio, sk-or-… → OpenRouter, gsk_… → Groq.
GOOGLE_KEY_RE = r'(?:AIza[0-9A-Za-z_-]{30,}|AQ\.[0-9A-Za-z._-]{20,})'
OPENROUTER_KEY_RE = r'sk-or-[0-9A-Za-z_-]{20,}'
GROQ_KEY_RE = r'gsk_[A-Za-z0-9]+'
# Paid keys (optional). Lookarounds keep one key from being read as another: a DeepSeek key is exactly
# sk- and 32 lowercase hex characters; OpenAI is any other sk- that is not OpenRouter's or Anthropic's.
_EDGE_L, _EDGE_R = r'(?<![0-9A-Za-z_-])', r'(?![0-9A-Za-z_-])'
ANTHROPIC_KEY_RE = _EDGE_L + r'sk-ant-[0-9A-Za-z_-]{20,}'
XAI_KEY_RE = _EDGE_L + r'xai-[0-9A-Za-z_-]{20,}'
DEEPSEEK_KEY_RE = _EDGE_L + r'sk-[0-9a-f]{32}' + _EDGE_R
OPENAI_KEY_RE = _EDGE_L + r'sk-(?!ant-|or-)(?![0-9a-f]{32}' + _EDGE_R + r')[0-9A-Za-z_-]{20,}'
ANTHROPIC_URL = 'https://api.anthropic.com/v1/messages'
ANTHROPIC_MODELS = ['claude-opus-5', 'claude-sonnet-5']
OPENAI_URL = 'https://api.openai.com/v1/chat/completions'
OPENAI_MODELS = ['gpt-6-astra', 'gpt-6.1-sol']
XAI_URL = 'https://api.x.ai/v1/chat/completions'
XAI_MODELS = ['grok-4.7', 'grok-4.6']
DEEPSEEK_URL = 'https://api.deepseek.com/chat/completions'
DEEPSEEK_MODELS = ['deepseek-v4-pro', 'deepseek-flash']
ANTHROPIC_MAX_TOKENS = '4096'
# OpenAI's reasoning models count their thinking against max_completion_tokens.
OPENAI_MAX_TOKENS = '8000'
# Groq's free tier allows 1000 OUTPUT tokens a minute; a request that may exceed it is refused
# outright, so the answer is capped below that. 900 is ample for «only what both missed».
MAX_TOKENS = '900'
# OpenRouter's free models think before they answer; the thinking counts against max_tokens.
OPENROUTER_MAX_TOKENS = '4000'


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


def act_post_json(url_uid, key_uid, model_uid, prompt_uid, uid, max_uid=None,
                  max_field='max_tokens'):
    """POST {model, messages:[{role:user, content:prompt}], max_tokens} with a Bearer key.

    OpenAI's current models refuse `max_tokens` on Chat Completions and want `max_completion_tokens`."""
    src = 'Item from List' if max_uid else 'Variable'
    body = top_dict([
        item_text('model', text_token('{M}', {'M': (model_uid, src)})),
        {'WFItemType': 2, 'WFKey': plain('messages'),
         'WFValue': {'Value': [{'WFItemType': 1, 'WFValue': nested_dict([
             item_text('role', plain('user')),
             item_text('content', text_token('{P}', {'P': (prompt_uid, 'Text')})),
         ])}], 'WFSerializationType': 'WFArrayParameterState'}},
        (item_number(max_field, MAX_TOKENS) if max_uid is None else
         {'WFItemType': 3, 'WFKey': plain(max_field),
          'WFValue': text_token('{X}', {'X': (max_uid, 'Item from List')})}),
    ])
    headers = top_dict([
        item_text('Authorization', text_token('Bearer {K}', {'K': (key_uid, src)})),
        item_text('Content-Type', plain('application/json')),
    ])
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.downloadurl',
            'WFWorkflowActionParameters': {'WFURL': text_token('{U}', {'U': (url_uid, src)}),
                                           'WFHTTPMethod': 'POST',
                                           'ShowHeaders': True,
                                           'WFHTTPHeaders': headers,
                                           'WFHTTPBodyType': 'JSON',
                                           'WFJSONValues': body,
                                           'UUID': uid}}


def act_post_anthropic(url_uid, key_uid, model_uid, prompt_uid, max_uid, uid):
    """POST to Anthropic's native Messages API: `x-api-key`, `anthropic-version`, thinking off — so
    content[0] is the text block (with thinking on, content[0] is an empty thinking block)."""
    src = 'Item from List'
    body = top_dict([
        item_text('model', text_token('{M}', {'M': (model_uid, src)})),
        {'WFItemType': 3, 'WFKey': plain('max_tokens'),
         'WFValue': text_token('{X}', {'X': (max_uid, src)})},
        {'WFItemType': 1, 'WFKey': plain('thinking'),
         'WFValue': nested_dict([item_text('type', plain('disabled'))])},
        {'WFItemType': 2, 'WFKey': plain('messages'),
         'WFValue': {'Value': [{'WFItemType': 1, 'WFValue': nested_dict([
             item_text('role', plain('user')),
             item_text('content', text_token('{P}', {'P': (prompt_uid, 'Text')})),
         ])}], 'WFSerializationType': 'WFArrayParameterState'}},
    ])
    headers = top_dict([
        item_text('x-api-key', text_token('{K}', {'K': (key_uid, src)})),
        item_text('anthropic-version', plain('2023-06-01')),
        item_text('Content-Type', plain('application/json')),
    ])
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.downloadurl',
            'WFWorkflowActionParameters': {'WFURL': text_token('{U}', {'U': (url_uid, src)}),
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


def act_replace(src_uid, src_name, find, repl, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.text.replace',
            'WFWorkflowActionParameters': {'WFInput': text_token('{T}', {'T': (src_uid, src_name)}),
                                           'WFReplaceTextFind': find,
                                           'WFReplaceTextReplace': repl,
                                           'WFReplaceTextRegularExpression': True,
                                           'WFReplaceTextCaseSensitive': True,
                                           'UUID': uid}}


def act_combine(src_uid, src_name, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.text.combine',
            'WFWorkflowActionParameters': {'text': attachment(src_uid, src_name),
                                           'WFTextSeparator': 'New Lines', 'UUID': uid}}


def act_split(src_uid, src_name, separator, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.text.split',
            'WFWorkflowActionParameters': {'text': text_token('{T}', {'T': (src_uid, src_name)}),
                                           'WFTextSeparator': 'Custom',
                                           'WFTextCustomSeparator': separator, 'UUID': uid}}


def act_item_at(src_uid, src_name, index, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.getitemfromlist',
            'WFWorkflowActionParameters': {'WFItemSpecifier': 'Item At Index', 'WFItemIndex': index,
                                           'WFInput': attachment(src_uid, src_name), 'UUID': uid}}


def repeat_each(group, src_uid, src_name):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.repeat.each',
            'WFWorkflowActionParameters': {'GroupingIdentifier': group, 'WFControlFlowMode': 0,
                                           'WFInput': attachment(src_uid, src_name)}}


def repeat_each_close(group):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.repeat.each',
            'WFWorkflowActionParameters': {'GroupingIdentifier': group, 'WFControlFlowMode': 2}}


def act_set_from_repeat_item(var_name):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.setvariable',
            'WFWorkflowActionParameters': {'WFVariableName': var_name,
                                           'WFInput': {'Value': {'Type': 'Variable',
                                                                 'VariableName': 'Repeat Item'},
                                                       'WFSerializationType': 'WFTextTokenAttachment'}}}


def if_contains_ref(group, var_name, src_uid, src_name):
    """If <variable> contains the text of an earlier action's output."""
    action = if_contains(group, var_name, '')
    action['WFWorkflowActionParameters']['WFConditionalActionString'] = \
        text_token('{N}', {'N': (src_uid, src_name)})
    return action


def if_output_has_value(group, src_uid, src_name):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.conditional',
            'WFWorkflowActionParameters': {'GroupingIdentifier': group, 'WFControlFlowMode': 0,
                                           'WFCondition': 100,
                                           'WFInput': {'Type': 'Variable',
                                                       'Variable': attachment(src_uid, src_name)}}}


def if_no_value(group, var_name):
    action = if_has_value(group, var_name)
    action['WFWorkflowActionParameters']['WFCondition'] = 101  # «does not have any value»
    return action


# Every free provider and its model chain. One attempt = one (model, key) pair; the shortcut walks
# them in this order — every model of a provider over every key of that provider, then the next
# provider — until someone answers. Names checked live on 2026-10-01 (models lists + real requests).
PROVIDERS = [  # (locale name key, url, key regex, models, max_tokens)
    # paid keys of a THIRD company first (ChatGPT and Claude already spoke)
    ('provider.xai', XAI_URL, XAI_KEY_RE, XAI_MODELS, OPENROUTER_MAX_TOKENS),
    ('provider.deepseek', DEEPSEEK_URL, DEEPSEEK_KEY_RE, DEEPSEEK_MODELS, OPENROUTER_MAX_TOKENS),
    # then the free keys, strongest first
    ('provider.nvidia', NVIDIA_URL, NVIDIA_KEY_RE, NVIDIA_MODELS, OPENROUTER_MAX_TOKENS),
    ('provider.gemini', GEMINI_URL, GOOGLE_KEY_RE, GEMINI_MODELS, MAX_TOKENS),
    ('provider.openrouter', OPENROUTER_URL, OPENROUTER_KEY_RE, OPENROUTER_MODELS, OPENROUTER_MAX_TOKENS),
    ('provider.groq', GROQ_URL, GROQ_KEY_RE, GROQ_MODELS, MAX_TOKENS),
    # paid keys of the two companies already in the pair — last: same company, another model
    ('provider.anthropic', ANTHROPIC_URL, ANTHROPIC_KEY_RE, ANTHROPIC_MODELS, ANTHROPIC_MAX_TOKENS),
    ('provider.openai', OPENAI_URL, OPENAI_KEY_RE, OPENAI_MODELS, OPENAI_MAX_TOKENS),
]

# What a failed reply means. «Get Contents of URL» gives no status code, so the reply's own words
# decide: `"code": 402` (Gemini, OpenRouter) or a known phrase (Groq has no numeric code).
# (kind, dead key?, needles in the reply) — first match wins.
FAILS = [
    ('billing', True, ['"code": 402', '"code":402', 'credits', 'billing', 'credit balance',
                       'insufficient_quota', 'Insufficient Balance']),
    ('region', True, ['location is not supported', 'not available in your country']),
    ('key', True, ['"code": 401', '"code":401', '"code": 403', '"code":403', 'API key', 'API Key',
                   'API_KEY', 'User not found', 'invalid_api_key', 'PERMISSION_DENIED',
                   '"status":401', '"status":403', 'Authorization failed', 'Unauthorized',
                   'authentication_error', 'permission_error', 'Authentication Fails',
                   'Incorrect API key']),
    ('limit', False, ['"code": 429', '"code":429', 'quota', 'rate_limit', 'rate-limited',
                      'RESOURCE_EXHAUSTED', 'Rate limit', '"status":429', 'Too Many Requests',
                      'rate_limit_error']),
    ('busy', False, ['"code": 503', '"code":503', '"code": 500', '"code":500', '"code": 502',
                     '"code":502', 'UNAVAILABLE', 'over capacity', 'high demand', 'overloaded',
                     '"status":500', '"status":502', '"status":503', '"status":504']),
    ('model', False, ['"code": 404', '"code":404', 'NOT_FOUND', 'model_not_found', 'No endpoints',
                      '"status":404', 'not_found_error']),
]


def third_voice(T, V, prompt_uid, keys_uid, keys_name='Variable'):
    """From the finished trio prompt and the saved keys text to V['third'] holding the third voice.

    Every key the person saved is tried with every model of its provider until one answers; a key
    that answered «no money» or «invalid» is not asked again. Only when all failed does V['third']
    get an honest list of what each one said. Shared with the Mac probe, so what is tested on a Mac
    is exactly what ships.
    """
    u = new_uuid
    var = lambda name, default: V.get(name, default)
    attempts_v, log_v, dead_v, why_v = (var('attempts', 'Attempts'), var('log', 'Log'),
                                         var('dead', 'DeadKeys'), var('why', 'Why'))
    actions = []

    # ---- the attempt list: one line «url|model|key|provider|max_tokens» per (model, key)
    parts = {}
    for n, (name_key, url, key_re, models, max_tokens) in enumerate(PROVIDERS):
        found, joined = u(), u()
        actions += [act_match(key_re, keys_uid, keys_name, found),
                    act_combine(found, 'Matches', joined)]
        for m, model in enumerate(models):
            line = u()
            actions.append(act_replace(joined, 'Combined Text', r'([^\n]+)',
                                       f'{url}|{model}|$1|{T[name_key]}|{max_tokens}', line))
            parts[f'P{n}_{m}'] = (line, 'Updated Text')
    all_lines, lines = u(), u()
    actions += [act_text(text_token('\n'.join('{%s}' % k for k in parts), parts), all_lines),
                act_match(r'[^\n]+', all_lines, 'Text', lines)]

    loop, skip_done, skip_dead, ok, has_text = u(), u(), u(), u(), u()
    attempt, split = u(), u()
    f_url, f_model, f_key, f_name, f_max = u(), u(), u(), u(), u()
    post, raw, raw_get, data, choices, first, message, content = (u() for _ in range(8))
    k_get, dead_get, tail_m, tail, label_n, label_m, label = (u() for _ in range(7))
    c_tail, c_clean = u(), u()
    g_ant, g_oai, post_a, raw_a, post_o, raw_o = (u() for _ in range(6))
    a_ok, a_has, a_data, a_content, a_first, a_text = (u() for _ in range(6))
    actions += [
        repeat_each(loop, lines, 'Matches'),
        act_set_from_repeat_item(attempts_v),
        if_no_value(skip_done, V['third']),
        act_get_variable(attempts_v, attempt),
        act_split(attempt, 'Variable', '|', split),
        act_item_at(split, 'Split Text', 1, f_url), act_set_variable(V['url'], f_url, 'Item from List'),
        act_item_at(split, 'Split Text', 2, f_model), act_set_variable(V['model'], f_model, 'Item from List'),
        act_item_at(split, 'Split Text', 3, f_key), act_set_variable(V['key'], f_key, 'Item from List'),
        act_item_at(split, 'Split Text', 4, f_name), act_set_variable(V['provider'], f_name, 'Item from List'),
        act_item_at(split, 'Split Text', 5, f_max),
        act_get_variable(V['key'], k_get),
        # a key that already said «no money» / «invalid» is not asked again
        if_contains_ref(skip_dead, dead_v, k_get, 'Variable'),
        if_else(skip_dead),
        # three dialects: Anthropic's own, OpenAI's with max_completion_tokens, everyone else
        if_contains(g_ant, V['url'], 'api.anthropic.com'),
        act_post_anthropic(f_url, f_key, f_model, prompt_uid, f_max, post_a),
        act_set_variable(V['data'], post_a, 'Contents of URL'),
        act_text(text_token('{R}', {'R': (post_a, 'Contents of URL')}), raw_a),
        act_set_variable(V['raw'], raw_a, 'Text'),
        if_else(g_ant),
        if_contains(g_oai, V['url'], 'api.openai.com'),
        act_post_json(f_url, f_key, f_model, prompt_uid, post_o, max_uid=f_max,
                      max_field='max_completion_tokens'),
        act_set_variable(V['data'], post_o, 'Contents of URL'),
        act_text(text_token('{R}', {'R': (post_o, 'Contents of URL')}), raw_o),
        act_set_variable(V['raw'], raw_o, 'Text'),
        if_else(g_oai),
        act_post_json(f_url, f_key, f_model, prompt_uid, post, max_uid=f_max),
        act_set_variable(V['data'], post, 'Contents of URL'),
        act_text(text_token('{R}', {'R': (post, 'Contents of URL')}), raw),
        act_set_variable(V['raw'], raw, 'Text'),
        if_close(g_oai),
        if_close(g_ant),
        act_get_variable(V['provider'], label_n),
        act_get_variable(V['model'], label_m),
        act_text(text_token('{N} · {M}', {'N': (label_n, 'Variable'), 'M': (label_m, 'Variable')}), label),
        if_contains(ok, V['raw'], '"choices"'),
        act_get_variable(V['data'], data),
        act_value('choices', data, 'Variable', choices),
        act_first_item(choices, 'Dictionary Value', first),
        act_value('message', first, 'Item from List', message),
        act_value('content', message, 'Dictionary Value', content),
        if_output_has_value(has_text, content, 'Dictionary Value'),
        act_replace(content, 'Dictionary Value', TOKEN_TAIL_RE, '', c_tail),
        act_replace(c_tail, 'Updated Text', TOKEN_RE, '', c_clean),
        act_set_variable(V['third'], c_clean, 'Updated Text'),
        act_set_variable(V['provider'], label, 'Text'),
        if_else(has_text),
        *set_text(why_v, T['why.empty'], u()),
        if_close(has_text),
        if_else(ok),
        # Anthropic's answer: {"content":[{"type":"text","text":…}], "stop_reason":…}; its errors
        # never carry stop_reason
        if_contains(a_ok, V['raw'], 'stop_reason'),
        act_get_variable(V['data'], a_data),
        act_value('content', a_data, 'Variable', a_content),
        act_first_item(a_content, 'Dictionary Value', a_first),
        act_value('text', a_first, 'Item from List', a_text),
        if_output_has_value(a_has, a_text, 'Dictionary Value'),
        act_set_variable(V['third'], a_text, 'Dictionary Value'),
        act_set_variable(V['provider'], label, 'Text'),
        if_else(a_has),
        *set_text(why_v, T['why.empty'], u()),
        if_close(a_has),
        if_else(a_ok),
    ]

    groups = []
    for kind, dead, needles in FAILS:
        for needle in needles:
            group = u()
            groups.append(group)
            actions += [if_contains(group, V['raw'], needle), *set_text(why_v, T[f'why.{kind}'], u())]
            if dead:
                d_old, d_new = u(), u()
                actions += [act_get_variable(dead_v, d_old),
                            act_text(text_token('{D}\n{K}', {'D': (d_old, 'Variable'),
                                                            'K': (k_get, 'Variable')}), d_new),
                            act_set_variable(dead_v, d_new, 'Text')]
            actions.append(if_else(group))
    actions += set_text(why_v, T['why.other'], u())
    actions += [if_close(group) for group in reversed(groups)]
    actions.append(if_close(a_ok))
    actions.append(if_close(ok))

    # one line of the honest list: «• Gemini · gemini-3.8-flash (key …x1Ab): overloaded»
    why_get, log_old, log_new = u(), u(), u()
    actions += [
        if_has_value(has_why := u(), why_v),
        act_match(r'.{4}$', k_get, 'Variable', tail_m),
        act_first_item(tail_m, 'Matches', tail),
        act_get_variable(why_v, why_get),
        act_get_variable(log_v, log_old),
        act_text(text_token('{L}\n• {P} (…{K}): {W}', {'L': (log_old, 'Variable'), 'P': (label, 'Text'),
                                                       'K': (tail, 'Item from List'),
                                                       'W': (why_get, 'Variable')}), log_new),
        act_set_variable(log_v, log_new, 'Text'),
        *set_text(why_v, '', u()),
        if_close(has_why),
        if_close(skip_dead),
        if_close(skip_done),
        repeat_each_close(loop),
    ]

    # ---- nobody answered: say what each one said and what to do
    none, any_log, log_get = u(), u(), u()
    actions += [
        if_no_value(none, V['third']),
        if_has_value(any_log, log_v),
        act_get_variable(log_v, log_get),
        *set_text(V['third'], T['error.all'], u(), {'L': (log_get, 'Variable')}),
        if_else(any_log),
        *set_text(V['third'], T['error.nokeys'], u()),
        if_close(any_log),
        *set_text(V['provider'], T['provider.none'], u()),
        if_close(none),
    ]
    return actions


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
    k_get, k_file, k_ask, k_save, k_var = ids(5)
    question, wrap, gpt, critique, claude = ids(5)
    t_prompt, = ids(1)
    f_third, f_provider, f_claude, f_out = ids(4)
    g_key, = ids(1)
    Q = {'Q': (question, 'Provided Input')}

    actions = [
        act_comment(T['comment']),

        # ---- the keys: from iCloud Drive → Shortcuts → poly-key.txt, or asked once and saved there.
        # Any number of free keys, one per line; each is recognised by how it begins.
        act_get_file(T['files.key'], k_get),
        act_set_variable(V['key_file'], k_get, 'File'),
        if_has_value(g_key, V['key_file']),
        *set_text(V['keys'], '{F}', k_file, {'F': (k_get, 'File')}),
        if_else(g_key),
        dict(act_ask(T['ask.key'], k_ask), WFWorkflowActionParameters={
            **act_ask(T['ask.key'], k_ask)['WFWorkflowActionParameters'], 'WFAllowsMultilineText': True}),
        act_save_file(T['files.key'], k_ask, k_save),
        act_set_variable(V['keys'], k_ask, 'Provided Input'),
        if_close(g_key),
        act_get_variable(V['keys'], k_var),

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
        *third_voice(T, V, t_prompt, k_var),

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
    workflow['WFWorkflowIcon'] = {'WFWorkflowIconStartColor': 3679049983,   # purple (kin to Duo's violet)
                                  'WFWorkflowIconGlyphNumber': 59800}      # people (a group)
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
