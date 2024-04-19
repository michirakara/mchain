from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .expression import Expression
    from .variable import Variable


class Line:
    def __init__(self, lhs: Variable, rhs: Expression):
        self.lhs: Variable = lhs
        self.rhs: Expression = rhs

    def __str__(self):
        return f"Line({self.lhs}, {self.rhs})"

    def __repr__(self):
        return self.__str__()
