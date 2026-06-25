import pytest

from design_patterns.behavioral.observer_pattern import Listener, Publisher


@pytest.fixture(scope="function")
def publisher() -> Publisher:
    """
    Create publisher
    """
    return Publisher()


@pytest.fixture(scope="function")
def listeners() -> list[Listener]:
    """
    Create list of listeners
    """
    listeners_list = []
    for _ in range(10):
        listener = Listener()
        listeners_list.append(listener)
    return listeners_list


@pytest.fixture(scope="function")
def subscribers(publisher: Publisher) -> list[Listener]:
    """
    Create list of subscribers
    """
    subscribers_list = []
    for _ in range(10):
        listener = Listener()
        subscribers_list.append(listener)
        publisher.subscribe(listener)
    return subscribers_list


@pytest.mark.parametrize(
    "message",
    ["Hello world!"],
)
def test_observer_pattern_1(publisher: Publisher, listeners: list[Listener], message: str):
    """
    Test observer pattern: subscribe and notify all subscribers from publisher
    """
    for listener in listeners:
        publisher.subscribe(listener)

    publisher.notify(message)

    for subscriber in listeners:
        assert message in subscriber.get_messages()


@pytest.mark.parametrize(
    "message",
    ["Hello world!"],
)
def test_observer_pattern_2(publisher: Publisher, subscribers: list[Listener], message: str):
    """
    Test observer pattern: unsubscribe all subscribers from publisher
    """
    for subscriber in subscribers:
        publisher.unsubscribe(subscriber)

    publisher.notify(message)

    for subscriber in subscribers:
        assert message not in subscriber.get_messages()
