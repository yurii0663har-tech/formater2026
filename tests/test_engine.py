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


    def test_for_loop(self):

        code = """
def process(items):
 for item in items:
  print(item)
"""

        result = self.formatter.format(code)

        self.assertIn(
            "for item in items:",
            result
        )

        self.assertIn(
            "print(item)",
            result
        )


    def test_while_and_return(self):

        code = """
def process():
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
    
if __name__ == "__main__":
    unittest.main()