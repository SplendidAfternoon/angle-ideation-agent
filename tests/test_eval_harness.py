#!/usr/bin/env python3
"""Eval harness must match expected labels, including stub-triad FAIL."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

try:
    import jsonschema
except ImportError:
    jsonschema = None

from eval.harness import ops_flags, run_harness, vsl_flags


class TestEvalHarness(unittest.TestCase):
    @unittest.skipIf(jsonschema is None, "jsonschema library not installed in environment")
    def test_manifest_matches_schema(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / "eval/cases/manifest.json").read_text(encoding="utf-8")
        )
        schema = json.loads(
            (REPO_ROOT / "schemas/eval_case.schema.json").read_text(encoding="utf-8")
        )
        jsonschema.validate(instance=manifest, schema=schema)

    @unittest.skipIf(jsonschema is None, "jsonschema library not installed in environment")
    def test_llm_trace_schema_validates_example(self) -> None:
        schema = json.loads(
            (REPO_ROOT / "schemas/llm_trace.schema.json").read_text(encoding="utf-8")
        )
        example = {
            "run_id": "x",
            "methodology": "angle-ideation-agent@1.7.0",
            "collapsed_roles": False,
            "ready_stamped_by": "not_ready",
            "calls": [
                {
                    "role": "critic",
                    "stage": "chain_judge",
                    "ended_ok": True,
                }
            ],
        }
        jsonschema.validate(instance=example, schema=schema)

    def test_collapsed_fixture_raises_ops_flags(self) -> None:
        flags = ops_flags(REPO_ROOT / "eval/fixtures/collapsed-triad")
        for needed in ("OPS-STUB-GATES", "OPS-STUB-GOLD", "OPS-STUB-ADVERSARY"):
            self.assertIn(needed, flags, f"missing {needed} in {flags}")

    def test_vsl_doctrine_fixture_raises_f16_f18(self) -> None:
        flags = vsl_flags(REPO_ROOT / "eval/fixtures/vsl-doctrine-fail")
        for needed in ("F16-ARRIVAL", "F17-MECH-ACTION", "F18-HOOK-CLUSTER"):
            self.assertIn(needed, flags, f"missing {needed} in {flags}")

    def test_bb_benchmark_does_not_trip_vsl_doctrine_flags(self) -> None:
        flags = vsl_flags(REPO_ROOT / "runs/20260814-bb-benchmark")
        self.assertEqual(flags, [], f"benchmark pack should pass F16–F18 lexical hunts: {flags}")

    def test_catalog_f16_f18_exist_in_docs_04(self) -> None:
        text = (REPO_ROOT / "docs/04-quality-gates.md").read_text(encoding="utf-8")
        for catalog_id in ("F16", "F17", "F18"):
            self.assertRegex(
                text,
                rf"\| {catalog_id} \|",
                f"{catalog_id} missing from docs/04 §9",
            )

    def test_harness_all_cases_match_labels(self) -> None:
        ok, results = run_harness()
        self.assertTrue(
            ok,
            "harness mismatch: "
            + json.dumps([r for r in results if not r["matched"]], indent=2),
        )


if __name__ == "__main__":
    unittest.main()
