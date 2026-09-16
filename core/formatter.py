class PythonFormatter:

    def __init__(self, indent_size=4, quote_style="single", max_line_length=120): 
        self.indent_size = indent_size
        self.quote_style = quote_style
        self.max_line_length = max_line_length

    def format(self, code: str) -> str:
        code = self.normalize_tabs(code)
        code = self.fix_indentation(code)
        code = self.clean_spaces(code)
        code = self.apply_quote_style(code)

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

    def limit_line_length(self, code):
        lines = []

        for line in code.splitlines():
            if len(line) <= self.max_line_length:
                lines.append(line)
                continue

            words = line.split()
            current = ""

            for word in words:
                if not current:
                    current = word
                elif len(current) + 1 + len(word) <= self.max_line_length:
                    current += " " + word
                else:
                    lines.append(current)
                    current = word

            if current:
                lines.append(current)

        return "\n".join(lines)

    def apply_quote_style(self, code):
        if self.quote_style == "single":
            return code

        if self.quote_style != "double":
            return code

        import io
        import tokenize

        tokens = []
        reader = io.StringIO(code).readline

        for token in tokenize.generate_tokens(reader):
            if token.type == tokenize.STRING:
                value = token.string

                if value.startswith("'") and value.endswith("'"):
                    value = '"' + value[1:-1].replace('"', '\\"') + '"'

                token = tokenize.TokenInfo(
                    token.type,
                    value,
                    token.start,
                    token.end,
                    token.line,
                )

            tokens.append(token)

        return tokenize.untokenize(tokens)
