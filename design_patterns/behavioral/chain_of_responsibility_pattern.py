import logging
from dataclasses import dataclass
from typing import Any, Protocol

logger = logging.getLogger(__name__)

@dataclass
class UserRequest:
    username: str = None
    email: str = None
    is_active: bool = False


class Executable(Protocol):
    """
    Common interface for handlers
    """

    def execute(self, request: UserRequest) -> None: ...

    def set_next_handler(self, handler: Any) -> None: ...


class BaseHandler(Executable):
    def __init__(self, next_handler: BaseHandler | None = None) -> None:
        self._next = next_handler

    def set_next_handler(self, handler: BaseHandler) -> None:
        self._next = handler

    def execute(self, request: UserRequest) -> None:
        if self._next:
            self._next.execute(request)


class CheckName(BaseHandler):
    def execute(self, request: UserRequest) -> None:
        if request.username:
            logger.info(request.username)
        super().execute(request)


class CheckEmail(BaseHandler):
    def execute(self, request: UserRequest) -> None:
        if request.email:
            logger.info(request.email)
        super().execute(request)


class CheckIsActive(BaseHandler):
    def execute(self, request: UserRequest) -> None:
        if request.is_active:
            logger.info("active" if request.is_active else "inactive")
        super().execute(request)
