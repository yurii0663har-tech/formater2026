from core.parser import Parser
from core.engine import FormatterEngine
from core.formatter import PythonFormatter
from core.config import FormatterConfig

from core.rules import (
    RemoveTrailingSpacesRule,
    RemoveExtraEmptyLinesRule,
)
class FormatterPipeline:

    def __init__(self, config=None):

        if config is None:
            config = FormatterConfig()

        self.config = config

        self.parser = Parser()

        self.engine = FormatterEngine(
            indent_size=config.indent_size
        )

        self.formatter = PythonFormatter(
            indent_size=config.indent_size
        )

        self.rules = [
            RemoveTrailingSpacesRule(),
        RemoveExtraEmptyLinesRule(),
]
    def format(self, code):

        tree = self.parser.parse(code)

        result = self.engine.format(tree)

        result = self.formatter.format(result)

        for rule in self.rules:
            result = rule.apply(result)

        return result