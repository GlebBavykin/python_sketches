import pytest
from algorithms.reverse_polish_notation import evaluate_rpn


@pytest.mark.parametrize(
    "expression,result",
    [
        ("1 2 +", 3),
        ("5 2 -", 3),
        ("2 3 *", 6),
        ("6 2 /", 3),
        ("36 2 /", 18),
    ],
)
def test_simple_expressions(expression, result):
    """
    Evaluate simple reverse polish expression
    """
    assert evaluate_rpn(expression) == result


@pytest.mark.parametrize(
    "expression,result",
    [
        ("1+2", 3),
        ("5-2", 3),
        ("2*3", 6),
        ("6/2", 3),
    ],
)
def test_invalid_expressions(expression, result):
    """
    Evaluate invalid expression
    """
    with pytest.raises(Exception):
        assert evaluate_rpn(expression) == result


@pytest.mark.parametrize(
    "expression,result",
    [
        ("4 8 + 1 3 + /", 3),
        ("2 4 8 + *", 24),
        ("3 4 + 5 6 + *", 77),
        ("3 4 - 5 +", 4),
        ("3 4 - 5 + ", 4),
    ],
)
def test_complex_expressions(expression, result):
    """
    Evaluate complex reverse polish expression
    """
    assert evaluate_rpn(expression) == result
