import logging
from typing import Protocol, runtime_checkable

logger = logging.getLogger(__name__)


@runtime_checkable
class Notifiable(Protocol):
    """
    Common interface for mediators
    """

    def notify(self, sender, event: str) -> None: ...


class Mediator:
    """
    Mediator for components
    """

    def __init__(self, send_button: Button, text_field: TextField) -> None:
        self.send_button = send_button
        self.send_button.mediator = self
        self.text_field = text_field
        self.text_field.mediator = self
        self.message = ""

    def notify(self, sender, event: str):
        if isinstance(sender, Button) and event == "click":
            logger.info(self.message)
            self.message = ""
        elif isinstance(sender, TextField):
            self.message += event


class Component:
    """
    Components communicate with a mediator
    """

    def __init__(self, mediator: Notifiable | None = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Notifiable | None:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Notifiable) -> None:
        self._mediator = mediator


class Button(Component):
    """
    Buttons communicate with a mediator
    """

    def click(self) -> None:
        if self.mediator is None:
            raise Exception("No mediator provided")
        else:
            self.mediator.notify(self, "click")


class TextField(Component):
    """
    TextFields communicate with a mediator
    """

    def keypress(self, text) -> None:
        if self.mediator is None:
            raise Exception("No mediator provided")
        else:
            self.mediator.notify(self, text)
