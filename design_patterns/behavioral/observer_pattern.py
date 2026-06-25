from typing import Any, Protocol


class Subscribable(Protocol):
    """
    Common interface for subscriber
    """

    def update(self, data: Any) -> None: ...


class Publisher:
    """
    The base publisher class
    """

    def __init__(self) -> None:
        self.subscribers: list[Subscribable] = []

    def subscribe(self, subscriber: Subscribable) -> None:
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscribable) -> None:
        self.subscribers.remove(subscriber)

    def notify(self, data: Any) -> None:
        for subscriber in self.subscribers:
            subscriber.update(data)


class Listener(Subscribable):
    """
    The concrete listener class
    """

    def __init__(self) -> None:
        self.messages: list[str] = []

    def update(self, data: Any) -> None:
        self.messages.append(data)

    def get_messages(self) -> str:
        return ", ".join(self.messages)
