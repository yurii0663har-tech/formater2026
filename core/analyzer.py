import ast


class CodeAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.blocks = []

    def visit_FunctionDef(self, node):

        decorators = []

        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Name):
                decorators.append(decorator.id)

            elif isinstance(decorator, ast.Call):
                if isinstance(decorator.func, ast.Attribute):
                    decorators.append(decorator.func.attr)

        self.blocks.append(
            {
                "type": "function",
                "name": node.name,
                "line": node.lineno,
                "decorators": decorators
            }
        )

        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):

        self.blocks.append(
            {
                "type": "function",
                "name": node.name,
                "line": node.lineno
            }
        )

        self.generic_visit(node)

    def visit_ClassDef(self, node):

        self.blocks.append(
            {
                "type": "class",
                "name": node.name,
                "line": node.lineno
            }
        )

        self.generic_visit(node)
