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
        indent = 0

        for line in lines:

            stripped = line.strip()

            if not stripped:
                result.append("")
                continue


            # уменьшение уровня перед блоками
            if stripped.startswith(
                ("elif ", "else:", "except", "finally:")
            ):
                indent -= 1


            result.append(
                " " * (indent * self.indent_size)
                + stripped
            )


            # увеличение после :
            if stripped.endswith(":"):
                indent += 1


        return "\n".join(result)


    def clean_spaces(self, code):

        lines = []

        for line in code.splitlines():

            line = line.rstrip()

            lines.append(line)

        return "\n".join(lines)