import unittest

import ast


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

    def test_multiple_except(self):

        code = """
def handle():
    try:
        work()
    except ValueError:
        handle_value()
    except Exception:
        handle_other()
"""

        result = self.formatter.format(code)

        self.assertIn(
            "except ValueError:",
            result
        )

        self.assertIn(
            "except Exception:",
            result
        )

    def test_try_except_else(self):

        code = """
def check():
    try:
        value = 1
    except Exception:
        handle()
    else:
        success()
"""

        result = self.formatter.format(code)

        self.assertIn(
            "else:",
            result
        )
    def test_except_star_with_name(self):

        code = """
def handle():
    try:
        risky()
    except* ValueError as e:
        print(e)
"""

        result = self.formatter.format(code)

        self.assertIn(
        "except* ValueError as e:",
            result
    )
    
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
    def test_async_with_without_as_statement(self):

        code = """
async def read():
    async with open_async("file.txt"):
        process()
"""

        result = self.formatter.format(code)

        self.assertIn(
            "async with open_async('file.txt'):",
            result
        )  
        
    def test_multiple_async_with_statement(self):

        code = """
async def load():
    async with open_async("a.txt") as a, open_async("b.txt") as b:
        data = await a.read()
"""

        result = self.formatter.format(code)

        self.assertIn(
            "async with open_async('a.txt') as a, open_async('b.txt') as b:",
            result
        )
        
    def test_with_without_as_statement(self):

        code = """
def read():
    with open("file.txt"):
        process()
"""

        result = self.formatter.format(code)

        self.assertIn(
            "with open('file.txt'):",
            result
        ) 
     
        
    def test_multiple_with_statement(self):

        code = """
def copy():
    with open("a.txt") as a, open("b.txt") as b:
        data = a.read()
"""

        result = self.formatter.format(code)

        self.assertIn(
            "with open('a.txt') as a, open('b.txt') as b:",
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


    def test_complex_match_patterns(self):

        code = """
def parse(value):
 match value:
    case [a, b]:
        return a + b
    case {"name": name}:
        return name
"""

        result = self.formatter.format(code)

        self.assertIn(
            "case [a, b]:",
            result
        )

        self.assertIn(
            "{'name': name}",
            result
        )
    
    def test_match_or_pattern(self):

        code = """
def check(value):
 match value:
  case 1 | 2:
   return "small"
  case _:
   return "other"
"""

        result = self.formatter.format(code)

        self.assertIn(
            "case 1 | 2:",
            result
        )
    def test_match_as_pattern(self):

        code = """
def parse(value):
 match value:
  case [x, y] as pair:
   return pair
"""

        result = self.formatter.format(code)

        self.assertIn(
            "case [x, y] as pair:",
            result
        )
    
    def test_match_class_pattern(self):

        code = """
def parse(value):
 match value:
  case Point(x, y):
   return x + y
"""

        result = self.formatter.format(code)

        self.assertIn(
            "case Point(x, y):",
            result
        )
        
    def test_match_guard_pattern(self):

        code = """
def check(value):
 match value:
  case x if x > 0:
   return "positive"
  case _:
   return "other"
"""

        result = self.formatter.format(code)

        self.assertIn(
            "case x if x > 0:",
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
       
    def test_raise_from_statement(self):

        code = """
def fail():
    try:
        work()
    except Exception as e:
        raise RuntimeError("failed") from e
"""

        result = self.formatter.format(code)

        self.assertIn(
            "raise RuntimeError('failed') from e",
            result
        )

    def test_await_expression(self):

        code = """
async def load():
 result = await fetch()
 return result
"""

        result = self.formatter.format(code)

        self.assertIn(
            "await fetch()",
            result
        )    

        code = """
def fail():
    try:
        work()
    except Exception as e:
        raise RuntimeError("failed") from e
"""

        result = self.formatter.format(code)
  
        self.assertIn(
        "raise RuntimeError('failed') from e",
            result
    ) 
    def test_await_expression(self):

        code = """
async def load():
 result = await fetch()
 return result
"""

        result = self.formatter.format(code)

        self.assertIn(
            "await fetch()",
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
    def test_yield_from_statement(self):

        code = """
def generator(items):
 yield from items
"""

        result = self.formatter.format(code)

        self.assertIn(
            "yield from items",
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

    def test_nonlocal_statement(self):

        code = """
def outer():
    value = 1

    def inner():
        nonlocal value
        value = 2
"""

        result = self.formatter.format(code)

        self.assertIn(
        "nonlocal value",
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
    def test_ast_equivalence(self):
        
        self.maxDiff = None
        
        code = """
def add(a: int, b: int) -> int:
    if a > b:
        return a
    return b
"""

        
        
        formatted = self.formatter.format(code)

      

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )
    
        

      

    
    
        self.assertEqual(
            original_ast,
            formatted_ast
        )
        
    def test_typevar_statement(self):

        code = """
from typing import TypeVar

T = TypeVar("T")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "T = TypeVar('T')",
            result
        ) 
        
    def test_paramspec_statement(self):

        code = """
from typing import ParamSpec

P = ParamSpec("P")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "P = ParamSpec('P')",
            result
        )  
    def test_typevartuple_statement(self):

        code = """
from typing import TypeVarTuple

Ts = TypeVarTuple("Ts")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "Ts = TypeVarTuple('Ts')",
            result
        )
    def test_annotated_type_annotation(self):

        code = """
from typing import Annotated

def user_id(value: Annotated[int, "positive"]) -> int:
    return value
"""

        result = self.formatter.format(code)

        self.assertIn(
    "value: Annotated[int, 'positive']",
        result
)

        self.assertIn(
            "-> int:",
            result
        ) 
        
    def test_literal_type_annotation(self):

        code = """
from typing import Literal

def status(value: Literal["ok", "error"]) -> str:
    return value
"""

        result = self.formatter.format(code)

        self.assertIn(
            "value: Literal['ok', 'error']",
            result
        )

        self.assertIn(
            "-> str:",
            result
        )     
    def test_callable_type_annotation(self):

        code = """
from collections.abc import Callable

def execute(callback: Callable[[int, str], bool]) -> bool:
    return callback(1, "test")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "callback: Callable[[int, str], bool]",
            result
        )

        self.assertIn(
            "-> bool:",
            result
        )
    
    def test_type_alias_statement(self):

        code = """
type UserId = int
"""

        result = self.formatter.format(code)

        self.assertIn(
            "type UserId = int",
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
    
    def test_named_expression(self):

        code = """
def check(items):
 if (n := len(items)) > 0:
  return n
 return 0
"""

        result = self.formatter.format(code)

        self.assertIn(
            "n := len(items)",
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
        
    def test_complex_f_string_expression(self):

        code = """
def info(user, count):
 message = f"{user.name}: {count + 1}"
 return message
"""

        result = self.formatter.format(code)

        self.assertIn(
            "user.name",
            result
        )

        self.assertIn(
            "count + 1",
            result
        )
        
    def test_starred_expression(self):

        code = """
def expand(items):
 result = [*items]
 return result
"""

        result = self.formatter.format(code)

        self.assertIn(
            "*items",
            result
        )
        
    def test_dict_unpack_expression(self):

        code = """
def merge(first, second):
 result = {**first, **second}
 return result
"""

        result = self.formatter.format(code)

        self.assertIn(
            "**first",
            result
        )

        self.assertIn(
            "**second",
            result
        )
        
    def test_function_call_unpack_expression(self):

        code = """
def run(args, options):
 result = func(*args, **options)
 return result
"""

        result = self.formatter.format(code)

        self.assertIn(
            "*args",
            result
        )

        self.assertIn(
            "**options",
            result
        )
        
   
        
    def test_del_statement(self):

        code = """
def remove(items):
 del items[0]
"""

        result = self.formatter.format(code)

        self.assertIn(
        "del items[0]",
            result
        ) 
        
    def test_assert_with_message(self):

        code = """
def check(value):
 assert value, "invalid value"
"""

        result = self.formatter.format(code)

        self.assertIn(
        "assert value, 'invalid value'",
            result
        )  
        
    def test_except_star_statement(self):

        code = """
def handle():
 try:
  risky()
 except* ValueError:
  pass
"""

        result = self.formatter.format(code)

        self.assertIn(
        "except* ValueError:",
            result
        ) 
        
    def test_union_type_annotation(self):

        code = """
def parse(value: int | str) -> int | None:
    return None
"""

        result = self.formatter.format(code)

        self.assertIn(
        "def parse(value: int | str) -> int | None:",
            result
    )
      
    def test_generic_type_annotations(self):

        code = """
def process(items: list[int], mapping: dict[str, int]) -> tuple[int, ...]:
    return (1,)
"""

        result = self.formatter.format(code)

        self.assertIn(
        "items: list[int]",
            result
    )

        self.assertIn(
        "mapping: dict[str, int]",
            result
    )

        self.assertIn(
        "-> tuple[int, ...]",
            result
    )    



        code = """
from typing import ParamSpec

P = ParamSpec("P")
"""

        result = self.formatter.format(code)

        self.assertIn(
        "P = ParamSpec('P')",
            result
    )   
   
    def test_typevartuple_statement(self):

        code = """
from typing import TypeVarTuple

Ts = TypeVarTuple("Ts")
"""

        result = self.formatter.format(code)

        self.assertIn(
            "Ts = TypeVarTuple('Ts')",
            result
        )
    def test_nested_if_for_ast_equivalence(self):

        code = """
def process(items):
    for item in items:
        if item:
            return item
    return None
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )
    def test_if_elif_else_ast_equivalence(self):

        code = """
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    else:
        return "C"
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )
        
    def find(items):
        for item in items:
            if item:
                return item
        else:
            return None 
    def test_for_else_ast_equivalence(self):

        code = """
def find(items):
    for item in items:
        if item:
            return item
    else:
        return None
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )  
    
    def test_while_else_ast_equivalence(self):

        code = """
def search(items):
    while items:
        item = items.pop()
        if item:
            break
    else:
        return None
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )
        
    def test_try_except_else_finally_ast_equivalence(self):

        code = """
def load():
    try:
        value = read()
    except Exception:
        return None
    else:
        return value
    finally:
        cleanup()
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        ) 
        
    def test_with_statement_ast_equivalence(self):

        code = """
def read_file():
    with open("data.txt") as f:
        return f.read()
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )  
        
    def test_multiple_with_statement_ast_equivalence(self):

        code = """
def copy_files():
    with open("a.txt") as a, open("b.txt") as b:
        return a.read()
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )
        
    def test_async_function_ast_equivalence(self):

        code = """
async def fetch():
    return await get_data()
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )  
        
    def test_async_for_ast_equivalence(self):

        code = """
async def process(items):
    async for item in items:
        return item
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )
        
    def test_async_with_ast_equivalence(self):

        code = """
