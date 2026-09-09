import ast
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "main.py").read_text(encoding="utf-8")


class SubmissionReadinessTests(unittest.TestCase):
    def test_main_is_valid_python(self):
        ast.parse(SOURCE)

    def test_fall_tournament_is_explicit(self):
        self.assertIn('"fall-futureeval-2026"', SOURCE)
        self.assertIn("/tournament/fall-futureeval-2026/", SOURCE)
        self.assertNotIn('"summer-futureeval-2026"', SOURCE)

    def test_evidence_strategy_is_active(self):
        for marker in (
            "class EvidenceEdgeBot",
            "Metaculus questions",
            "Seek disconfirming evidence",
            "_evidence_edge_protocol()",
            'predictions_per_research_report=3',
            '"openrouter/openai/gpt-5.4"',
            '"openrouter/openai/gpt-5.4:online"',
        ):
            self.assertIn(marker, SOURCE)

    def test_overconfidence_cap_is_active(self):
        self.assertIn("max(0.03, min(0.97", SOURCE)

    def test_live_forecasts_are_not_human_reviewed(self):
        self.assertIn("skip_previously_forecasted_questions=True", SOURCE)
        self.assertIn("publish_to_metaculus = True", SOURCE)


if __name__ == "__main__":
    unittest.main()
