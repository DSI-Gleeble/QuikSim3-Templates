"""Scan examples/ and emit a manifest.json at the repo root.

Run from any directory:

    python tools/generate_manifest.py

The script expects each example to live at
``examples/<id>/`` with a ``meta.json`` describing it and a program file
referenced by ``meta.program``. It prints a short summary and writes
``manifest.json`` at the repo root.
"""

from __future__ import annotations

import datetime as _dt
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EXAMPLES_DIR = REPO / "examples"
MANIFEST = REPO / "manifest.json"

_REQUIRED_META_FIELDS = ("id", "name", "category", "description", "program", "min_quiksim3")


def _read_meta(meta_path: Path) -> dict:
    try:
        data = json.loads(meta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        sys.exit(f"error: {meta_path.relative_to(REPO)}: invalid JSON — {err}")
    missing = [f for f in _REQUIRED_META_FIELDS if f not in data]
    if missing:
        sys.exit(
            f"error: {meta_path.relative_to(REPO)}: missing fields {missing}"
        )
    return data


def _program_type(program_name: str) -> str:
    ext = Path(program_name).suffix.lower().lstrip(".")
    return {"qhd": "hds", "qst": "table", "qhz": "haz"}.get(ext, ext)


def main() -> int:
    if not EXAMPLES_DIR.is_dir():
        sys.exit(f"error: {EXAMPLES_DIR} not found")

    entries: list[dict] = []
    for meta_path in sorted(EXAMPLES_DIR.glob("*/meta.json")):
        example_dir = meta_path.parent
        meta = _read_meta(meta_path)

        expected_id = example_dir.name
        if meta["id"] != expected_id:
            sys.exit(
                f"error: {meta_path.relative_to(REPO)}: id {meta['id']!r} "
                f"does not match directory name {expected_id!r}"
            )

        program_path = example_dir / meta["program"]
        if not program_path.is_file():
            sys.exit(
                f"error: {meta_path.relative_to(REPO)}: program file "
                f"{meta['program']!r} not found"
            )

        readme_path = example_dir / "README.md"

        entry = {
            "id": meta["id"],
            "name": meta["name"],
            "category": meta["category"],
            "description": meta["description"],
            "tags": list(meta.get("tags", [])),
            "difficulty": meta.get("difficulty", "beginner"),
            "type": _program_type(meta["program"]),
            "program": str(program_path.relative_to(REPO).as_posix()),
            "readme": (
                str(readme_path.relative_to(REPO).as_posix())
                if readme_path.is_file()
                else None
            ),
            "min_quiksim3": meta["min_quiksim3"],
        }
        entries.append(entry)

    manifest = {
        "schemaVersion": 1,
        "generated_at": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "examples": entries,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {MANIFEST.relative_to(REPO)} ({len(entries)} examples)")
    for entry in entries:
        print(f"  • {entry['id']:<25} [{entry['type']}]  {entry['category']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
