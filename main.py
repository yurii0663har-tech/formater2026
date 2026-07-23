import ast

from core.engine import FormatterEngine
from core.config import FormatterConfig

code = """
def process(items):

    total = 0

    for item in items:

        if item > 0:
            total = total + item

    while total < 100:
        total = total + 1

    return total
"""


# Создаем AST-дерево Python-кода
tree = ast.parse(code)


# Запускаем форматировщик
formatter = FormatterEngine()


result = formatter.format(tree)


print(result)