async def load():
    async with session.get("/") as response:
        return await response.text()
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )
    def test_async_with_ast_equivalence(self):

        code = """
async def load():
    async with session.get("/") as response:
        return await response.text()
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )    
        
    def test_match_case_ast_equivalence(self):

        code = """
def classify(value):
    match value:
        case 0:
            return "zero"
        case 1:
            return "one"
        case _:
            return "other"
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        ) 
        
    def test_list_comprehension_ast_equivalence(self):

        code = """
def squares(items):
    return [x * x for x in items]
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
        ast.parse(code),
        include_attributes=False
    )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        ) 
    def test_set_comprehension_ast_equivalence(self):

        code = """
def unique(items):
    return {x for x in items}
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )   
    def test_dict_comprehension_ast_equivalence(self):

        code = """
def mapping(items):
    return {x: x * x for x in items}
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        ) 
        
    def test_generator_expression_ast_equivalence(self):

        code = """
def stream(items):
    return (x * x for x in items)
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )  
        
    def test_yield_statement_ast_equivalence(self):

        code = """
def numbers():
    yield 1
    yield 2
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
    )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
    )  
    def test_yield_from_ast_equivalence(self):

        code = """
def flatten(items):
    yield from items
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )    
    def test_lambda_multiple_arguments_ast_equivalence(self):

        code = """
def calculate():
    return lambda x, y: x + y
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )
    def test_lambda_default_argument_ast_equivalence(self):

        code = """
