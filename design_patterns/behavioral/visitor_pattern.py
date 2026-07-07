import logging
from typing import Protocol

from design_patterns.structural.composite import Expression, Number

logger = logging.getLogger(__name__)


class Visitor(Protocol):
    """
    Visitor interface
    """

    def visit_expression(self, expression: Expression) -> None: ...

    def visit_number(self, number: Number) -> None: ...


class CompositeVisitor(Visitor):
    """
    Concrete Visitor
    """

    def visit_expression(self, expression: Expression) -> None:
        logger.info(expression)

    def visit_number(self, number: Number) -> None:
        logger.info(number)


class Item(Protocol):
    """
    Item interface
    """

    def accept(self, visitor: Visitor) -> None: ...


class NumberItem(Item, Number):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_number(self)


class ExpressionItem(Item, Expression):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_expression(self)
