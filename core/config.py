class FormatterConfig:

    def __init__(
        self,
        indent_size=4,
        max_line_length=120,
        quote_style="single"
    ):

        self.indent_size = indent_size
        self.max_line_length = max_line_length
        self.quote_style = quote_style