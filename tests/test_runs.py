#!/usr/bin/env python3
"""Automated Regression & Validation Test Suite for Angle Ideation Agent."""

from __future__ import annotations

import glob
import json
import os
import sys
import unittest
from pathlib import Path

# Add repo root to sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

try:
    import jsonschema
except ImportError:
    jsonschema = None

from scripts.validate_run import validate_run
from scripts.export_angle_pack_json import parse_markdown_pack


class TestAngleIdeationAgent(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_root = REPO_ROOT
        self.schemas_dir = self.repo_root / "schemas"
        self.runs_dir = self.repo_root / "runs"

    @unittest.skipIf(jsonschema is None, "jsonschema library not installed in environment")
    def test_schemas_are_valid_draft202012(self) -> None:
        """All schemas in schemas/*.schema.json must be valid Draft 2020-12 schemas."""
        schema_files = list(self.schemas_dir.glob("*.schema.json"))
        self.assertGreater(len(schema_files), 0, "No schema files found in schemas/")
        for sf in schema_files:
            with open(sf, "r", encoding="utf-8") as f:
                data = json.load(f)
            # This raises SchemaError if invalid
            jsonschema.Draft202012Validator.check_schema(data)

    def test_no_utf8_bom_in_repo(self) -> None:
        """No json, md, py, or schema file in the repository should contain a UTF-8 BOM."""
        for root, dirs, files in os.walk(self.repo_root):
            if ".git" in root or "__pycache__" in root:
                continue
            for fname in files:
                if fname.endswith((".json", ".md", ".py", ".toml")):
                    fpath = Path(root) / fname
                    with open(fpath, "rb") as fp:
                        prefix = fp.read(3)
                        self.assertNotEqual(
                            prefix,
                            b"\xef\xbb\xbf",
                            f"UTF-8 BOM found in file: {fpath.relative_to(self.repo_root)}",
                        )

    def test_benchmark_run_passes(self) -> None:
        """runs/20260814-bb-benchmark must pass all artifact, schema, headline, and triad checks."""
        run_dir = self.runs_dir / "20260814-bb-benchmark"
        self.assertTrue(run_dir.is_dir(), "20260814-bb-benchmark run directory not found")
        success, errors = validate_run(
            run_dir=run_dir,
            repo_root=self.repo_root,
            product_name="Baby Bubble",
            verbose=False,
        )
        self.assertTrue(success, f"Benchmark run failed validation: {errors}")

    def test_strideform_transfer_run_passes(self) -> None:
        """runs/20260814-strideform-l3 must pass all artifact, schema, headline, and triad checks."""
        run_dir = self.runs_dir / "20260814-strideform-l3"
        self.assertTrue(run_dir.is_dir(), "20260814-strideform-l3 run directory not found")
        success, errors = validate_run(
            run_dir=run_dir,
            repo_root=self.repo_root,
            product_name="StrideForm",
            verbose=False,
        )
        self.assertTrue(success, f"StrideForm run failed validation: {errors}")

    def test_negative_control_fails_expected_checks(self) -> None:
        """runs/20260814-negcontrol-feature must fail validation (false-positive defense)."""
        run_dir = self.runs_dir / "20260814-negcontrol-feature"
        self.assertTrue(run_dir.is_dir(), "20260814-negcontrol-feature run directory not found")
        success, errors = validate_run(
            run_dir=run_dir,
            repo_root=self.repo_root,
            product_name="AirPurge",
            verbose=False,
        )
        self.assertFalse(success, "Negative control run should have failed validation!")
        # Ensure errors cite expected failures
        error_text = " ".join(errors)
        self.assertIn("H5", error_text, "Negative control should flag H5 preamble failures")
        self.assertIn("H6", error_text, "Negative control should flag H6 ad-ese failures")

    def test_export_angle_pack_json_conformance(self) -> None:
        """parse_markdown_pack must produce valid JSON adhering to angle_pack.schema.json."""
        pack_path = self.runs_dir / "20260814-bb-benchmark" / "05_angle_pack.md"
        text = pack_path.read_text(encoding="utf-8")
        data = parse_markdown_pack(text)

        schema_path = self.schemas_dir / "angle_pack.schema.json"
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)

        if jsonschema is not None:
            jsonschema.validate(instance=data, schema=schema)
        self.assertEqual(data["pack"]["product_name"], "Baby Bubble")
        self.assertEqual(len(data["pack"]["angles"]), 8)
        self.assertEqual(data["pack"]["status"], "Ready for Pre-Lander Agent")


if __name__ == "__main__":
    unittest.main()
