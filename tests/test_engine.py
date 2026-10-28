import unittest

from engine import ForwardChainingEngine
from kb_loader import load_rules


class LaptopRuleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = load_rules("kb/laptop_rules.json")

    # Test documented test cases
    def test_documented_scenarios(self):
        cases = [
            (
                ["budget_high", "portable", "long_battery"],
                ["premium_ultrabook"],
                [],
                ["Premium Ultrabook"],
            ),
            (
                ["budget_low", "portable", "office_only"],
                ["budget_ultrabook"],
                [],
                ["Budget Ultrabook"],
            ),
            (
                ["budget_medium", "gaming"],
                ["midrange_gaming_laptop"],
                [],
                ["Gaming"],
            ),
            (
                ["budget_high", "gaming"],
                ["high_end_gaming_laptop"],
                [],
                ["Pro Gaming"],
            ),
            (
                ["creative_work", "portable"],
                [],
                ["ram_16_plus"],
                ["Creative Portable"],
            ),
            (
                ["creative_work", "large_screen"],
                [],
                ["display_15_plus_color_accurate"],
                ["Creative Display"],
            ),
            (
                ["travel_often", "long_battery"],
                [],
                ["battery_60wh_plus"],
                ["Travel + Battery"],
            ),
            (
                ["pref_os_macos"],
                [],
                ["macos_required"],
                ["OS Preference Mapping"],
            ),
            (
                ["needs_ai_accel"],
                [],
                ["gpu_with_tensor_cores"],
                ["AI Acceleration"],
            ),
            (
                ["pref_os_linux", "office_only"],
                [],
                ["linux_friendly_hw"],
                ["Linux Suitability"],
            ),
            (
                [
                    "creative_work",
                    "portable",
                    "large_screen",
                    "travel_often",
                    "long_battery",
                ],
                [],
                [
                    "ram_16_plus",
                    "display_15_plus_color_accurate",
                    "battery_60wh_plus",
                ],
                ["Creative Portable", "Creative Display", "Travel + Battery"],
            ),
            (["portable"], [], [], []),
        ]

        for facts, recommendations, specs, fired_rules in cases:
            with self.subTest(facts=facts):
                engine = ForwardChainingEngine(self.rules)
                engine.assert_facts(facts)
                engine.run()
                results = engine.conclusions()

                self.assertCountEqual(results["recommendations"], recommendations)
                self.assertCountEqual(results["specs"], specs)
                self.assertEqual([entry["rule"] for entry in engine.trace], fired_rules)


if __name__ == "__main__":
    unittest.main()
