from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Self


class Product:
    def __init__(self) -> None:
        self._parts: List[str] = []

    def add_part(self, part: str):
        self._parts.append(part)

    def get_parts(self) -> List[str]:
        return self._parts


class Builder(ABC):
    @abstractmethod
    def get_result(self) -> list[str]:
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


class ConcreteBuilder(Builder):
    def __init__(self):
        self._product = Product()

    def get_result(self) -> list[str]:
        product = self._product.get_parts()
        self._product = Product()
        return product

    def produce_part_a(self):
        self._product.add_part("a")
        return self

    def produce_part_b(self):
        self._product.add_part("b")
        return self

    def produce_part_c(self):
        self._product.add_part("c")
        return self
