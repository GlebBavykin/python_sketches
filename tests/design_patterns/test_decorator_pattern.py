from pathlib import Path
from typing import Generator

import pytest

from design_patterns.structural.decorator import (Base64Decorator, FileHandler,
                                                  ZlibDecorator)


@pytest.fixture(scope="class")
def handler() -> Generator[FileHandler, None, None]:
    """
    FileHandler instance
    """
    path = Path("test.txt")
    yield FileHandler(path)
    path.unlink(missing_ok=True)


@pytest.fixture(scope="class")
def data() -> str:
    """
    Testing string data
    """
    return "Python is a powerful language. " * 10


@pytest.mark.parametrize(
    "decorator",
    [
        Base64Decorator,
        ZlibDecorator,
    ],
)
def test_write_data_with_decorators(handler: FileHandler, data: str, decorator: type[Base64Decorator | ZlibDecorator]):
    """
    Write/Read string data with different decorators
    """
    decorated_handler = decorator(handler)
    decorated_handler.write(data)
    assert decorated_handler.read() == data
