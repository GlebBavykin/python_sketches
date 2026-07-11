import pytest

from design_patterns.behavioral.command import (
    OpenCommand,
    PrintCommand,
    Receiver,
    SaveCommand,
    Sender,
)


@pytest.fixture(scope="function")
def sender() -> Sender:
    """
    Sender instance
    """
    return Sender()


@pytest.fixture(scope="function")
def receiver() -> Receiver:
    """
    Receiver instance
    """
    return Receiver()


@pytest.mark.parametrize(
    "command, params, outcome",
    [
        (SaveCommand, "json=True", "save_request with json=True params"),
        (OpenCommand, "verbose=True", "open_request with verbose=True params"),
        (PrintCommand, "plain_text=True", "print_request with plain_text=True params"),
    ],
)
def test_command_pattern(
    command: type[SaveCommand | OpenCommand | PrintCommand],
    params: str,
    outcome: str,
    sender: Sender,
    receiver: Receiver,
) -> None:
    """
    Check command pattern: send request with params to Command instance
    """
    sender.command = command(receiver, params)
    sender.execute()
    assert outcome in receiver.get_request()
