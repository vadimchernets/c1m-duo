#!/usr/bin/env python3
"""Generator for the "Poly Choirs" Tasker project (Android, clipboard-relay style):
four tasks — All AIs / West / East / East-West (a special East-vs-West rollup).

Clones the proven action blocks out of poly-clipboard-relay.prj.xml, so the choir
tasks behave exactly like the two-AI relay, just looped over a longer app list.

Usage:
    python3 generate_choirs.py en      # writes en/poly-choirs.prj.xml
    python3 generate_choirs.py ru      # writes ru/poly-choirs.prj.xml

Edit the WEST / EAST lists below to change which apps are in the choir, then rerun.
"""
import sys
import copy
import json
import xml.etree.ElementTree as ET
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
LOCALES_DIR = SCRIPT_DIR.parent / "locales"

# Canonical lineup: 5 US AIs + 5 China AIs. A "~" marks a package that hasn't been
# confirmed to be the correct, currently-published one. If the app isn't installed,
# the task will stop when it tries to launch it — remove that entry after import,
# or edit the list here and regenerate.
WEST = [  # US AIs
    ("ChatGPT",  "com.openai.chatgpt"),
    ("Claude",   "com.anthropic.claude"),
    ("Gemini",   "com.google.android.apps.bard"),
    ("Grok",     "ai.x.grok"),             # ~
    ("Meta AI",  "com.facebook.stella"),   # ~
]
EAST = [  # China AIs
    ("DeepSeek", "com.deepseek.chat"),
    ("Qwen",     "com.alibaba.qianwen"),   # ~
    ("Kimi",     "com.moonshot.kimi"),     # ~
    ("Ernie",    "com.baidu.newapp"),      # ~ (Baidu Wenxin Yiyan / Ernie Bot)
    ("GLM",      "com.zhipuai.qingyan"),   # ~ (Zhipu / Z.ai)
]
# Optional extras outside the canonical ten (uncomment to include):
# WEST += [("Perplexity", "ai.perplexity.app.android"), ("Copilot", "com.microsoft.copilot")]

# ---------------------------------------------------------------------------
# Per-language strings live in locales/<lang>/choirs.json (English is the base
# language; every other locale is a translation of it, same keys). The four
# "*_flash"/"*_label" entries that used to be lambdas are now .format()
# templates — see locales/en/choirs.json for the placeholder names.
# ---------------------------------------------------------------------------


def load_strings(lang):
    return json.loads((LOCALES_DIR / lang / "choirs.json").read_text(encoding="utf-8"))


def build(lang: str):
    tr = load_strings(lang)
    donor_path = SCRIPT_DIR / lang / "poly-clipboard-relay.prj.xml"
    out_path = SCRIPT_DIR / lang / "poly-choirs.prj.xml"

    tree = ET.parse(donor_path)
    root = tree.getroot()
    go = next(t for t in root.findall("Task") if t.find("nme").text == "Duo Go")
    A = go.findall("Action")

    # Locate the starting action by its Tasker action code, not by list index —
    # that way, if actions get added earlier in the donor task, cloning still
    # starts from the right place.
    BASE = next(i for i, a in enumerate(A) if a.find("code").text == "548")

    def clone(i):
        return copy.deepcopy(A[BASE + i])

    def set_str(action, idx, value):
        action.findall("Str")[idx].text = value

    # Template for a "Variable Set <var> to empty" action, used to clear stale
    # per-run variables at the top of each task.
    CLR_TEMPLATE = next(a for a in A[:BASE] if a.find("code").text == "547")

    def clear_var(name):
        action = copy.deepcopy(CLR_TEMPLATE)
        strs = action.findall("Str")
        strs[0].text = name
        strs[1].text = None
        return action

    def build_task(tid, name, apps, merge_text):
        # Clear last run's answers first, so a stale value from a previous run
        # can't leak into this run's merge or journal.
        actions = [clear_var(f"%POLYANS{i}") for i in range(1, len(apps) + 1)]
        actions += [clear_var("%DuoFinal"), clear_var("%DuoFile"), clone(0), clone(1)]

        for n, (app_name, pkg) in enumerate(apps, 1):
            actions.append(clone(2))
            launch = clone(3)
            for el in launch.iter("appPkg"):
                el.text = pkg
            for el in launch.iter("label"):
                el.text = app_name
            actions.append(launch)
            flash = clone(4)
            set_str(flash, 0, tr["step_flash"].format(n=n, total=len(apps), name=app_name))
            actions.append(flash)
            actions.append(clone(5))
            wait = clone(6)
            set_str(wait, 0, f"%POLYANS{n}")
            actions.append(wait)

        merge_value = merge_text + f"\n{tr['my_question_label']}:\n%DuoQuestion\n\n" + "".join(
            f"{tr['answer_from_label'].format(i=i, name=app_name)}\n%POLYANS{i}\n\n"
            for i, (app_name, _) in enumerate(apps, 1)
        )
        merge_prompt = clone(12)
        set_str(merge_prompt, 1, merge_value)
        actions.append(merge_prompt)
        actions.append(clone(13))
        actions.append(clone(14))

        final_flash = clone(15)
        set_str(final_flash, 0, tr["final_flash"].format(name=name, total=len(apps)))
        actions.append(final_flash)
        actions.append(clone(16))
        actions.append(clone(17))

        # Assemble the journal text before the Write File action that saves it.
        journal = clone(18)
        journal_body = f"{tr['journal_question_label']}:\n%DuoQuestion\n\n" + "".join(
            f"=== {app_name} ===\n%POLYANS{i}\n\n" for i, (app_name, _) in enumerate(apps, 1)
        ) + f"{tr['journal_summary_label'].format(name=name)}\n%DuoFinal\n"
        set_str(journal, 1, journal_body)
        actions.append(journal)

        write_file = clone(19)
        for str_el in write_file.findall("Str"):
            if str_el.text and "Tasker/Poly" in str_el.text:
                str_el.text = str_el.text.replace(".txt", f"-{tid}.txt")
        actions.append(write_file)
        actions.append(clone(20))

        done_flash = clone(21)
        set_str(done_flash, 0, tr["done_flash"].format(name=name))
        actions.append(done_flash)

        task = ET.Element("Task", {"sr": f"task{tid}"})
        for tag, val in [("cdate", "1788235200000"), ("id", str(tid)), ("nme", name), ("pri", "100")]:
            ET.SubElement(task, tag).text = val
        ET.SubElement(task, "stayawake").text = "true"
        for i, action in enumerate(actions):
            action.set("sr", f"act{i}")
            task.append(action)
        return task

    out = ET.Element("TaskerData", dict(root.attrib))
    project = copy.deepcopy(root.find("Project"))
    project.find("name").text = tr["project_name"]
    project.find("tids").text = "150,151,152,153"
    out.append(project)

    names = tr["task_names"]
    out.append(build_task(150, names["all"], WEST + EAST, tr["merge_base"]))
    out.append(build_task(151, names["west"], WEST, tr["merge_base"]))
    out.append(build_task(152, names["east"], EAST, tr["merge_base"]))
    out.append(build_task(153, names["east_west"], WEST + EAST, tr["merge_base"] + tr["merge_ew_extra"]))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(out).write(out_path, encoding="UTF-8", xml_declaration=True)
    print(
        f"{out_path}: 4 choirs — "
        f"all({len(WEST) + len(EAST)}) / west({len(WEST)}) / east({len(EAST)}) / east-west({len(WEST) + len(EAST)})"
    )


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("en", "ru"):
        sys.exit("usage: python3 generate_choirs.py en|ru")
    build(sys.argv[1])
