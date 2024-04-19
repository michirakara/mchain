from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .variable import Variable
    from .expression import Expression


class Function:
    def __init__(self, *vars: Variable, expression: Expression):
        self.vars = list(vars)
        self.expression = expression
