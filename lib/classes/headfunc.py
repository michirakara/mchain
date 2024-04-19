from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .expression import Expression


class HeadFunc:
    def __init__(self, name: str, args: list[Expression]):
        self.name: str = name
        self.args: list[Expression] = args

    def __str__(self):
        return f"HeadFunc({self.name}, {self.args})"

    def __repr__(self):
        return self.__str__()
