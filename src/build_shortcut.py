#!/usr/bin/env python3
"""Build the main C1 shortcut (Poly) for one locale.

Usage:  python3 src/build_shortcut.py <lang>        # e.g. en, ru
Output: dist/<lang>/Poly.shortcut  (unsigned; tools/build.sh signs it)

Every user-visible string comes from locales/<lang>/ — the code carries no text.
Adding a language means adding a locale folder, nothing else.
"""
import json
import plistlib
import re
import os
import sys
import uuid as uuidlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OBJ = '￼'  # object replacement char: marks an inserted value inside a text token

# ---------------------------------------------------------------- locale

class Locale:
    def __init__(self, lang):
        self.lang = lang
        base = ROOT / 'locales' / lang
        if not base.is_dir():
            sys.exit(f'locale not found: {base}')
        self.ui = json.loads((base / 'ui.json').read_text(encoding='utf-8'))
        # prompts are shared: the models read them, not the user, and English works best.
        # A locale may override any of them by dropping a file into locales/<lang>/prompts/.
        self.prompts_dirs = [base / 'prompts', ROOT / 'locales' / 'en' / 'prompts']

    def __getitem__(self, dotted):
        node = self.ui
        for part in dotted.split('.'):
            node = node[part]
        return node

    def prompt(self, name):
        for directory in self.prompts_dirs:
            path = directory / f'{name}.txt'
            if path.exists():
                return path.read_text(encoding='utf-8').rstrip('\n')
        sys.exit(f'prompt not found: {name}')


# ---------------------------------------------------------------- plist helpers

def new_uuid():
    return str(uuidlib.uuid4()).upper()


def text_token(template, refs=None, special=None):
    """Build a WFTextTokenString.

    refs:    marker -> (action uuid, output name)   — reference to an action's output
    special: marker -> ready-made attachment dict   — e.g. the share-sheet input

    Only ActionOutput references are placed inside strings; dates and variables are
    fetched by their own actions first (see act_date / act_get_variable) so that the
    text always renders on device.
    """
    refs, special = refs or {}, special or {}
    keys = list(refs) + list(special)
    out, attachments = '', {}
    if keys:
        pattern = re.compile(r'\{(' + '|'.join(re.escape(k) for k in keys) + r')\}')
        last = 0
        for m in pattern.finditer(template):
            out += template[last:m.start()]
            key = m.group(1)
            if key in refs:
                attachment = {'OutputUUID': refs[key][0], 'Type': 'ActionOutput',
                              'OutputName': refs[key][1]}
            else:
                attachment = dict(special[key])
            # offsets are counted in UTF-16 code units, as Shortcuts expects
            attachments['{%d, 1}' % (len(out.encode('utf-16-le')) // 2)] = attachment
            out += OBJ
            last = m.end()
        out += template[last:]
    else:
        out = template
    return {'Value': {'string': out, 'attachmentsByRange': attachments},
            'WFSerializationType': 'WFTextTokenString'}


def attachment(uid, name):
    return {'Value': {'OutputUUID': uid, 'Type': 'ActionOutput', 'OutputName': name},
            'WFSerializationType': 'WFTextTokenAttachment'}


def variable(name):
    return {'Value': {'Type': 'Variable', 'VariableName': name},
            'WFSerializationType': 'WFTextTokenAttachment'}


SHARE_INPUT = {'Type': 'ExtensionInput'}


def act_ask(prompt, uid, default=None, prefill_from_share=False):
    params = {'WFAskActionPrompt': prompt, 'UUID': uid}
    if prefill_from_share:
        params['WFAskActionDefaultAnswer'] = text_token('{S}', special={'S': SHARE_INPUT})
    elif default is not None:
        params['WFAskActionDefaultAnswer'] = text_token(default)
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.ask',
            'WFWorkflowActionParameters': params}


def act_gpt(prompt, uid):
    return {'WFWorkflowActionIdentifier': 'com.openai.chat.AskIntent',
            'WFWorkflowActionParameters': {
                'AppIntentDescriptor': {'TeamIdentifier': '2DC432GLL2',
                                        'BundleIdentifier': 'com.openai.chat',
                                        'Name': 'ChatGPT', 'AppIntentIdentifier': 'AskIntent'},
                'newChat': True, 'continuous': False,
                'model': {'identifier': 'auto', 'title': {'key': 'Auto'},
                          'subtitle': {'key': 'Auto'}},
                'ShowWhenRun': False, 'prompt': prompt, 'UUID': uid}}


def act_claude(message, uid):
    return {'WFWorkflowActionIdentifier': 'com.anthropic.claude.ClaudeAppIntentsExtension',
            'WFWorkflowActionParameters': {
                'AppIntentDescriptor': {'TeamIdentifier': 'Q6L2SF6YDW',
                                        'BundleIdentifier': 'com.anthropic.claude',
                                        'Name': 'Claude',
                                        'AppIntentIdentifier': 'ClaudeAppIntentsExtension'},
                'ShowWhenRun': False, 'message': message, 'UUID': uid}}


def act_text(token, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.gettext',
            'WFWorkflowActionParameters': {'WFTextActionText': token, 'UUID': uid}}


def act_set_variable(name, src_uid, src_name):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.setvariable',
            'WFWorkflowActionParameters': {'WFVariableName': name,
                                           'WFInput': attachment(src_uid, src_name)}}


def act_get_variable(name, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.getvariable',
            'WFWorkflowActionParameters': {'WFVariable': variable(name), 'UUID': uid}}


def act_date(uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.date',
            'WFWorkflowActionParameters': {'WFDateActionMode': 'Current Date', 'UUID': uid}}


def act_notify(body):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.notification',
            'WFWorkflowActionParameters': {'WFNotificationActionTitle': 'Poly',
                                           'WFNotificationActionBody': body,
                                           'WFNotificationActionSound': False}}