def create():
    return lambda x=10: x * 2
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
    )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )    
    def test_lambda_inside_call_ast_equivalence(self):

        code = """
def sort_items(items):
    return sorted(items, key=lambda x: x.value)
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        ) 
    def test_call_with_star_args_ast_equivalence(self):

        code = """
def run(args):
    return execute(*args)
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
       )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )    
    def test_call_with_kwargs_ast_equivalence(self):

        code = """
def run(options):
    return execute(**options)
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
       )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
    ) 
    def test_call_with_star_and_kwargs_ast_equivalence(self):

        code = """
def run(args, options):
    return execute(*args, **options)
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
    )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
    )

        self.assertEqual(
            original_ast,
            formatted_ast
       )    
    def test_nested_function_calls_ast_equivalence(self):

        code = """
def process(value):
    return outer(inner(value))
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
    )

        formatted_ast = ast.dump(
        ast.parse(formatted),
        include_attributes=False
    )

        self.assertEqual(
            original_ast,
            formatted_ast
        ) 
        
    def test_attribute_chain_ast_equivalence(self):

        code = """
def get_name(user):
    return user.profile.account.name
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
            )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        ) 
    def test_attribute_call_chain_ast_equivalence(self):

        code = """
def load(user):
    return user.profile.get_name().strip()
"""

        formatted = self.formatter.format(code)
        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
        ast.parse(formatted),
        include_attributes=False
    )

        self.assertEqual(
            original_ast,
            formatted_ast
    )
    def test_await_attribute_call_chain_ast_equivalence(self):

        code = """
async def load(client):
    return await client.session.fetch()
"""

        formatted = self.formatter.format(code)

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
    )   
   
    def test_formatter_idempotency_simple_function(self):

        code = """
def hello(name):
    return "Hello " + name
"""

        formatted_once = self.formatter.format(code)

        formatted_twice = self.formatter.format(
            formatted_once
        )

        self.assertEqual(
            formatted_once,
            formatted_twice
        )
    def test_formatter_idempotency_nested_blocks(self):

        code = """
def process(items):
    for item in items:
        if item:
            return item
"""

        formatted_once = self.formatter.format(code)

        formatted_twice = self.formatter.format(
            formatted_once
        )

        self.assertEqual(
            formatted_once,
            formatted_twice
        )   
    def test_formatter_idempotency_async_function(self):

        code = """
async def fetch(client):
    data = await client.get()
    return data
"""

        formatted_once = self.formatter.format(code)

        formatted_twice = self.formatter.format(
            formatted_once
    )

        self.assertEqual(
            formatted_once,
            formatted_twice
        )
    def test_formatter_idempotency_match_statement(self):

        code = """
def handle(value):
    match value:
        case 1:
            return "one"
        case _:
            return "other"
"""

        formatted_once = self.formatter.format(code)

        formatted_twice = self.formatter.format(
            formatted_once
        )

        self.assertEqual(
            formatted_once,
            formatted_twice
        )
    def test_formatter_idempotency_try_except_finally(self):

        code = """
def load():
    try:
        return read()
    except Exception:
        return None
    finally:
        close()
"""

        formatted_once = self.formatter.format(code)

        formatted_twice = self.formatter.format(
            formatted_once
        )

        self.assertEqual(
            formatted_once,
            formatted_twice
        )
    def test_formatter_idempotency_class_statement(self):

        code = """
class User:
    def get_name(self):
        return self.name
"""

        formatted_once = self.formatter.format(code)

        formatted_twice = self.formatter.format(
            formatted_once
        )

        self.assertEqual(
            formatted_once,
            formatted_twice
        )
    def test_formatter_idempotency_complex_expression(self):

        code = """
def calculate(data):
    return process(data.items[0].value)
"""

        formatted_once = self.formatter.format(code)

        formatted_twice = self.formatter.format(
            formatted_once
        )

        self.assertEqual(
            formatted_once,
            formatted_twice
        )  
    def test_formatter_idempotency_list_comprehension(self):

        code = """
def build(values):
    return [x * 2 for x in values if x > 0]
"""

        formatted_once = self.formatter.format(code)

        formatted_twice = self.formatter.format(
            formatted_once
        )

        self.assertEqual(
            formatted_once,
            formatted_twice
        )  
    def test_formatter_idempotency_dict_comprehension(self):

        code = """
def build(values):
    return {x: x * 2 for x in values}
"""

        formatted_once = self.formatter.format(code)

        formatted_twice = self.formatter.format(
            formatted_once
        )

        self.assertEqual(
            formatted_once,
            formatted_twice
        )    
    def test_formatter_idempotency_set_comprehension(self):

        code = """
def build(values):
    return {x * 2 for x in values}
"""

        formatted_once = self.formatter.format(code)

        formatted_twice = self.formatter.format(
            formatted_once
        )

        self.assertEqual(
            formatted_once,
            formatted_twice
        )  
    def test_formatter_integration_complex_module(self):

        code = """
import asyncio


class Worker:

    def __init__(self, items):
        self.items = items

    async def process(self):
        results = []

        for item in self.items:
            if item:
                results.append(item)

        return results


async def main():
    worker = Worker([1, 2, 3])
    return await worker.process()
"""

        formatted_once = self.formatter.format(code)

        formatted_twice = self.formatter.format(
            formatted_once
        )

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted_once),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )

        self.assertEqual(
            formatted_once,
            formatted_twice
        )    
    def test_formatter_integration_advanced_module(self):

        code = """
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar("T")


@dataclass
class Box(Generic[T]):

    value: T

    def get(self) -> T:
        return self.value


def process(items: list[int]) -> dict[int, int]:

    result = {
        item: item * 2
        for item in items
        if item > 0
    }

    return result


def handle(value):

    match value:
        case 0:
            return "zero"
        case _:
            return "other"
"""

        formatted_once = self.formatter.format(code)
        print(formatted_once)

        formatted_twice = self.formatter.format(
            formatted_once
        )

        original_ast = ast.dump(
            ast.parse(code),
            include_attributes=False
        )

        formatted_ast = ast.dump(
            ast.parse(formatted_once),
            include_attributes=False
        )

        self.assertEqual(
            original_ast,
            formatted_ast
        )

        self.assertEqual(
            formatted_once,
            formatted_twice
        )
    def test_self_host_engine_module(self):

        from pathlib import Path

        path = Path("core/engine.py")

        code = path.read_text(encoding="utf-8")

        formatted_once = self.formatter.format(code)
        
        from pathlib import Path

        Path("engine_formatted.py").write_text(
            formatted_once,
            encoding="utf-8",
) 
        #formatted_twice = self.formatter.format(formatted_once)

       # original_ast = ast.dump(
            #ast.parse(code),
            #include_attributes=False,
       #)

        #formatted_ast = ast.dump(
            #ast.parse(formatted_once),
            #include_attributes=False,
       #)

        #self.assertEqual(original_ast, formatted_ast)
        #self.assertEqual(formatted_once, formatted_twice)   
        
                                                   
if __name__ == "__main__":
        unittest.main()



    