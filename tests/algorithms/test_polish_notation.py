import pytest
from algorithms.polish_notation import evaluate_pn


@pytest.mark.parametrize(
    "reverse, expression, result",
    [
        (True, "1 2 +", 3),
        (True, "5 2 -", 3),
        (True, "2 3 *", 6),
        (True, "36 2 /", 18),
        (False, "+ 1 2", 3),
        (False, "- 5 2", 3),
        (False, "* 2 3", 6),
        (False, "/ 36 2", 18),
    ],
)
def test_simple_expressions(reverse, expression, result):
    """
    Evaluate simple polish expressions
    """
    assert evaluate_pn(expression, reverse) == result


@pytest.mark.parametrize(
    "reverse, expression, result",
    [
        (True, "1+2", 3),
        (True, "5-2", 3),
        (True, "2*3", 6),
        (True, "6/2", 3),
        (False, "1+2", 3),
        (False, "5-2", 3),
        (False, "2*3", 6),
        (False, "6/2", 3),
    ],
)
def test_invalid_expressions(reverse, expression, result):
    """
    Evaluate invalid expressions
    """
    with pytest.raises(Exception):
        assert evaluate_pn(expression, reverse) == result


@pytest.mark.parametrize(
    "reverse, expression, result",
    [
        (True, "4 8 + 1 3 + /", 3),
        (True, "2 4 8 + *", 24),
        (True, "3 4 + 5 6 + *", 77),
        (True, "3 4 - 5 +", 4),
        (False, "/ + 4 8 + 1 3", 3),
        (False, "* 2 + 4 8", 24),
        (False, "* + 3 4 + 5 6", 77),
        (False, "+ + 1 * 2 3 4", 11),
        (False, "* + 1 2 + 3 4", 21),
        (False, "+ * + 1 2 3 4", 13),
    ],
)
def test_complex_expressions(reverse, expression, result):
    """
    Evaluate complex polish expressions
    """
    assert evaluate_pn(expression, reverse) == result