def act_comment(text):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.comment',
            'WFWorkflowActionParameters': {'WFCommentActionText': text}}


def act_clipboard(source):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.setclipboard',
            'WFWorkflowActionParameters': {'WFInput': source, 'WFLocalOnly': False}}


def act_quick_look(source):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.previewdocument',
            'WFWorkflowActionParameters': {'WFInput': source}}


def act_append_file(path, src_uid):
    # a text field needs a token STRING (not a bare attachment) to receive a value
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.file.append',
            'WFWorkflowActionParameters': {'WFFileStorageService': 'iCloud Drive',
                                           'WFFilePath': path,
                                           'WFAppendFileWriteMode': 'Append',
                                           'WFInput': text_token('{T}', {'T': (src_uid, 'Text')})}}


def act_save_file(path, src_uid, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.documentpicker.save',
            'WFWorkflowActionParameters': {'WFFileStorageService': 'iCloud Drive',
                                           'WFAskWhereToSave': False,
                                           'WFFileDestinationPath': path,
                                           'WFSaveFileOverwrite': True,
                                           'WFInput': text_token('{H}', {'H': (src_uid, 'Text')}),
                                           'UUID': uid}}


def act_get_file(path, uid):
    # a missing file is not an error here: the action returns nothing and the shortcut goes on
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.documentpicker.open',
            'WFWorkflowActionParameters': {'WFFileStorageService': 'iCloud Drive',
                                           'WFGetFilePath': path,
                                           'WFShowFilePicker': False,
                                           'WFFileErrorIfNotFound': False,
                                           'UUID': uid}}


def act_alert(title, message):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.alert',
            'WFWorkflowActionParameters': {'WFAlertActionTitle': title,
                                           'WFAlertActionMessage': message,
                                           'WFAlertActionCancelButtonShown': False}}


def act_run_shortcut(name, src_uid, src_name):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.runworkflow',
            'WFWorkflowActionParameters': {'WFWorkflowName': name, 'WFShowWorkflow': False,
                                           'WFInput': attachment(src_uid, src_name)}}


def menu_open(group, title, items):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.choosefrommenu',
            'WFWorkflowActionParameters': {'GroupingIdentifier': group, 'WFControlFlowMode': 0,
                                           'WFMenuPrompt': title, 'WFMenuItems': items}}


def menu_case(group, title):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.choosefrommenu',
            'WFWorkflowActionParameters': {'GroupingIdentifier': group, 'WFControlFlowMode': 1,
                                           'WFMenuItemTitle': title}}


def menu_close(group):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.choosefrommenu',
            'WFWorkflowActionParameters': {'GroupingIdentifier': group, 'WFControlFlowMode': 2}}


def if_has_value(group, var_name):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.conditional',
            'WFWorkflowActionParameters': {'GroupingIdentifier': group, 'WFControlFlowMode': 0,
                                           'WFCondition': 100,
                                           'WFInput': {'Type': 'Variable',
                                                       'Variable': variable(var_name)}}}


def if_contains(group, var_name, needle):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.conditional',
            'WFWorkflowActionParameters': {'GroupingIdentifier': group, 'WFControlFlowMode': 0,
                                           'WFCondition': 99,  # «contains»
                                           'WFConditionalActionString': needle,
                                           'WFInput': {'Type': 'Variable',
                                                       'Variable': variable(var_name)}}}


def if_else(group):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.conditional',
            'WFWorkflowActionParameters': {'GroupingIdentifier': group, 'WFControlFlowMode': 1}}


def if_close(group):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.conditional',
            'WFWorkflowActionParameters': {'GroupingIdentifier': group, 'WFControlFlowMode': 2}}


# ---------------------------------------------------------------- weekly version check
#
# A shortcut cannot replace itself, so it only offers the new one (distribution decision of 2026-10-02, item e).
# At most once in 7 days, at the very END of a run — after the answer is on screen, in the clipboard
# and in the journal — it reads releases/version.json: GitHub raw first, the site copy second. If the
# number there is higher than the one built in, one line asks «a new version is out — install?» and
# «Install» opens the iCloud link for this language from the same file. The day of the last check is
# the modification date of a small file next to poly-key.txt (iCloud Drive → Shortcuts). The network
# is checked first by actions that cannot throw (Wi-Fi name, else cellular radio): offline, the check
# is silently skipped and tried again on the next run; an empty or non-JSON answer means «no update».

VERSION_FILE = ROOT / 'releases' / 'version.json'
VERSION_URLS = ('https://raw.githubusercontent.com/vadimchernets/c1m-duo/main/releases/version.json',
                'https://polyhelper.ai/duo/version.json')
VERSION_DAYS = 7
# The name the main shortcut is released under (releases/<lang>/Duo.shortcut, the iCloud record, the
# site). iOS names an imported shortcut after it, so «another mode — same question» calls this name.
RELEASE_NAME = 'Duo'
# «Debate until agreement»: a side that is genuinely convinced starts its reply with this marker
# (the prompts argue-2-object / argue-3-reply ask for it); the shortcut stops the rounds when it appears.
ARGUE_MARKER = '[[CONCEDE]]'


def built_version(key):
    """The number this build carries: the one in releases/version.json at build time."""
    return int(json.loads(VERSION_FILE.read_text(encoding='utf-8'))[key])


def act_download(url, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.downloadurl',
            'WFWorkflowActionParameters': {'WFURL': url, 'UUID': uid}}


def act_dict_value(key, src_uid, src_name, uid):
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.getvalueforkey',
            'WFWorkflowActionParameters': {'WFGetDictionaryValueType': 'Value',
                                           'WFDictionaryKey': key,
                                           'WFInput': attachment(src_uid, src_name),
                                           'UUID': uid}}


