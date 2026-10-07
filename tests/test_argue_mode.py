"""Duo «Debate until agreement»: ChatGPT takes a side, Claude objects, up to three rounds, a side
that is convinced starts its reply with the marker and the rounds stop; then Claude sums up."""
import json
import os
import plistlib
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
LANGS = sorted(d.name for d in (ROOT / 'locales').iterdir() if d.is_dir())
MARKER = '[[CONCEDE]]'
PROMPTS = ROOT / 'locales' / 'en' / 'prompts'


def ui(lang):
    return json.loads((ROOT / 'locales' / lang / 'ui.json').read_text(encoding='utf-8'))


def build(tmp_path, lang):
    env = dict(os.environ, C1_DIST=str(tmp_path))
    subprocess.run([sys.executable, str(ROOT / 'src' / 'build_shortcut.py'), lang], check=True,
                   cwd=ROOT, env=env, capture_output=True)
    name = ui(lang)['shortcut_names']['main']
    return plistlib.loads((tmp_path / lang / f'{name}.shortcut').read_bytes())['WFWorkflowActions']


def test_prompts_carry_the_marker_and_the_three_sections():
    for name in ('argue-2-object', 'argue-3-reply'):
        text = (PROMPTS / f'{name}.txt').read_text(encoding='utf-8')
        assert MARKER in text and '{ROUND}' in text and '{LOG}' in text and '{QUESTION}' in text
    opening = (PROMPTS / 'argue-1-open.txt').read_text(encoding='utf-8')
    assert MARKER not in opening and '{Q}' in opening
    verdict = (PROMPTS / 'argue-4-verdict.txt').read_text(encoding='utf-8')
    for section in ('Where they agreed', 'Where the dispute remains', 'What you decide'):
        assert section in verdict


@pytest.mark.parametrize('lang', LANGS)
def test_mode_sits_next_to_critique(lang):
    items = ui(lang)['menu']['main_items']
    assert len(items) == 7 and items[1].startswith('🤝') and '3–8✉' in items[1]
    assert '🤝' in ui(lang)['help']


@pytest.mark.parametrize('lang', ['en', 'es', 'pt', 'ru', 'uk'])
def test_three_rounds_that_stop_on_the_marker(tmp_path, lang):
    actions = build(tmp_path, lang)
    log = ui(lang)['variables']['argue_log']
    guards = [a['WFWorkflowActionParameters'] for a in actions
              if a['WFWorkflowActionIdentifier'] == 'is.workflow.actions.conditional'
              and a['WFWorkflowActionParameters'].get('WFConditionalActionString') == MARKER]
    # each round: before Claude objects and before ChatGPT answers
    assert len(guards) == 6
    assert all(g['WFCondition'] == 99 and g['WFInput']['Variable']['Value']['VariableName'] == log
               for g in guards)
    start = next(i for i, a in enumerate(actions)
                 if a['WFWorkflowActionParameters'].get('WFMenuItemTitle') == ui(lang)['menu']['main_items'][1])
    end = next(i for i, a in enumerate(actions)
               if a['WFWorkflowActionParameters'].get('WFMenuItemTitle') == ui(lang)['menu']['main_items'][2])
    branch = [a['WFWorkflowActionIdentifier'] for a in actions[start:end]]
    assert branch.count('com.openai.chat.AskIntent') == 4          # opening + three answers
    assert branch.count('com.anthropic.claude.ClaudeAppIntentsExtension') == 4   # three objections + summary
