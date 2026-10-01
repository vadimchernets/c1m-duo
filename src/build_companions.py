#!/usr/bin/env python3
"""Build the C1 companion shortcuts for one locale.

Usage:  python3 src/build_companions.py <lang>
Output: dist/<lang>/Poly Voice.shortcut, Poly Photo.shortcut, Poly Quiet.shortcut,
        Poly Compress.shortcut, Poly Multi.shortcut

Voice     — tap, dictate, hear the final answer read aloud.
Photo     — share a photo or PDF, text is recognized on device and handed to Poly.
Quiet     — the Critique pipeline with no screens: clipboard and journal only.
Compress  — shrink a long text with the on-device Apple model, then hand it to Poly.
Multi     — PRO: the automatic pair plus as many hand-polled AIs as you want.
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_shortcut import (  # noqa: E402
    ROOT, Locale, new_uuid, text_token, attachment, variable, validate,
    act_ask, act_gpt, act_claude, act_text, act_set_variable, act_get_variable,
    act_date, act_notify, act_comment, act_clipboard, act_append_file,
    act_run_shortcut, menu_open, menu_case, menu_close, SHARE_INPUT,
)
import plistlib  # noqa: E402


def act_speak(uid, name):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.speaktext',
            'WFWorkflowActionParameters': {'WFText': attachment(uid, name)}}


def act_show_result(uid, name):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.showresult',
            'WFWorkflowActionParameters': {'Text': text_token('{R}', {'R': (uid, name)})}}


def act_detect_text(uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.detect.text',
            'WFWorkflowActionParameters': {'UUID': uid,
                                           'WFInput': {'Value': dict(SHARE_INPUT),
                                                       'WFSerializationType': 'WFTextTokenAttachment'}}}


def act_ask_llm(prompt, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.askllm',
            'WFWorkflowActionParameters': {'WFLLMModel': 'Apple Intelligence',
                                           'WFGenerativeResultType': 'Text',
                                           'WFLLMPrompt': prompt, 'UUID': uid}}


def act_alert(title, message):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.alert',
            'WFWorkflowActionParameters': {'WFAlertActionTitle': title,
                                           'WFAlertActionMessage': message,
                                           'WFAlertActionCancelButtonShown': False}}


def act_get_clipboard(uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.getclipboard',
            'WFWorkflowActionParameters': {'UUID': uid}}


def act_append_variable(name, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.appendvariable',
            'WFWorkflowActionParameters': {'WFVariableName': name,
                                           'WFInput': attachment(uid, 'Clipboard')}}


def repeat_open(group, count_uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.repeat.count',
            'WFWorkflowActionParameters': {
                'GroupingIdentifier': group, 'WFControlFlowMode': 0,
                'WFRepeatCount': {'Value': {'OutputUUID': count_uid, 'Type': 'ActionOutput',
                                            'OutputName': 'Provided Input'},
                                  'WFSerializationType': 'WFTextTokenAttachment'}}}


def repeat_close(group):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.repeat.count',
            'WFWorkflowActionParameters': {'GroupingIdentifier': group, 'WFControlFlowMode': 2}}


def write(lang, name, actions, color, glyph, types=None, classes=None, share_input=False):
    validate(actions)
    workflow = plistlib.loads((ROOT / 'src' / 'metadata.plist').read_bytes())
    workflow['WFWorkflowIcon'] = {'WFWorkflowIconStartColor': color,
                                  'WFWorkflowIconGlyphNumber': glyph}
    workflow['WFWorkflowTypes'] = types if types is not None else []
    workflow['WFWorkflowInputContentItemClasses'] = classes if classes is not None else []
    if share_input:
        workflow['WFWorkflowHasShortcutInputVariables'] = True
    workflow['WFWorkflowActions'] = actions
    out_dir = Path(os.environ.get('C1_DIST', ROOT / 'dist')) / lang
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / f'{name}.shortcut').open('wb') as f:
        plistlib.dump(workflow, f, fmt=plistlib.FMT_BINARY)
    print(f'{lang}: {name} — {len(actions)} actions')


TEXT_CLASSES = ['WFStringContentItem', 'WFURLContentItem']


def build(lang):
    L = Locale(lang)
    RESULT = L['variables.result']
    names = L['shortcut_names']
    journal_file = L['files.journal']

    # ---------------------------------------------------------------- Voice
    q, wrap, gpt, prompt, claude, entry, date = (new_uuid() for _ in range(7))
    Q = {'Q': (q, 'Provided Input')}
    voice = [
        {'WFWorkflowActionIdentifier': 'is.workflow.actions.ask',
         'WFWorkflowActionParameters': {'WFAskActionPrompt': L['ask.voice_question'],
                                        'WFAskActionImmediateDictation': True, 'UUID': q}},
        act_notify(L['notify.voice_start']),
        act_text(text_token(L.prompt('wrap'), Q), wrap),
        act_gpt(text_token('{P}', {'P': (wrap, 'Text')}), gpt),
        act_text(text_token(L.prompt('critique'),
                            {'QUESTION': (q, 'Provided Input'),
                             'GPT_ANSWER': (gpt, 'Ask ChatGPT')}), prompt),
        act_claude(text_token('{P}', {'P': (prompt, 'Text')}), claude),
        act_clipboard(attachment(claude, 'Ask Claude')),
        act_speak(claude, 'Ask Claude'),
        act_show_result(claude, 'Ask Claude'),
        act_date(date),
        act_text(text_token(L['journal.entry_simple'].replace('{M}', L['journal.voice']),
                            {**Q, 'D': (date, 'Date'), 'R': (claude, 'Ask Claude')}), entry),
        act_append_file(journal_file, entry),
    ]
    write(lang, names['voice'], voice, 4292093695, 59785)

    # ---------------------------------------------------------------- Compress
    prompt_uid, llm_uid = new_uuid(), new_uuid()
    compress = [
        act_text(text_token(L.prompt('squeeze'), special={'TEXT': SHARE_INPUT}), prompt_uid),
        act_ask_llm(text_token('{P}', {'P': (prompt_uid, 'Text')}), llm_uid),
        act_run_shortcut(names['main'], llm_uid, 'Ask AI'),
    ]
    write(lang, names['compress'], compress, 431817727, 61440,
          types=['ActionExtension'], classes=TEXT_CLASSES, share_input=True)

    # ---------------------------------------------------------------- Photo
    ocr = new_uuid()
    photo = [
        act_comment(L['comment.photo']),
        act_detect_text(ocr),
        act_notify(L['notify.photo_done']),
        act_run_shortcut(names['main'], ocr, 'Text'),
    ]
    write(lang, names['photo'], photo, 946986751, 59511,
          types=['ActionExtension'],
          classes=['WFImageContentItem', 'WFPDFContentItem'], share_input=True)

    # ---------------------------------------------------------------- Quiet
    q4, wrap4, gpt4, prompt4, claude4, entry4, date4 = (new_uuid() for _ in range(7))
    Q4 = {'Q': (q4, 'Provided Input')}
    quiet = [
        act_ask(L['ask.quiet_question'], q4, prefill_from_share=True),
        act_text(text_token(L.prompt('wrap'), Q4), wrap4),
        act_gpt(text_token('{P}', {'P': (wrap4, 'Text')}), gpt4),
        act_text(text_token(L.prompt('critique'),
                            {'QUESTION': (q4, 'Provided Input'),
                             'GPT_ANSWER': (gpt4, 'Ask ChatGPT')}), prompt4),
        act_claude(text_token('{P}', {'P': (prompt4, 'Text')}), claude4),
        act_clipboard(attachment(claude4, 'Ask Claude')),
        act_date(date4),
        act_text(text_token(L['journal.entry_simple'].replace('{M}', L['journal.quiet']),
                            {**Q4, 'D': (date4, 'Date'), 'R': (claude4, 'Ask Claude')}), entry4),
        act_append_file(journal_file, entry4),
    ]
    write(lang, names['quiet'], quiet, 4278222847, 61440,
          types=['ActionExtension'], classes=TEXT_CLASSES, share_input=True)

    # ---------------------------------------------------------------- Multi (PRO)
    (mq, mwrap, mgpt, mclaude, mcount, mclip, mempty, mextra, mfinal_prompt,
     mp1, mp2, mclaude_final, mentry, mdate) = (new_uuid() for _ in range(14))
    g_loop, g_merge = new_uuid(), new_uuid()
    MQ = {'Q': (mq, 'Provided Input')}
    EXTRA_ANSWERS = L['variables.extra_answers']
    FINAL_PROMPT = L['variables.final_prompt']
    merge_refs = {**MQ, 'G': (mgpt, 'Ask ChatGPT'), 'C': (mclaude, 'Ask Claude'),
                  'EXTRA': (mextra, 'Variable')}
    multi = [
        act_comment(L['comment.multi']),
        act_ask(L['ask.multi_question'], mq, prefill_from_share=True),
        act_notify(L['notify.multi_step1']),
        act_text(text_token(L.prompt('wrap'), MQ), mwrap),
        act_gpt(text_token('{P}', {'P': (mwrap, 'Text')}), mgpt),
        act_claude(text_token('{P}', {'P': (mwrap, 'Text')}), mclaude),
        act_clipboard(attachment(mwrap, 'Text')),
        {'WFWorkflowActionIdentifier': 'is.workflow.actions.ask',
         'WFWorkflowActionParameters': {'WFAskActionPrompt': L['ask.multi_count'],
                                        'WFInputType': 'Number', 'UUID': mcount}},
        # the variable must exist even when the loop runs zero times
        act_text(text_token(''), mempty),
        act_set_variable(EXTRA_ANSWERS, mempty, 'Text'),
        repeat_open(g_loop, mcount),
        act_alert(L['alert.multi_next_title'], L['alert.multi_next_body']),
        act_get_clipboard(mclip),
        act_append_variable(EXTRA_ANSWERS, mclip),
        repeat_close(g_loop),
        act_notify(L['notify.multi_step3']),
        act_get_variable(EXTRA_ANSWERS, mextra),
        menu_open(g_merge, L['menu.multi_merge_title'], L['menu.multi_merge_items']),
        menu_case(g_merge, L['menu.multi_merge_items'][0]),
        act_text(text_token(L.prompt('multi-merge'), merge_refs), mp1),
        act_set_variable(FINAL_PROMPT, mp1, 'Text'),
        menu_case(g_merge, L['menu.multi_merge_items'][1]),
        act_text(text_token(L.prompt('multi-merge-east-west'), merge_refs), mp2),
        act_set_variable(FINAL_PROMPT, mp2, 'Text'),
        menu_close(g_merge),
        act_get_variable(FINAL_PROMPT, mfinal_prompt),
        act_claude(text_token('{P}', {'P': (mfinal_prompt, 'Variable')}), mclaude_final),
        act_clipboard(attachment(mclaude_final, 'Ask Claude')),
        act_show_result(mclaude_final, 'Ask Claude'),
        act_date(mdate),
        act_text(text_token(L['journal.entry_simple'].replace('{M}', L['journal.multi']),
                            {**MQ, 'D': (mdate, 'Date'),
                             'R': (mclaude_final, 'Ask Claude')}), mentry),
        act_append_file(journal_file, mentry),
    ]
    write(lang, names['multi'], multi, 4290822336, 59511,
          types=['ActionExtension'], classes=TEXT_CLASSES, share_input=True)


if __name__ == '__main__':
    languages = sys.argv[1:] or [d.name for d in sorted((ROOT / 'locales').iterdir()) if d.is_dir()]
    for language in languages:
        build(language)
