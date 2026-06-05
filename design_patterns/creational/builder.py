from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Self


class Product:
    def __init__(self):
        self._parts: List[str] = []

    def add_part(self, part: str):
        self._parts.append(part)

    def get_parts(self) -> List[str]:
        return self._parts


class Builder(ABC):
    @abstractmethod
    def get_result(self) -> Product:
        pass

    @abstractmethod
    def produce_part_a(self) -> Self:
        pass

    @abstractmethod
    def produce_part_b(self) -> Self:
        pass

    @abstractmethod
    def produce_part_c(self) -> Self:
        pass
