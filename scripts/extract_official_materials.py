from __future__ import annotations

import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "app-core-v2.5.0.html"
CONTEXT = {"schoolYear": 2026, "courseCode": "LE1", "courseName": "論理・表現Ⅰ", "grade": 1}
TARGETS = {
    "pack_e_lesson8_jodoushi1_yoshu": "practice",
    "pack_e_lesson8_anshou": "recitation",
}


def extract_sample_packs(text: str) -> list[dict]:
    match = re.search(r"const SAMPLE_PACKS=(\[.*?\]);\s*/\*==教材ここまで==\*/", text, re.S)
    if not match:
        raise RuntimeError("SAMPLE_PACKS block not found in frozen core")
    return json.loads(match.group(1))


def enrich(pack: dict, material_type: str) -> dict:
    pack = copy.deepcopy(pack)
    pack.update({
        "version": 2,
        "schoolYear": CONTEXT["schoolYear"],
        "courseCode": CONTEXT["courseCode"],
        "courseName": CONTEXT["courseName"],
        "materialType": material_type,
        "_englishLadderExternal": True,
    })
    if material_type == "recitation":
        for unit in pack.get("units", []):
            tab = unit.get("lessonTab", "")
            for question in unit.get("questions", []):
                if tab == "きく":
                    question.pop("noRead", None)
                else:
                    question["noRead"] = True
    return pack


def validate_recitation(pack: dict) -> None:
    tabs = {"きく": 0, "ならべる（句）": 0, "ならべる（語）": 0, "かく": 0}
    seen: set[str] = set()
    for unit in pack.get("units", []):
        tab = unit.get("lessonTab")
        for q in unit.get("questions", []):
            qid = q.get("id")
            if not qid or qid in seen:
                raise RuntimeError(f"duplicate/missing recitation question id: {qid}")
            seen.add(qid)
            if tab in tabs:
                tabs[tab] += 1
            if tab == "きく":
                if q.get("noRead"):
                    raise RuntimeError(f"listening stage must allow audio: {qid}")
                if q.get("listening") is not True:
                    raise RuntimeError(f"listening:true missing: {qid}")
            elif tab in {"ならべる（句）", "ならべる（語）", "かく"}:
                if q.get("noRead") is not True:
                    raise RuntimeError(f"noRead:true missing: {qid}")
                if tab == "かく" and not (q.get("lenient") is True and q.get("recite") is True):
                    raise RuntimeError(f"Stage 3 lenient/recite missing: {qid}")
    if tabs != {"きく": 23, "ならべる（句）": 23, "ならべる（語）": 23, "かく": 23}:
        raise RuntimeError(f"unexpected Lesson 8 ladder shape: {tabs}")


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    source = CORE.read_text(encoding="utf-8")
    packs = {p["id"]: p for p in extract_sample_packs(source)}
    missing = sorted(set(TARGETS) - set(packs))
    if missing:
        raise RuntimeError(f"required LE1 packs missing from core: {missing}")

    generated = []
    for pack_id, material_type in TARGETS.items():
        pack = enrich(packs[pack_id], material_type)
        if material_type == "recitation":
            validate_recitation(pack)
        filename = "recitation.json" if material_type == "recitation" else "practice.json"
        rel = Path("materials") / "2026" / "logical-expression-1" / "lesson08" / filename
        write_json(ROOT / rel, pack)
        generated.append({
            "id": pack_id,
            "path": rel.as_posix(),
            "schoolYear": 2026,
            "courseCode": "LE1",
            "lesson": "08",
            "materialType": material_type,
            "enabled": True,
        })

    write_json(ROOT / "materials" / "manifest.json", {
        "schema": "english-ladder-manifest@1",
        "updatedAt": "2026-09-17",
        "packs": generated,
    })
    print("Generated:", ", ".join(x["path"] for x in generated))


if __name__ == "__main__":
    main()
