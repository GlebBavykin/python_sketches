from operator import add

import pytest
from _pytest.logging import LogCaptureFixture

from design_patterns.behavioral.visitor_pattern import (CompositeVisitor,
                                                        ExpressionItem,
                                                        NumberItem)


@pytest.fixture(scope="class")
def visitor() -> CompositeVisitor:
    """
    Visitor instance
    """
    return CompositeVisitor()


@pytest.mark.parametrize(
    "expression, outcome",
    [
        (ExpressionItem(NumberItem(1), add, NumberItem(2)), "Value: 3\n"),
    ],
)
def test_visitor_for_composite_expression(
    expression: ExpressionItem, visitor: CompositeVisitor, caplog: LogCaptureFixture, outcome: str
) -> None:
    """
    Check visitor pattern: accept visitor for composite expression and capture log from the console
    """
    expression.accept(visitor)
    assert outcome in caplog.text


@pytest.mark.parametrize(
    "number, outcome",
    [
        (NumberItem(150), "Number: 150\n"),
    ],
)
def test_visitor_for_composite_number(
    number: NumberItem, visitor: CompositeVisitor, caplog: LogCaptureFixture, outcome: str
) -> None:
    """
    Check visitor pattern: accept visitor for composite number and capture log from the console
    """
    number.accept(visitor)
    assert outcome in caplog.text