def if_output(group, src_uid, src_name, condition, **numbers):
    """If <an earlier action's output> <condition> — 100 has any value, 2 greater than, 1003 between."""
    params = {'GroupingIdentifier': group, 'WFControlFlowMode': 0, 'WFCondition': condition,
              'WFInput': {'Type': 'Variable', 'Variable': attachment(src_uid, src_name)}}
    params.update(numbers)
    return {'WFWorkflowActionIdentifier': 'is.workflow.actions.conditional',
            'WFWorkflowActionParameters': params}


def if_no_value(group, var_name):
    action = if_has_value(group, var_name)
    action['WFWorkflowActionParameters']['WFCondition'] = 101  # «does not have any value»
    return action


def version_check(L, key, name, lang):
    """Actions of the weekly version check for the shortcut `key` ('duo' or 'trio') in `lang`."""
    ids = lambda n: [new_uuid() for _ in range(n)]
    (f_get, f_date, now, age, far, age_get, stamp_now, stamp, stamp_save,
     wifi, cell, net_get, gh, site, json_get, remote, link) = ids(17)
    g_file, g_due, g_wifi, g_net, g_gh, g_site, g_json, g_new, g_menu = ids(9)
    age_var, json_var, net_var = f'{name}VersionAge', f'{name}VersionJson', f'{name}Network'
    stamp_file = f'{name}-version-check.txt'
    needle = f'"{key}":'
    install, later = L['update.install'], L['update.later']
    return [
        act_comment(f'Version check: at most once in {VERSION_DAYS} days, '
                    f'{VERSION_URLS[0]} then {VERSION_URLS[1]}; this build is '
                    f'{key} {built_version(key)}.'),
        act_get_file(stamp_file, f_get),
        if_output(g_file, f_get, 'File', 100),
        {'WFWorkflowActionIdentifier': 'is.workflow.actions.properties.files',
         'WFWorkflowActionParameters': {'WFInput': attachment(f_get, 'File'),
                                        'WFContentItemPropertyName': 'Last Modified Date',
                                        'UUID': f_date}},
        act_date(now),
        {'WFWorkflowActionIdentifier': 'is.workflow.actions.gettimebetweendates',
         'WFWorkflowActionParameters': {'WFInput': attachment(now, 'Date'),
                                        'WFTimeUntilFromDate': text_token(
                                            '{D}', {'D': (f_date, 'Last Modified Date')}),
                                        'WFTimeUntilUnit': 'Days', 'UUID': age}},
        act_set_variable(age_var, age, 'Time Between Dates'),
        if_else(g_file),
        {'WFWorkflowActionIdentifier': 'is.workflow.actions.number',
         'WFWorkflowActionParameters': {'WFNumberActionNumber': 999, 'UUID': far}},
        act_set_variable(age_var, far, 'Number'),
        if_close(g_file),
        act_get_variable(age_var, age_get),
        # «between −7 and 7 days» reads the same whichever way the system counts the difference
        if_output(g_due, age_get, 'Variable', 1003,
                  WFNumberValue=-VERSION_DAYS, WFAnotherNumber=VERSION_DAYS),
        if_else(g_due),
        # Offline, «Get Contents of URL» stops the shortcut with a system error, and Shortcuts has
        # no try/catch. So the network goes first, by actions that never throw: a Wi-Fi network
        # name, else a cellular radio technology. Neither → no check this run, no stamp, no error.
        {'WFWorkflowActionIdentifier': 'is.workflow.actions.getwifi',
         'WFWorkflowActionParameters': {'WFNetworkDetailsNetwork': 'Wi-Fi',
                                        'WFWiFiDetail': 'Network Name', 'UUID': wifi}},
        act_set_variable(net_var, wifi, 'Network Details'),
        if_no_value(g_wifi, net_var),
        {'WFWorkflowActionIdentifier': 'is.workflow.actions.getwifi',
         'WFWorkflowActionParameters': {'WFNetworkDetailsNetwork': 'Cellular',
                                        'WFCellularDetail': 'Radio Technology', 'UUID': cell}},
        act_set_variable(net_var, cell, 'Network Details'),
        if_close(g_wifi),
        act_get_variable(net_var, net_get),
        if_output(g_net, net_get, 'Variable', 100),
        act_date(stamp_now),
        act_text(text_token('{D}', {'D': (stamp_now, 'Date')}), stamp),
        act_save_file(stamp_file, stamp, stamp_save),
        # An empty answer, a 404 page or HTML from a proxy is «no update»: only a text that
        # contains the key is ever read as a dictionary.
        act_download(VERSION_URLS[0], gh),
        if_output(g_gh, gh, 'Contents of URL', 99, WFConditionalActionString=needle),
        act_set_variable(json_var, gh, 'Contents of URL'),
        if_else(g_gh),
        act_download(VERSION_URLS[1], site),
        if_output(g_site, site, 'Contents of URL', 99, WFConditionalActionString=needle),
        act_set_variable(json_var, site, 'Contents of URL'),
        if_close(g_site),
        if_close(g_gh),
        act_get_variable(json_var, json_get),
        if_output(g_json, json_get, 'Variable', 99, WFConditionalActionString=needle),
        act_dict_value(key, json_get, 'Variable', remote),
        if_output(g_new, remote, 'Dictionary Value', 2, WFNumberValue=built_version(key)),
        act_dict_value(f'{key}_{lang}', json_get, 'Variable', link),
        menu_open(g_menu, L['update.prompt'].replace('{NAME}', name), [install, later]),
        menu_case(g_menu, install),
        {'WFWorkflowActionIdentifier': 'is.workflow.actions.openurl',
         'WFWorkflowActionParameters': {'WFInput': text_token('{L}', {'L': (link, 'Dictionary Value')}),
                                        'Show-WFInput': True}},
        menu_case(g_menu, later),
        menu_close(g_menu),
        if_close(g_new),
        if_close(g_json),
        if_close(g_net),
        if_close(g_due),
    ]


