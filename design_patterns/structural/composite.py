from collections.abc import Callable
from typing import Protocol


class Evaluatable(Protocol):
    """
    Common interface for numbers and expressions
    """

    def eval(self) -> float: ...


class Number(Evaluatable):
    """
    Leaf of expression class
    """

    def __init__(self, value: float):
        self._value = value

    def eval(self) -> float:
        return self._value

    def __str__(self) -> str:
        return f"Number: {self.eval()}"


class Expression(Evaluatable):
    """
    Container of numbers and operation
    """

    def __init__(self, operand_a: Number | Expression, operation: Callable, operand_b: Number | Expression):
        self._operand_a = operand_a
        self._operation = operation
        self._operand_b = operand_b

    def eval(self) -> float:
        return self._operation(self._operand_a.eval(), self._operand_b.eval())

    def __str__(self) -> str:
        return f"Value: {self.eval()}"
