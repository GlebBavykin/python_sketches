import base64
import zlib
from pathlib import Path
from typing import Protocol, runtime_checkable


@runtime_checkable
class Fileable(Protocol):
    """
    File interface
    """

    def write(self, data: str): ...

    def read(self) -> str: ...


class FileHandler:
    """
    File handler with basic methods
    """

    def __init__(self, path: Path):
        self._path = path

    def write(self, data: str | bytes, mode="w") -> None:
        with self._path.open(mode) as file:
            file.write(data)

    def read(self, mode="r") -> str:
        data = ""
        with self._path.open(mode) as file:
            data = file.read()
        return data


class Base64Decorator:
    """
    Base64 decorator for FileHandler
    """

    def __init__(self, source: Fileable):
        self.wrappee = source

    def write(self, data: str):
        base64_data = base64.b64encode(data.encode("utf-8"))
        self.wrappee.write(base64_data.decode("utf-8"))

    def read(self) -> str:
        base64_data = self.wrappee.read()
        return base64.b64decode(base64_data).decode("utf-8")


class ZlibDecorator:
    """
    Zlib decorator for FileHandler
    """

    def __init__(self, source: FileHandler):
        self.wrappee = source

    def write(self, data: str):
        zlib_data = zlib.compress(data.encode("utf-8"))
        self.wrappee.write(zlib_data, mode="wb")

    def read(self) -> str:
        zlib_data = self.wrappee.read(mode="rb")
        return zlib.decompress(zlib_data).decode("utf-8")
