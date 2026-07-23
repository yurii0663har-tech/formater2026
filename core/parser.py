import ast
import textwrap


class Parser:

    def parse(self, code: str):

        code = textwrap.dedent(code)

        return ast.parse(code)