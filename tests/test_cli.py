import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CLITests(unittest.TestCase):

    def test_cli_formats_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "demo.py"
            path.write_text("x=1\nprint(x)\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, "cli.py", str(path)],
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0)
            self.assertIn("x = 1", result.stdout)
            self.assertIn("print(x)", result.stdout)

    def test_cli_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "demo.py"
            path.write_text("x=1\nprint(x)\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, "cli.py", str(path), "--write"],
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0)

            content = path.read_text(encoding="utf-8")

            self.assertIn("x = 1", content)
            self.assertIn("print(x)", content)

    def test_cli_missing_file(self):
        result = subprocess.run(
            [sys.executable, "cli.py", "missing_file.py"],
            capture_output=True,
            text=True,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("File not found", result.stderr)

    def test_cli_syntax_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "broken.py"
            path.write_text("def foo(\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, "cli.py", str(path)],
                capture_output=True,
                text=True,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Syntax error", result.stderr)


if __name__ == "__main__":
    unittest.main()