import ast
import textwrap


class Parser:

    def parse(self, code: str):
        code = code.replace("\ufeff", "")
        code = textwrap.dedent(code)

        try:
            return ast.parse(code)
        except IndentationError:
            lines = code.splitlines()

            fixed_lines = []
            level = 0

            for line in lines:
                stripped = line.strip()

                if not stripped:
                    fixed_lines.append("")
                    continue

                # Закрываем предыдущий блок перед elif/else/except/finally
                if stripped.startswith(("elif ", "else:", "except", "finally:")):
                    level = max(0, level - 1)

                fixed_lines.append(
                    "    " * level + stripped
                )

                # Строка с ":" открывает новый блок
                if stripped.endswith(":"):
                    level += 1

            code = "\n".join(fixed_lines)

            return ast.parse(code)