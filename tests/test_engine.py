import unittest

from core.pipeline import FormatterPipeline


class TestFormatterPipeline(unittest.TestCase):

    def setUp(self):

        self.formatter = FormatterPipeline()


    def test_simple_function(self):

        code = """
def hello():
 print("Hello")
"""

        expected = """def hello():
    print('Hello')"""

        result = self.formatter.format(code)

        self.assertEqual(
            result,
            expected
        )


    def test_if_statement(self):

        code = """
def check():
 if True:
  print("OK")
"""

        expected = """def check():
    if True:
        print('OK')"""

        result = self.formatter.format(code)

        self.assertEqual(
            result,
            expected
        )


    def test_imports(self):

        code = """
import os
from pathlib import Path

def hello():
 print("Hello")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "import os",
            result
        )

        self.assertIn(
            "from pathlib import Path",
            result
        )

        self.assertIn(
            "def hello():",
            result
        )


if __name__ == "__main__":
    unittest.main()