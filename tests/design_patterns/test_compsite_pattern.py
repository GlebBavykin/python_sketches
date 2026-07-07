from operator import add, mul

import pytest

from design_patterns.structural.composite import Expression, Number


@pytest.mark.parametrize(
    "expression, outcome",
    [
        (Expression(Number(1), add, Number(2)), 3),
    ],
)
def test_calculate_composite_1(expression: Expression, outcome: float) -> None:
    """
    Calculate value of simple expression
    """
    assert expression.value == outcome


@pytest.mark.parametrize(
    "expression, outcome",
    [
        (
            Expression(
                Expression(Number(3), mul, Number(5)),
                add,
                Expression(Number(7), mul, Number(8)),
            ),
            71,
        ),
    ],
)
def test_calculate_composite_2(expression: Expression, outcome: float) -> None:
    """
    Calculate value of nested expression
    """
    assert expression.value == outcome
