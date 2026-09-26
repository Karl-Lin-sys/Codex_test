import datetime as dt
import unittest

from daily_prompt import PROMPTS, prompt_for_date


class DailyPromptTests(unittest.TestCase):
    def test_prompt_is_reproducible_for_a_date(self):
        day = dt.date(2026, 9, 26)
        self.assertEqual(prompt_for_date(day), prompt_for_date(day))

    def test_prompt_is_from_catalog(self):
        self.assertIn(prompt_for_date(dt.date(2026, 1, 1)), PROMPTS)


if __name__ == "__main__":
    unittest.main()
