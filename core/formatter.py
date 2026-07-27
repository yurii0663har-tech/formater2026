class PythonFormatter:

    def __init__(self, indent_size=4):
        self.indent_size = indent_size


    def format(self, code: str) -> str:
        code = self.normalize_tabs(code)
        code = self.fix_indentation(code)
        code = self.clean_spaces(code)

        return code


    def normalize_tabs(self, code):
        return code.replace("\t", " " * self.indent_size)


    def fix_indentation(self, code):
        lines = code.splitlines()

        result = []

        for line in lines:
            if not line.strip():
                result.append("")
                continue

            result.append(line.rstrip())

        return "\n".join(result)

    def clean_spaces(self, code):

        lines = []

        for line in code.splitlines():

            line = line.rstrip()

            lines.append(line)

        return "\n".join(lines)