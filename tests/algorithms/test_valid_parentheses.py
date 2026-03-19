import pytest

from algorithms.valid_parentheses import is_valid_parentheses


@pytest.mark.parametrize(
    "expression, result",
    [
        # Одна незакрытая скобка
        ("[", False),
        ("(", False),
        ("{", False),
        ("]", False),
        (")", False),
        ("}", False),
        # Две соответствующие закрытые скобки
        ("[]", True),
        ("()", True),
        ("{}", True),
        # Две несоответствующие закрытые скобки
        ("[)", False),
        ("[}", False),
        ("(]", False),
        ("(}", False),
        ("{]", False),
        ("{)", False),
        # Три скобки
        ("[({", False),
        ("])}", False),
        ("[{}", False),
        ("]{}", False),
        # Четыре скобки
        ("[()]", True),
        ("[}{]", False),
        ("[{)]", False),
        ("[{]]", False),
    ],
)
def test_validate_parentheses(expression, result):
    """
    Check if the parentheses has pairs
    """
    assert is_valid_parentheses(expression) == result
