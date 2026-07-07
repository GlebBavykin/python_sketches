from collections.abc import Callable
from typing import Protocol


class Calculable(Protocol):
    """
    Common interface for numbers and expressions
    """

    def value(self) -> float: ...


class Number(Callable):
    """
    Leaf of expression class
    """

    def __init__(self, value: float):
        self._value = value

    @property
    def value(self) -> float:
        return self._value

    def __str__(self) -> str:
        return f"Number: {self.value}"


class Expression(Callable):
    """
    Container of numbers and operation
    """

    def __init__(self, operand_a: Number | Expression, operation: Callable, operand_b: Number | Expression):
        self._operand_a = operand_a
        self._operation = operation
        self._operand_b = operand_b

    @property
    def value(self) -> float:
        return self._operation(self._operand_a.value, self._operand_b.value)

    def __str__(self) -> str:
        return f"Value: {self.value}"
