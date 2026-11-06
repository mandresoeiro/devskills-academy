"""Validate the planned DevSkills Academy inventory using the standard library."""
import json
from collections import Counter
from datetime import date
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {"💡 Ideia", "📋 Planejada", "🚧 Em desenvolvimento", "🧪 Em testes", "✅ Concluída", "🔄 Em revisão"}
FIELDS = {"id", "name", "category", "description", "priority", "status", "difficulty", "compatible_agents", "created_at", "updated_at", "path", "tests", "documentation"}

def validate(rows):
    if not isinstance(rows, list) or len(rows) < 150:
        raise ValueError("Expected at least 150 catalog entries")
    for field in ("id", "name", "path"):
        values = [row[field].strip().casefold() for row in rows]
        if len(values) != len(set(values)):
            raise ValueError(f"Duplicate {field}")
    for row in rows:
        if set(row) != FIELDS:
            raise ValueError(f"Invalid fields: {row.get('id')}")
        if row["status"] not in STATUSES or row["priority"] not in {"P1", "P2", "P3"}:
            raise ValueError(f"Invalid status or priority: {row['id']}")
        if not isinstance(row["compatible_agents"], list):
            raise ValueError("compatible_agents must be a list")
        for field in FIELDS - {"compatible_agents"}:
            if not isinstance(row[field], str) or not row[field].strip():
                raise ValueError(f"Missing text: {row['id']} / {field}")
        created = date.fromisoformat(row["created_at"])
        updated = date.fromisoformat(row["updated_at"])
        if updated < created:
            raise ValueError("Update date precedes creation")
        path = PurePosixPath(row["path"])
        if path.is_absolute() or ".." in path.parts or "\\" in row["path"] or ":" in row["path"] or path.parts[0] != "skills" or path.name != "SKILL.md":
            raise ValueError(f"Unsafe or invalid path: {path}")
        if row["status"] == "✅ Concluída" and not (ROOT / row["path"]).is_file():
            raise ValueError(f"Completed skill file missing: {path}")
    return Counter(row["status"] for row in rows)

if __name__ == "__main__":
    rows = json.loads((ROOT / "catalog" / "skills.json").read_text(encoding="utf-8"))
    statuses = validate(rows)
    catalog_view = (ROOT / "catalog" / "README.md").read_text(encoding="utf-8")
    for row in rows:
        expected = f"| {row['id']} | {row['name']} | {row['category']} | {row['priority']} | {row['status']} |"
        if expected not in catalog_view:
            raise ValueError(f"Markdown catalog differs: {row['id']}")
    print(f"Validated {len(rows)} skills across {len({r['category'] for r in rows})} categories.")
    for status, count in statuses.items():
        print(f"{status.encode('ascii', errors='ignore').decode().strip()}: {count}")

