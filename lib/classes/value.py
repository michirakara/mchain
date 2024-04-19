from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .function import Function


class Value:
    def __init__(self, val: int | float | str | list | bool | Function):
        self.val: int | float | str | list | bool | Function = val

    def __str__(self):
        return f"Value({self.val})"

    def __repr__(self):
        return self.__str__()
