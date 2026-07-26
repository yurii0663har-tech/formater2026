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
        
    def test_lambda_expression(self):

        code = """
square = lambda x: x * x
"""

        result = self.formatter.format(code)

        self.assertIn(
            "lambda x: x * x",
            result
        )
        
    def test_list_comprehension(self):

        code = """
numbers = [x for x in items]
"""

        result = self.formatter.format(code)

        self.assertIn(
            "[x for x in items]",
            result
        )
        
     
        
    def test_dict_comprehension(self):

        code = """
squares = {x: x*x for x in numbers}
"""

        result = self.formatter.format(code)

        self.assertIn(
            "{x: x * x for x in numbers}",
            result
        )

    def test_set_comprehension(self):

        code = """
values = {x for x in numbers}
"""

        result = self.formatter.format(code)

        self.assertIn(
            "{x for x in numbers}",
            result
        )


    def test_set_comprehension(self):

        code = """
values = {x for x in numbers}
"""

        result = self.formatter.format(code)

        self.assertIn(
            "{x for x in numbers}",
            result
        )


    def test_match_statement(self):

        code = """
def check(value):
 match value:
  case 1:
   print("one")
  case _:
   print("other")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "match value:",
            result
        )

        self.assertIn(
            "case 1:",
            result
        )

        self.assertIn(
            "case _:",
            result
        )

      

        result = self.formatter.format(code)

        self.assertIn(
            "{x for x in numbers}",
            result
        )


    


    def test_match_statement(self):

        code = """
def check(value):
 match value:
  case 1:
   print("one")
  case _:
   print("other")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "match value:",
            result
        )

        self.assertIn(
            "case 1:",
            result
        )

        self.assertIn(
            "case _:",
            result
        )


    def test_raise_statement(self):

        code = """
def fail():
 raise ValueError("error")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "raise ValueError('error')",
            result
        )
        
    def test_yield_statement(self):

        code = """
def numbers():
 yield 1
"""

        result = self.formatter.format(code)

        self.assertIn(
            "yield 1",
            result
        )
        
    def test_break_statement(self):

        code = """
def process():
 while True:
  break
"""

        result = self.formatter.format(code)

        self.assertIn(
            "break",
            result
        )


    def test_continue_statement(self):

        code = """
def process():
 while True:
  continue
"""

        result = self.formatter.format(code)

        self.assertIn(
            "continue",
            result
        )
        
    def test_assert_statement(self):

        code = """
def check(value):
 assert value > 0
"""

        result = self.formatter.format(code)

        self.assertIn(
            "assert value > 0",
            result
        )
        
        
    def test_global_statement(self):

        code = """
value = 0

def update():
 global value
 value = 10
"""

        result = self.formatter.format(code)

        self.assertIn(
            "global value",
            result
        )





    def test_async_with_statement(self):

        code = """
async def load():
 async with resource:
  print("ok")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "async with resource:",
            result
        )
        

    def test_async_for_statement(self):

        code = """
async def process(items):
 async for item in items:
  print(item)
"""

        result = self.formatter.format(code)

        self.assertIn(
            "async for item in items:",
            result
        )
        
    def test_type_annotations(self):

        code = """
def add(a: int, b: int) -> int:
 return a + b
"""

        result = self.formatter.format(code)

        self.assertIn(
            "def add(a: int, b: int) -> int:",
            result
        )

        self.assertIn(
            "return a + b",
            result
        )
    
    def test_variable_annotations(self):

        code = """
age: int = 30

class User:
 name: str
"""

        result = self.formatter.format(code)

        self.assertIn(
            "age: int = 30",
            result
        )

        self.assertIn(
            "name: str",
            result
        )
        
    def test_function_call_expression(self):

        code = """
def run():
 print("hello")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "print('hello')",
            result
        )
        
    def test_attribute_expression(self):

        code = """
def show(user):
 print(user.name)
"""

        result = self.formatter.format(code)

        self.assertIn(
            "user.name",
        result
        )
    def test_binary_expression(self):

        code = """
def calc(a, b, c):
 x = a + b * c
"""

        result = self.formatter.format(code)

        self.assertIn(
            "a + b * c",
            result
        )
        
    def test_boolean_expression(self):

        code = """
def check(a, b, c):
 if a and b or c:
  print("yes")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "a and b or c",
            result
        )
        
    def test_compare_expression(self):

        code = """
def check(x, y):
 if x > 10 and y != 0:
  return True
"""

        result = self.formatter.format(code)

        self.assertIn(
            "x > 10 and y != 0",
            result
        )
        
    def test_unary_expression(self):

        code = """
def check(value):
 if not value:
  return -value
"""

        result = self.formatter.format(code)

        self.assertIn(
            "not value",
            result
        )

        self.assertIn(
            "-value",
            result
        )
        
    def test_if_expression(self):

        code = """
def choose(flag):
 result = "yes" if flag else "no"
 return result
"""

        result = self.formatter.format(code)

        self.assertIn(
    "yes",
        result
)

        self.assertIn(
    "if flag else",
        result
)

        self.assertIn(
    "no",
    result
)
      
    def test_subscript_expression(self):

        code = """
def get(items, user):
 value = items[0]
 name = user["name"]
 return value, name
"""

        result = self.formatter.format(code)

        self.assertIn(
            "items[0]",
            result
        )

        self.assertIn(
            "user['name']",
            result
        )
    
    def test_subscript_expression(self):

        code = """
def get(items, user):
 value = items[0]
 name = user["name"]
 return value, name
"""

        result = self.formatter.format(code)

        self.assertIn(
            "items[0]",
            result
        )

        self.assertIn(
            "user['name']",
            result
        )
        
    def test_slice_expression(self):

        code = """
def get(items):
 first = items[1:5]
 second = items[:10]
 third = items[::2]
 return first, second, third
"""

        result = self.formatter.format(code)

        self.assertIn(
            "items[1:5]",
            result
        )

        self.assertIn(
            "items[:10]",
            result
        )

        self.assertIn(
            "items[::2]",
            result
        )  
        
    def test_collection_literals(self):

        code = """
def create():
 values = [1, 2, 3]
 point = (10, 20)
 config = {"debug": True}
 tags = {"python", "ast"}
 return values, point, config, tags
"""

        result = self.formatter.format(code)

        self.assertIn(
            "[1, 2, 3]",
            result
        )

        self.assertIn(
            "(10, 20)",
            result
        )

        self.assertIn(
            "{'debug': True}",
            result
        )

        self.assertIn(
            "{'python', 'ast'}",
            result
        )
 
    def test_collection_literals(self):

        code = """
def create():
 values = [1, 2, 3]
 point = (10, 20)
 config = {"debug": True}
 tags = {"python", "ast"}
 return values, point, config, tags
"""

        result = self.formatter.format(code)

        self.assertIn(
            "[1, 2, 3]",
            result
        )

        self.assertIn(
            "(10, 20)",
            result
        )

        self.assertIn(
            "{'debug': True}",
            result
        )

        self.assertIn(
            "{'python', 'ast'}",
            result
        )
        
    def test_f_string_expression(self):

        code = """
def greet(name):
 message = f"Hello {name}"
 return message
"""

        result = self.formatter.format(code)

        self.assertIn(
            "f'Hello {name}'",
            result
        )
if __name__ == "__main__":
    unittest.main()



    