import ast


class CodeAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.blocks = []


    def visit_FunctionDef(self, node):

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