IMAGE_GALLERY_HTML = (
    '<!DOCTYPE html><html><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1"><style>'
    'body{font-family:-apple-system,sans-serif;background:#111;color:#eee;margin:0;padding:14px}'
    'h2{margin:4px 0 14px}figure{margin:0 0 26px}'
    'svg{width:100%;height:auto;background:#fff;border-radius:14px;display:block}'
    'figcaption{margin-top:8px;font-size:15px;letter-spacing:.5px;color:#9ad}'
    '</style></head><body><h2>{TITLE}</h2>'
    '<figure>{C}<figcaption>{CAP_C}</figcaption></figure>'
    '<figure>{G}<figcaption>{CAP_G}</figcaption></figure></body></html>'
)


# ---------------------------------------------------------------- build

def build(lang):
    L = Locale(lang)
    RESULT = L['variables.result']
    JOURNAL_EXTRA = L['variables.journal_extra']
    MAIN = L['menu.main_items']
    EXTRA = L['menu.extra_items']

    ids = lambda n: [new_uuid() for _ in range(n)]
    question, = ids(1)
    Q = {'Q': (question, 'Provided Input')}
    QUESTION = {'QUESTION': (question, 'Provided Input')}

    g_main, g_extra, g_anchor, g_image, g_empty, g_finale = ids(6)
    g_notice, = ids(1)

    def journal_note(template, refs=None):
        """Per-branch note: mode name plus the raw drafts that produced the result."""
        uid = new_uuid()
        return [act_text(text_token(template, refs or {}), uid),
                act_set_variable(JOURNAL_EXTRA, uid, 'Text')]

    # --- Critique
    cr_wrap, cr_gpt, cr_prompt, cr_claude = ids(4)
    # --- Debate until agreement (see argue_round below)
    ar_open, ar_gpt, ar_log0, ar_get, ar_prompt, ar_verdict, ar_out, ar_log_final = ids(8)
    ARGUE_LOG = L['variables.argue_log']
    # --- Advisor
    ad_prompt, ad_claude = ids(2)
    # --- Side by side
    sb_wrap, sb_gpt, sb_claude, sb_join = ids(4)
    # --- Synthesis, Claude anchors / ChatGPT anchors
    sc_wrap, sc_gpt, sc_claude, sc_prompt, sc_final = ids(5)
    sg_wrap, sg_gpt, sg_claude, sg_prompt, sg_final = ids(5)
    # --- Auto
    au_prompt, au_gpt, au_text = ids(3)
    # --- Decision
    de_fast, de_gpt, de_caution, de_claude, de_referee, de_final = ids(6)
    # --- Dispute map
    dm_wrap, dm_gpt, dm_claude, dm_prompt, dm_final = ids(5)
    # --- Debate
    db_wrap, db_draft, db_crit_prompt, db_crit, db_rev_prompt, db_rev, db_judge_prompt, db_judge = ids(8)
    # --- Clarify
    cl_prompt, cl_gpt, cl_ask, cl_final_prompt, cl_final = ids(5)
    # --- Image: sketches only / sketches + judge
    i1_brief, i1_gpt, i1_claude, i1_html, i1_file, i1_codes = ids(6)
    i2_brief, i2_gpt, i2_claude, i2_html, i2_file, i2_raw, i2_judge_prompt, i2_judge, i2_codes = ids(9)
    # --- Delta
    dl_wrap, dl_claude, dl_prompt, dl_gpt, dl_join = ids(5)
    # --- Help
    hp_text, = ids(1)
    # --- Tail
    tl_date, tl_extra, tl_result, tl_entry = ids(4)
    # --- The one-time word about the PC version
    pc_get, pc_text, pc_save = ids(3)

    def argue_round(n):
        """One round of «Debate until agreement»: Claude objects, ChatGPT answers. Each half runs only
        while nobody has conceded — the debate log does not yet contain the marker."""
        g_obj, g_rep = ids(2)
        get1, pr1, cl1, get2, add1, get3, pr2, gp2, get4, add2 = ids(10)
        rnd = str(n)
        return [
            if_contains(g_obj, ARGUE_LOG, ARGUE_MARKER),
            if_else(g_obj),
            act_notify(L['notify.argue_object'].replace('{N}', rnd)),
            act_get_variable(ARGUE_LOG, get1),
            act_text(text_token(L.prompt('argue-2-object').replace('{ROUND}', rnd),
                                {**QUESTION, 'LOG': (get1, 'Variable')}), pr1),
            act_claude(text_token('{P}', {'P': (pr1, 'Text')}), cl1),
            act_get_variable(ARGUE_LOG, get2),
            act_text(text_token('{L}\n\n' + L['output.argue_side_b_round'].replace('{N}', rnd) + '\n{B}',
                                {'L': (get2, 'Variable'), 'B': (cl1, 'Ask Claude')}), add1),
            act_set_variable(ARGUE_LOG, add1, 'Text'),
            if_contains(g_rep, ARGUE_LOG, ARGUE_MARKER),
            if_else(g_rep),
            act_notify(L['notify.argue_reply'].replace('{N}', rnd)),
            act_get_variable(ARGUE_LOG, get3),
            act_text(text_token(L.prompt('argue-3-reply').replace('{ROUND}', rnd),
                                {**QUESTION, 'LOG': (get3, 'Variable')}), pr2),
            act_gpt(text_token('{P}', {'P': (pr2, 'Text')}), gp2),
            act_get_variable(ARGUE_LOG, get4),
            act_text(text_token('{L}\n\n' + L['output.argue_side_a_round'].replace('{N}', rnd) + '\n{A}',
                                {'L': (get4, 'Variable'), 'A': (gp2, 'Ask ChatGPT')}), add2),
            act_set_variable(ARGUE_LOG, add2, 'Text'),
            if_close(g_rep),
            if_close(g_obj),
        ]

    actions = [
        act_comment(L['comment.main']),

        # ---- Once, on the very first run: PolyHelper on a laptop or PC does more. Shown before the question so the
        # person reads it at once and nothing of a run is interrupted; a marker file next to the journal
        # (iCloud Drive → Shortcuts) says it was shown, so it never comes back. No marker (the first run, or the
        # file was deleted) → shown once more; a missing file is not an error. The help screen keeps its paragraph.
        act_get_file(L['files.pc_notice'], pc_get),
        act_set_variable(L['variables.pc_notice_seen'], pc_get, 'File'),
        if_has_value(g_notice, L['variables.pc_notice_seen']),
        if_else(g_notice),
        act_alert(L['alert.pc_notice_title'], L['alert.pc_notice_body']),
        act_text(text_token(L['alert.pc_notice_body']), pc_text),
        act_save_file(L['files.pc_notice'], pc_text, pc_save),
        if_close(g_notice),

        act_ask(L['ask.question'], question, prefill_from_share=True),
        menu_open(g_main, L['menu.main_title'], MAIN),

        # ---- Critique: ChatGPT answers, Claude verifies and finalizes
        menu_case(g_main, MAIN[0]),
        act_notify(L['notify.critique_start']),
        act_text(text_token(L.prompt('wrap'), Q), cr_wrap),
        act_gpt(text_token('{P}', {'P': (cr_wrap, 'Text')}), cr_gpt),
        act_text(text_token(L.prompt('critique'),
                            {**QUESTION, 'GPT_ANSWER': (cr_gpt, 'Ask ChatGPT')}), cr_prompt),
        act_notify(L['notify.critique_step2']),
        act_claude(text_token('{P}', {'P': (cr_prompt, 'Text')}), cr_claude),
        act_set_variable(RESULT, cr_claude, 'Ask Claude'),
        *journal_note(L['journal.critique'], {'X': (cr_gpt, 'Ask ChatGPT')}),

        # ---- Debate until agreement: ChatGPT takes a side, Claude objects, ChatGPT answers… up to three
        # rounds; a side that is convinced starts its reply with the marker and the debate stops there.
        # Then Claude, as a neutral recorder: where they agreed / what is still disputed / what you decide.
        menu_case(g_main, MAIN[1]),
        act_notify(L['notify.argue_start']),
        act_text(text_token(L.prompt('argue-1-open'), Q), ar_open),
        act_gpt(text_token('{P}', {'P': (ar_open, 'Text')}), ar_gpt),
        act_text(text_token(L['output.argue_side_a'] + '\n{A}', {'A': (ar_gpt, 'Ask ChatGPT')}), ar_log0),
        act_set_variable(ARGUE_LOG, ar_log0, 'Text'),
        *argue_round(1), *argue_round(2), *argue_round(3),
        act_notify(L['notify.argue_verdict']),
        act_get_variable(ARGUE_LOG, ar_get),
        act_text(text_token(L.prompt('argue-4-verdict'),
                            {**QUESTION, 'LOG': (ar_get, 'Variable')}), ar_prompt),
        act_claude(text_token('{P}', {'P': (ar_prompt, 'Text')}), ar_verdict),
        act_get_variable(ARGUE_LOG, ar_log_final),
        act_text(text_token(L['output.argue'], {'V': (ar_verdict, 'Ask Claude'),
                                                'L': (ar_log_final, 'Variable')}), ar_out),
        act_set_variable(RESULT, ar_out, 'Text'),
        *journal_note(L['journal.argue']),

        # ---- Advisor: Claude reviews the user's own text without rewriting it
        menu_case(g_main, MAIN[2]),
        act_notify(L['notify.advisor_start']),
        act_text(text_token(L.prompt('advisor'), Q), ad_prompt),
        act_claude(text_token('{P}', {'P': (ad_prompt, 'Text')}), ad_claude),
        act_set_variable(RESULT, ad_claude, 'Ask Claude'),
        *journal_note(L['journal.advisor']),

        # ---- Side by side: both answer independently, answers shown together
        menu_case(g_main, MAIN[3]),
        act_notify(L['notify.survey_start']),
        act_text(text_token(L.prompt('wrap'), Q), sb_wrap),
        act_gpt(text_token('{P}', {'P': (sb_wrap, 'Text')}), sb_gpt),
        act_claude(text_token('{P}', {'P': (sb_wrap, 'Text')}), sb_claude),
        act_text(text_token(L['output.survey'],
                            {'G': (sb_gpt, 'Ask ChatGPT'), 'C': (sb_claude, 'Ask Claude')}), sb_join),
        act_set_variable(RESULT, sb_join, 'Text'),
        *journal_note(L['journal.survey']),

        # ---- Synthesis: both answer blind, then one of them anchors the assembly
        menu_case(g_main, MAIN[4]),
        menu_open(g_anchor, L['menu.anchor_title'], L['menu.anchor_items']),

        menu_case(g_anchor, L['menu.anchor_items'][0]),
        act_notify(L['notify.synthesis_claude_start']),
        act_text(text_token(L.prompt('wrap'), Q), sc_wrap),
        act_gpt(text_token('{P}', {'P': (sc_wrap, 'Text')}), sc_gpt),
        act_claude(text_token('{P}', {'P': (sc_wrap, 'Text')}), sc_claude),
        act_text(text_token(L.prompt('synthesis-anchor-claude'),
                            {**QUESTION, 'GPT_ANSWER': (sc_gpt, 'Ask ChatGPT'),
                             'CLAUDE_ANSWER': (sc_claude, 'Ask Claude')}), sc_prompt),
        act_claude(text_token('{P}', {'P': (sc_prompt, 'Text')}), sc_final),
        act_set_variable(RESULT, sc_final, 'Ask Claude'),
        *journal_note(L['journal.synthesis_claude'],
                      {'X': (sc_gpt, 'Ask ChatGPT'), 'Y': (sc_claude, 'Ask Claude')}),

        menu_case(g_anchor, L['menu.anchor_items'][1]),
        act_notify(L['notify.synthesis_gpt_start']),
        act_text(text_token(L.prompt('wrap'), Q), sg_wrap),
        act_gpt(text_token('{P}', {'P': (sg_wrap, 'Text')}), sg_gpt),
        act_claude(text_token('{P}', {'P': (sg_wrap, 'Text')}), sg_claude),
        act_text(text_token(L.prompt('synthesis-anchor-gpt'),
                            {**QUESTION, 'GPT_ANSWER': (sg_gpt, 'Ask ChatGPT'),
                             'CLAUDE_ANSWER': (sg_claude, 'Ask Claude')}), sg_prompt),
        act_claude(text_token('{P}', {'P': (sg_prompt, 'Text')}), sg_final),
        act_set_variable(RESULT, sg_final, 'Ask Claude'),
        *journal_note(L['journal.synthesis_gpt'],
                      {'X': (sg_gpt, 'Ask ChatGPT'), 'Y': (sg_claude, 'Ask Claude')}),
        menu_close(g_anchor),

        # ---- Auto: one classification call recommends the mode to use
        menu_case(g_main, MAIN[5]),
        act_notify(L['notify.auto_start']),
        act_text(text_token(L.prompt('auto-router'), Q), au_prompt),
        act_gpt(text_token('{P}', {'P': (au_prompt, 'Text')}), au_gpt),
        act_text(text_token(L['output.auto'], {'R': (au_gpt, 'Ask ChatGPT')}), au_text),
        act_set_variable(RESULT, au_text, 'Text'),
        *journal_note(L['journal.auto']),

        # ---- More…: the less frequent modes plus built-in help
        menu_case(g_main, MAIN[6]),
        menu_open(g_extra, L['menu.extra_title'], EXTRA),

        # ---- Decision: fast view, cautious view, referee
        menu_case(g_extra, EXTRA[0]),
        act_notify(L['notify.decision_start']),
        act_text(text_token(L.prompt('decision-1-fast'), Q), de_fast),
        act_gpt(text_token('{P}', {'P': (de_fast, 'Text')}), de_gpt),
        act_notify(L['notify.decision_step2']),
        act_text(text_token(L.prompt('decision-2-cautious'), Q), de_caution),
        act_claude(text_token('{P}', {'P': (de_caution, 'Text')}), de_claude),
        act_notify(L['notify.decision_step3']),
        act_text(text_token(L.prompt('decision-3-referee'),
                            {**QUESTION, 'FAST': (de_gpt, 'Ask ChatGPT'),
                             'CAUTIOUS': (de_claude, 'Ask Claude')}), de_referee),
        act_claude(text_token('{P}', {'P': (de_referee, 'Text')}), de_final),
        act_set_variable(RESULT, de_final, 'Ask Claude'),
        *journal_note(L['journal.decision'],
                      {'X': (de_gpt, 'Ask ChatGPT'), 'Y': (de_claude, 'Ask Claude')}),

        # ---- Dispute map: where the two agree, where they don't, what to verify
        menu_case(g_extra, EXTRA[1]),
        act_notify(L['notify.disputemap_start']),
        act_text(text_token(L.prompt('wrap'), Q), dm_wrap),
        act_gpt(text_token('{P}', {'P': (dm_wrap, 'Text')}), dm_gpt),
        act_claude(text_token('{P}', {'P': (dm_wrap, 'Text')}), dm_claude),
        act_text(text_token(L.prompt('dispute-map'),
                            {**QUESTION, 'GPT_ANSWER': (dm_gpt, 'Ask ChatGPT'),
                             'CLAUDE_ANSWER': (dm_claude, 'Ask Claude')}), dm_prompt),
        act_claude(text_token('{P}', {'P': (dm_prompt, 'Text')}), dm_final),
        act_set_variable(RESULT, dm_final, 'Ask Claude'),
        *journal_note(L['journal.disputemap'],
                      {'X': (dm_gpt, 'Ask ChatGPT'), 'Y': (dm_claude, 'Ask Claude')}),

        # ---- Debate: draft, opponent, revision, judge
        menu_case(g_extra, EXTRA[2]),
        act_notify(L['notify.debate_start']),
        act_text(text_token(L.prompt('wrap'), Q), db_wrap),
        act_gpt(text_token('{P}', {'P': (db_wrap, 'Text')}), db_draft),
        act_notify(L['notify.debate_step2']),
        act_text(text_token(L.prompt('debate-1-opponent'),
                            {**QUESTION, 'DRAFT': (db_draft, 'Ask ChatGPT')}), db_crit_prompt),
        act_claude(text_token('{P}', {'P': (db_crit_prompt, 'Text')}), db_crit),
        act_notify(L['notify.debate_step3']),
        act_text(text_token(L.prompt('debate-2-revise'),
                            {**QUESTION, 'DRAFT': (db_draft, 'Ask ChatGPT'),
                             'CRITIQUE': (db_crit, 'Ask Claude')}), db_rev_prompt),
        act_gpt(text_token('{P}', {'P': (db_rev_prompt, 'Text')}), db_rev),
        act_notify(L['notify.debate_step4']),
        act_text(text_token(L.prompt('debate-3-judge'),
                            {**QUESTION, 'ANSWER': (db_rev, 'Ask ChatGPT'),
                             'CRITIQUE': (db_crit, 'Ask Claude')}), db_judge_prompt),
        act_claude(text_token('{P}', {'P': (db_judge_prompt, 'Text')}), db_judge),
        act_set_variable(RESULT, db_judge, 'Ask Claude'),
        *journal_note(L['journal.debate'],
                      {'X': (db_draft, 'Ask ChatGPT'), 'Y': (db_crit, 'Ask Claude'),
                       'Z': (db_rev, 'Ask ChatGPT')}),

        # ---- Clarify: ask the user what's missing, then answer
        menu_case(g_extra, EXTRA[3]),
        act_notify(L['notify.clarify_step1']),
        act_text(text_token(L.prompt('clarify-1-questions'), Q), cl_prompt),
        act_gpt(text_token('{P}', {'P': (cl_prompt, 'Text')}), cl_gpt),
        act_ask(text_token('{Q}' + L['ask.clarify_suffix'], {'Q': (cl_gpt, 'Ask ChatGPT')}),
                cl_ask, default=L['ask.clarify_default']),
        act_notify(L['notify.clarify_step2']),
        act_text(text_token(L.prompt('clarify-2-final'),
                            {**Q, 'QUESTIONS': (cl_gpt, 'Ask ChatGPT'),
                             'USER_ANSWERS': (cl_ask, 'Provided Input')}), cl_final_prompt),
        act_claude(text_token('{P}', {'P': (cl_final_prompt, 'Text')}), cl_final),
        act_set_variable(RESULT, cl_final, 'Ask Claude'),
        *journal_note(L['journal.clarify'],
                      {'X': (cl_gpt, 'Ask ChatGPT'), 'Y': (cl_ask, 'Provided Input')}),

        # ---- Image: both draw SVG blind, gallery is shown, judge is optional
        menu_case(g_extra, EXTRA[4]),
        menu_open(g_image, L['menu.image_title'], L['menu.image_items']),

        menu_case(g_image, L['menu.image_items'][0]),
        act_notify(L['notify.image_step1']),
        act_text(text_token(L.prompt('image-svg-brief'), Q), i1_brief),
        act_gpt(text_token('{P}', {'P': (i1_brief, 'Text')}), i1_gpt),
        act_notify(L['notify.image_step2']),
        act_claude(text_token('{P}', {'P': (i1_brief, 'Text')}), i1_claude),
        act_text(text_token(IMAGE_GALLERY_HTML.replace('{TITLE}', L['output.image_html_title'])
                            .replace('{CAP_C}', L['output.image_html_claude'])
                            .replace('{CAP_G}', L['output.image_html_gpt']),
                            {'C': (i1_claude, 'Ask Claude'), 'G': (i1_gpt, 'Ask ChatGPT')}), i1_html),
        act_text(text_token(L['output.image_codes'],
                            {'C': (i1_claude, 'Ask Claude'), 'G': (i1_gpt, 'Ask ChatGPT')}), i1_codes),
        # the raw SVG code reaches the clipboard before the file is written
        act_clipboard(attachment(i1_codes, 'Text')),
        act_save_file(L['files.image_html'], i1_html, i1_file),
        act_quick_look(attachment(i1_file, 'Saved File')),
        act_set_variable(RESULT, i1_codes, 'Text'),
        *journal_note(L['journal.image']),

        menu_case(g_image, L['menu.image_items'][1]),
        act_notify(L['notify.image_step1']),
        act_text(text_token(L.prompt('image-svg-brief'), Q), i2_brief),
        act_gpt(text_token('{P}', {'P': (i2_brief, 'Text')}), i2_gpt),
        act_notify(L['notify.image_step2']),
        act_claude(text_token('{P}', {'P': (i2_brief, 'Text')}), i2_claude),
        act_text(text_token(IMAGE_GALLERY_HTML.replace('{TITLE}', L['output.image_html_title'])
                            .replace('{CAP_C}', L['output.image_html_claude'])
                            .replace('{CAP_G}', L['output.image_html_gpt']),
                            {'C': (i2_claude, 'Ask Claude'), 'G': (i2_gpt, 'Ask ChatGPT')}), i2_html),
        act_text(text_token(L['output.image_codes'],
                            {'C': (i2_claude, 'Ask Claude'), 'G': (i2_gpt, 'Ask ChatGPT')}), i2_raw),
        act_clipboard(attachment(i2_raw, 'Text')),
        act_save_file(L['files.image_html'], i2_html, i2_file),
        act_quick_look(attachment(i2_file, 'Saved File')),
        act_notify(L['notify.image_judge']),
        act_text(text_token(L.prompt('image-judge'),
                            {**QUESTION, 'SKETCH1': (i2_claude, 'Ask Claude'),
                             'SKETCH2': (i2_gpt, 'Ask ChatGPT')}), i2_judge_prompt),
        act_claude(text_token('{P}', {'P': (i2_judge_prompt, 'Text')}), i2_judge),
        act_text(text_token(L['output.image_codes_judged'],
                            {'J': (i2_judge, 'Ask Claude'), 'C': (i2_claude, 'Ask Claude'),
                             'G': (i2_gpt, 'Ask ChatGPT')}), i2_codes),
        act_set_variable(RESULT, i2_codes, 'Text'),
        *journal_note(L['journal.image']),
        menu_close(g_image),

        # ---- Delta: Claude anchors, ChatGPT returns only what it would add
        menu_case(g_extra, EXTRA[5]),
        act_notify(L['notify.delta_step1']),
        act_text(text_token(L.prompt('wrap'), Q), dl_wrap),
        act_claude(text_token('{P}', {'P': (dl_wrap, 'Text')}), dl_claude),
        act_notify(L['notify.delta_step2']),
        act_text(text_token(L.prompt('delta'),
                            {**QUESTION, 'ANCHOR': (dl_claude, 'Ask Claude')}), dl_prompt),
        act_gpt(text_token('{P}', {'P': (dl_prompt, 'Text')}), dl_gpt),
        act_text(text_token(L['output.delta'],
                            {'C': (dl_claude, 'Ask Claude'), 'G': (dl_gpt, 'Ask ChatGPT')}), dl_join),
        act_set_variable(RESULT, dl_join, 'Text'),
        *journal_note(L['journal.delta']),

        # ---- Help: what C1 is and which mode to pick, free of AI calls
        menu_case(g_extra, EXTRA[6]),
        act_notify(L['notify.help']),
        act_text(text_token(L['help']), hp_text),
        act_set_variable(RESULT, hp_text, 'Text'),
        *journal_note(L['journal.help']),
        menu_close(g_extra),
        menu_close(g_main),

        # ---- Shared tail: deliver, then record, then offer another run
        act_clipboard(variable(RESULT)),
        act_notify(L['notify.tail_done']),
        if_has_value(g_empty, RESULT),
        if_else(g_empty),
        act_notify(L['notify.tail_empty']),
        if_close(g_empty),
        act_quick_look(variable(RESULT)),
        act_date(tl_date),
        act_get_variable(JOURNAL_EXTRA, tl_extra),
        act_get_variable(RESULT, tl_result),
        act_text(text_token(L['journal.entry'],
                            {**Q, 'D': (tl_date, 'Date'), 'JX': (tl_extra, 'Variable'),
                             'R': (tl_result, 'Variable')}), tl_entry),
        act_append_file(L['files.journal'], tl_entry),
        menu_open(g_finale, L['menu.finale_title'], L['menu.finale_items']),
        menu_case(g_finale, L['menu.finale_items'][0]),
        menu_case(g_finale, L['menu.finale_items'][1]),
        act_run_shortcut(RELEASE_NAME, question, 'Provided Input'),
        menu_close(g_finale),

        # ---- Last of all, at most once a week: is there a newer Duo? (see version_check)
        *version_check(L, 'duo', RELEASE_NAME, lang),
    ]

    validate(actions)
    workflow = plistlib.loads((ROOT / 'src' / 'metadata.plist').read_bytes())
    workflow['WFWorkflowIcon'] = {'WFWorkflowIconStartColor': 2071128575,   # violet (lilac, near Poly A1 accent)
                                  'WFWorkflowIconGlyphNumber': 59403}      # two chat bubbles
    workflow['WFWorkflowTypes'] = ['ActionExtension']
    workflow['WFWorkflowInputContentItemClasses'] = ['WFStringContentItem', 'WFURLContentItem',
                                                     'WFRichTextContentItem', 'WFArticleContentItem']
    workflow['WFWorkflowHasShortcutInputVariables'] = True
    workflow['WFQuickActionSurfaces'] = ['ShareSheet']
    workflow['WFWorkflowActions'] = actions

    out_dir = Path(os.environ.get('C1_DIST', ROOT / 'dist')) / lang
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{L['shortcut_names.main']}.shortcut"
    with out.open('wb') as f:
        plistlib.dump(workflow, f, fmt=plistlib.FMT_BINARY)
    print(f'{lang}: {out.name} — {len(actions)} actions')


