import unittest

from core.pipeline import FormatterPipeline


class TestFormatterPipeline(unittest.TestCase):

    def setUp(self):
        self.formatter = FormatterPipeline()

    def test_simple_function(self):
        code = """
def hello(name):
 print("Hello",name)
"""

        result = self.formatter.format(code)

        self.assertIn(
            "def hello(name):",
            result
        )

        self.assertIn(
            "print('Hello', name)",
            result
        )

    def test_if_statement(self):
        code = """
if x>10:
 print("big")
else:
 print("small")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "if x > 10:",
            result
        )

        self.assertIn(
            "else:",
            result
        )

    def test_for_loop(self):
        code = """
for i in range(5):
 print(i)
"""

        result = self.formatter.format(code)

        self.assertIn(
            "for i in range(5):",
            result
        )

        self.assertIn(
            "print(i)",
            result
        )

    def test_while_and_return(self):
        code = """
def count():
 while True:
  return 1
"""

        result = self.formatter.format(code)

        self.assertIn(
            "while True:",
            result
        )

        self.assertIn(
            "return 1",
            result
        )

    def test_imports(self):
        code = """
import os
import sys
"""

        result = self.formatter.format(code)

        self.assertIn(
            "import os",
            result
        )

        self.assertIn(
            "import sys",
            result
        )

    def test_try_except(self):

        code = """
def load():
 try:
  print("start")
 except Exception:
  print("error")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "try:",
            result
        )

        self.assertIn(
            "except Exception:",
            result
        )

        self.assertIn(
            "print('error')",
            result
        )

    def test_with_statement(self):

        source = '''
with open("file.txt") as f:
    print(f.read())
'''

        result = self.formatter.format(source)

        self.assertIn(
            "with open('file.txt') as f:",
            result
        )

    def test_class_statement(self):

        source = '''
class User:
 def __init__(self,name):
  self.name=name
'''

        result = self.formatter.format(source)

        self.assertIn(
            "class User:",
            result
        )

        self.assertIn(
            "def __init__(self, name):",
            result
        )

        self.assertIn(
            "self.name = name",
            result
        )


if __name__ == "__main__":
    unittest.main()