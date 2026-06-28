from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self): ...


class Sender:
    def __init__(self, command: Command | None = None) -> None:
        self._command = command

    @property
    def command(self) -> Command | None:
        return self._command

    @command.setter
    def command(self, command: Command):
        self._command = command

    def execute(self) -> None:
        if self._command is not None:
            self._command.execute()
        else:
            raise Exception("Command is not set")


class Receiver:
    def __init__(self) -> None:
        self._received_request = []

    def get_request(self):
        return self._received_request.pop(0)

    def send_request(self, request: str, params: str) -> None:
        self._received_request.append(f"{request} with {params} params")


class SaveCommand(Command):
    def __init__(self, receiver: Receiver, params: str) -> None:
        self._receiver = receiver
        self._params = params

    def execute(self) -> None:
        self._receiver.send_request("save_request", self._params)


class OpenCommand(Command):
    def __init__(self, receiver: Receiver, params: str) -> None:
        self._receiver = receiver
        self._params = params

    def execute(self) -> None:
        self._receiver.send_request("open_request", self._params)


class PrintCommand(Command):
    def __init__(self, receiver: Receiver, params: str) -> None:
        self._receiver = receiver
        self._params = params

    def execute(self) -> None:
        self._receiver.send_request("print_request", self._params)
