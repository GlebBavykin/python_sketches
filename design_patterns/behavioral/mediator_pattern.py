import logging
from typing import Protocol

logger = logging.getLogger(__name__)


class Notifiable(Protocol):
    """
    Common interface for mediators
    """

    def notify(self, sender, event: str) -> None: ...


class Mediator(Notifiable):
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

    def __init__(self, mediator: Mediator | None = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator | None:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Button(Component):
    """
    Buttons communicate with a mediator
    """

    def click(self) -> None:
        self.mediator.notify(self, "click")


class TextField(Component):
    """
    TextFields communicate with a mediator
    """

    def keypress(self, text) -> None:
        self.mediator.notify(self, text)
