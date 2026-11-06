import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_catalog import validate


class CatalogValidationTests(unittest.TestCase):
    def setUp(self):
        self.rows = json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))

    def test_rejects_duplicate_names(self):
        self.rows[1]['name'] = self.rows[0]['name']
        with self.assertRaises(ValueError):
            validate(self.rows)

    def test_rejects_paths_outside_skills(self):
        self.rows[0]['path'] = 'skills/../bad/SKILL.md'
        with self.assertRaises(ValueError):
            validate(self.rows)

    def test_rejects_unknown_status(self):
        self.rows[0]['status'] = 'done'
        with self.assertRaises(ValueError):
            validate(self.rows)

    def test_rejects_completion_without_implementation(self):
        self.rows[0]['status'] = '\u2705 Concluída'
        with self.assertRaises(ValueError):
            validate(self.rows)

