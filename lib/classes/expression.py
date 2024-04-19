from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .head import Head
    from .method import Method


class Expression:
    def __init__(self, head: Head, chain: list[Method]):
        self.head: Head = head
        self.chain: list[Method] = chain

    def __str__(self):
        return f"Expression({self.head},{self.chain})"

    def __repr__(self):
        return self.__str__()
