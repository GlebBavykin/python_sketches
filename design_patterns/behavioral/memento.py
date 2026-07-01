from dataclasses import dataclass


@dataclass(frozen=True)
class Memento:
    text: str
    x: float
    y: float


class Originator:
    def __init__(self, text: str, x: float | int, y: float | int) -> None:
        self.text = text
        self._x = x
        self._y = y

    def snapshot(self) -> Memento:
        return Memento(self.text, self._x, self._y)

    def restore(self, snapshot: Memento) -> None:
        self.text = snapshot.text
        self._x = snapshot.x
        self._y = snapshot.y


class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._originator = originator
        self._history: list[Memento] = []

    def backup(self) -> None:
        self._history.append(self._originator.snapshot())

    def undo(self):
        if len(self._history) > 0:
            self._originator.restore(self._history.pop())
