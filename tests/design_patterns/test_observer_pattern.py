import pytest

from design_patterns.behavioral.observer_pattern import Listener, Publisher


@pytest.fixture(scope="class")
def publisher() -> Publisher:
    """
    Create publisher
    """
    return Publisher()


@pytest.fixture(scope="class")
def subscribers(publisher: Publisher) -> list[Listener]:
    """
    Create list of subscribers
    """
    subscribers_list = []
    for _ in range(10):
        listener = Listener()
        publisher.subscribe(listener)
        subscribers_list.append(listener)
    return subscribers_list


@pytest.mark.parametrize(
    "message",
    ["Hello world!"],
)
def test_observer_pattern(publisher: Publisher, subscribers: list[Listener], message: str):
    """
    Test observer pattern: notify all subscribers from publisher
    """

    publisher.notify(message)

    for subscriber in subscribers:
        assert message in subscriber.get_messages()
