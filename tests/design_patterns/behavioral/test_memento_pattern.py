import pytest

from design_patterns.behavioral.memento import Caretaker, Originator


@pytest.fixture(scope="function")
def originator() -> Originator:
    """
    Originator instance
    """
    return Originator(text="Just text", x=100, y=200)


@pytest.fixture(scope="function")
def caretaker(originator: Originator) -> Caretaker:
    """
    Caretaker instance
    """
    return Caretaker(originator)


@pytest.mark.parametrize(
    "previous_text, new_text",
    [("Hello world!", "Bye world!")],
)
def test_memento_pattern_1(
    originator: Originator, caretaker: Caretaker, previous_text: str, new_text: str
) -> None:
    """
    Test memento pattern: change originator text and undo it to previous text
    """
    originator.text = previous_text
    assert originator.text == previous_text
    caretaker.backup()

    originator.text = new_text
    assert originator.text == new_text

    caretaker.undo()
    assert originator.text == previous_text
