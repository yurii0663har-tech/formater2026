import unittest
import ast

from core.analyzer import CodeAnalyzer


class TestCodeAnalyzer(unittest.TestCase):

    def test_function(self):
        code = """
def hello():
    print("Hello")
"""

        tree = ast.parse(code)

        analyzer = CodeAnalyzer()
        analyzer.visit(tree)

        self.assertEqual(
            analyzer.blocks,
            [
                {
                    "type": "function",
                    "name": "hello",
                    "line": 2
                }
            ]
        )

    def test_class(self):
        code = """
class Person:
    pass
"""

        tree = ast.parse(code)

        analyzer = CodeAnalyzer()
        analyzer.visit(tree)

        self.assertEqual(
            analyzer.blocks,
            [
                {
                    "type": "class",
                    "name": "Person",
                    "line": 2
                }
            ]
        )

    def test_method_inside_class(self):
        code = """
class Person:
    def hello(self):
        pass
"""

        tree = ast.parse(code)

        analyzer = CodeAnalyzer()
        analyzer.visit(tree)

        self.assertEqual(
            analyzer.blocks,
            [
                {
                    "type": "class",
                    "name": "Person",
                    "line": 2
                },
                {
                    "type": "function",
                    "name": "hello",
                    "line": 3
                }
            ]
        )

    def test_async_function(self):
        code = """
async def load_data():
    pass
"""

        tree = ast.parse(code)

        analyzer = CodeAnalyzer()
        analyzer.visit(tree)

        self.assertEqual(
            analyzer.blocks,
            [
                {
                    "type": "function",
                    "name": "load_data",
                    "line": 2
                }
            ]
        )


if __name__ == "__main__":
    unittest.main()
