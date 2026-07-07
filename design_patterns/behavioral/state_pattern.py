from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, document: Document) -> None:
        self._document = document

    @property
    def document(self) -> Document:
        return self._document

    @abstractmethod
    def approved(self): ...


class Document:
    def __init__(self, name: str) -> None:
        self.name = name
        self._state: State = DraftState(self)

    def __str__(self):
        return f"Document {self.name}"

    @property
    def state(self):
        return self._state

    def change_state(self, new_state: State) -> None:
        self._state = new_state

    def publish(self):
        self._state.approved()


class PublishedState(State):
    def approved(self): ...

    def __str__(self):
        return f"{self.document} is published"


class ModerationState(State):
    def approved(self):
        self._document.change_state(PublishedState(self.document))

    def __str__(self):
        return f"{self.document} is moderating"


class DraftState(State):
    def approved(self):
        self._document.change_state(ModerationState(self.document))

    def __str__(self):
        return f"{self.document} is drafting"
