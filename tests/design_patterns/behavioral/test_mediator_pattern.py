import pytest
from _pytest.logging import LogCaptureFixture

from design_patterns.behavioral.mediator import Button, Mediator, TextField


@pytest.fixture(scope="function")
def send_button() -> Button:
    """
    Button instance
    """
    return Button()


@pytest.fixture(scope="function")
def text_field() -> TextField:
    """
    TextField instance
    """
    return TextField()


@pytest.fixture(scope="function")
def dialog(send_button: Button, text_field: TextField) -> Mediator:
    """
    Mediator instance
    """
    return Mediator(send_button, text_field)


@pytest.mark.parametrize(
    "message",
    [
        "Hello, mediator!",
    ],
)
def test_mediator_pattern(
    text_field: TextField, send_button: Button, dialog: Mediator, message: str, caplog: LogCaptureFixture
) -> None:
    """
    Check mediator pattern: send message from text_field by press send_button
    """
    text_field.keypress(message)
    send_button.click()
    assert message in caplog.text
