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

        self.assertEqual(result, expected)

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

        self.assertEqual(result, expected)

    def test_imports(self):

        code = """
import os
from pathlib import Path

def hello():
 print("Hello")
"""

        result = self.formatter.format(code)

        self.assertIn("import os", result)
        self.assertIn("from pathlib import Path", result)
        self.assertIn("def hello():", result)

    def test_for_loop(self):

        code = """
def process(items):
 for item in items:
  print(item)
"""

        result = self.formatter.format(code)

        self.assertIn("for item in items:", result)
        self.assertIn("print(item)", result)

    def test_while_and_return(self):

        code = """
def process():
 while True:
  return 1
"""

        result = self.formatter.format(code)

        self.assertIn("while True:", result)
        self.assertIn("return 1", result)

    def test_try_except(self):

        code = """
def load():
 try:
  print("start")
 except Exception:
  print("error")
"""

        result = self.formatter.format(code)

        self.assertIn("try:", result)
        self.assertIn("except Exception:", result)
        self.assertIn("print('error')", result)



    
    def test_with_statement(self):

        code = """
def read_file():
 with open("test.txt") as file:
  print(file.read())
"""

        result = self.formatter.format(code)

        self.assertIn(
            "with open('test.txt') as file:",
            result
        )

        self.assertIn(
            "print(file.read())",
            result
        )
        

    
    def test_class_statement(self):

        code = """
class User:
 def hello(self):
  print("Hi")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "class User:",
            result
        )

        self.assertIn(
            "def hello(self):",
            result
        )

        self.assertIn(
            "print('Hi')",
            result
        )
    def test_class_constructor(self):

        code = """
class User:
 def __init__(self,name):
  self.name=name
"""

        result = self.formatter.format(code)

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
    def test_class_inheritance(self):

        code = """
class User:
 pass

class Admin(User):
 pass
"""

        result = self.formatter.format(code)

        self.assertIn(
            "class User:",
            result
        )

        self.assertIn(
            "class Admin(User):",
            result
        )

        self.assertIn(
            "pass",
            result
            
    
        )
        
    def test_decorator_statement(self):

        code = """
class User:
    @staticmethod
    def hello():
        print("Hi")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "@staticmethod",
            result
            )

        self.assertIn(
            "def hello():",
            result
        )

        self.assertIn(
            "print('Hi')",
            result
        )
        
    def test_decorator_statement(self):

        code = """
class User:
    @staticmethod
    def hello():
        print("Hi")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "@staticmethod",
            result
        )

        self.assertIn(
            "def hello():",
            result
        )

        self.assertIn(
            "print('Hi')",
            result
        )
        
    def test_multiple_decorators(self):

        code = """
@staticmethod
@cache
def hello():
 print("Hi")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "@staticmethod",
            result
        )

        self.assertIn(
            "@cache",
            result
        )

        self.assertIn(
            "def hello():",
            result
        )
        
    def test_async_function(self):

        code = """
async def fetch():
 await request()
"""

        result = self.formatter.format(code)

        self.assertIn(
            "async def fetch():",
            result
        )

        self.assertIn(
            "await request()",
            result
        )
if __name__ == "__main__":
    unittest.main()