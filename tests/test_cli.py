import contextlib
import io
import sys
import unittest
from unittest.mock import patch

import main
from app.core.jobpilot import JobPilot


class CLITests(unittest.TestCase):
    def test_help_command_does_not_require_runtime_dependencies(self):
        buffer = io.StringIO()

        with patch.object(sys, "argv", ["main.py", "--help"]), patch("sys.stdout", buffer):
            with self.assertRaises(SystemExit) as exc:
                main.main()

        self.assertEqual(exc.exception.code, 0)
        self.assertIn("analyze-resume", buffer.getvalue())

    def test_resume_analysis_returns_text(self):
        jobpilot = JobPilot()
        result = jobpilot.analyze_resume("data/resumes/resume.pdf")

        self.assertIsInstance(result, str)
        self.assertTrue(len(result.strip()) > 0)


if __name__ == "__main__":
    unittest.main()
