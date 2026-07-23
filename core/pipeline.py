from core.parser import Parser
from core.engine import FormatterEngine
from core.formatter import PythonFormatter


class FormatterPipeline:

    def __init__(self):

        self.parser = Parser()
        self.engine = FormatterEngine()
        self.formatter = PythonFormatter()


    def format(self, code):

        tree = self.parser.parse(code)

        result = self.engine.format(tree)

        result = self.formatter.format(result)

        return result