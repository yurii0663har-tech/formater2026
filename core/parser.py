import ast


class PythonParser:

    def __init__(self):
        self.tree = None


    def parse(self, code: str):

        try:
            self.tree = ast.parse(code)
            return self.tree

        except SyntaxError as error:
            return error


    def get_structure(self):

        if not self.tree:
            return None

        result = []

        for node in ast.walk(self.tree):

            result.append(
                type(node).__name__
            )

        return result