from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .headfunc import HeadFunc
    from .value import Value
    from .variable import Variable


class Head:
    def __init__(self, val: HeadFunc | Value | Variable):
        self.val: HeadFunc | Value | Variable = val

    def __str__(self):
        return f"Head({self.val})"

    def __repr__(self):
        return self.__str__()
