import logging
from typing import Protocol, runtime_checkable

from design_patterns.structural.composite import Expression, Number

logger = logging.getLogger(__name__)


@runtime_checkable
class Visitorable(Protocol):
    """
    Visitor interface
    """

    def visit_expression(self, expression: Expression) -> None: ...

    def visit_number(self, number: Number) -> None: ...


class CompositeVisitor:
    """
    Concrete Visitor
    """

    @staticmethod
    def visit_expression(expression: Expression) -> None:
        logger.info(expression)

    @staticmethod
    def visit_number(number: Number) -> None:
        logger.info(number)


class Item(Protocol):
    """
    Item interface
    """

    def accept(self, visitor: Visitorable) -> None: ...


class NumberItem(Item, Number):
    def accept(self, visitor: Visitorable) -> None:
        visitor.visit_number(self)


class ExpressionItem(Item, Expression):
    def accept(self, visitor: Visitorable) -> None:
        visitor.visit_expression(self)
