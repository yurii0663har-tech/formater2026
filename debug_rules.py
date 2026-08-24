from abc import ABC, abstractmethod
class FormattingRule(ABC):
    @abstractmethod
    def apply(self, code: str) -> str:
        pass
class RemoveTrailingSpacesRule(FormattingRule):
    def apply(self, code: str) -> str:
        return '\n'.join((line.rstrip() for line in code.splitlines()))
class RemoveExtraEmptyLinesRule(FormattingRule):
    def apply(self, code: str) -> str:
        result = []
        empty = 0
        for line in code.splitlines():
            if line.strip() == '':
                empty += 1
            else:
                empty = 0
            if empty <= 1:
                result.append(line)
        return '\n'.join(result)