def validate(actions):
    """Structural checks that must hold for the shortcut to run correctly."""
    seen_uuid, flow_stack, produced = {}, [], set()
    menus = {}
    for i, action in enumerate(actions):
        params = action['WFWorkflowActionParameters']

        uid = params.get('UUID')
        if uid:
            assert uid not in seen_uuid, f'duplicate action UUID at {i} and {seen_uuid[uid]}'
            seen_uuid[uid] = i

        mode = params.get('WFControlFlowMode')
        if mode == 0:
            flow_stack.append(params['GroupingIdentifier'])
            if 'WFMenuItems' in params:
                menus[params['GroupingIdentifier']] = list(params['WFMenuItems'])
        elif mode == 1:
            assert flow_stack and flow_stack[-1] == params['GroupingIdentifier'], \
                f'case outside its group at {i}'
            title = params.get('WFMenuItemTitle')
            if title is not None:
                items = menus[params['GroupingIdentifier']]
                assert title in items, f'menu case without a matching item: {title!r}'
                items.remove(title)
        elif mode == 2:
            assert flow_stack and flow_stack.pop() == params['GroupingIdentifier'], \
                f'group closed out of order at {i}'

        for ref in collect_references(params):
            assert ref in produced or ref == uid, f'action {i} references a later action'
        if uid:
            produced.add(uid)

    assert not flow_stack, 'unbalanced control flow'
    for group, leftovers in menus.items():
        assert not leftovers, f'menu items without a case: {leftovers}'

    for token in collect_text_tokens(actions):
        string, ranges = token['string'], token.get('attachmentsByRange', {})
        utf16 = string.encode('utf-16-le')
        for position, att in ranges.items():
            offset = int(position.strip('{}').split(',')[0])
            assert utf16[offset * 2:offset * 2 + 2].decode('utf-16-le', 'replace') == OBJ, \
                'text token offset does not point at a placeholder'
            assert att.get('Type') in ('ActionOutput', 'ExtensionInput'), \
                'only action outputs and share input may be embedded in text'


def collect_references(node, found=None):
    found = set() if found is None else found
    if isinstance(node, dict):
        if node.get('Type') == 'ActionOutput':
            found.add(node['OutputUUID'])
        for value in node.values():
            collect_references(value, found)
    elif isinstance(node, list):
        for value in node:
            collect_references(value, found)
    return found


def collect_text_tokens(node, found=None):
    found = [] if found is None else found
    if isinstance(node, dict):
        if node.get('WFSerializationType') == 'WFTextTokenString':
            found.append(node['Value'])
        for value in node.values():
            collect_text_tokens(value, found)
    elif isinstance(node, list):
        for value in node:
            collect_text_tokens(value, found)
    return found


if __name__ == '__main__':
    languages = sys.argv[1:] or [d.name for d in sorted((ROOT / 'locales').iterdir()) if d.is_dir()]
    for language in languages:
        build(language)
