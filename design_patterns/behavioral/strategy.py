import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


# 1. Интерфейс Стратегии
class AuthStrategy(ABC):
    @abstractmethod
    def authenticate(self, user: str):
        raise NotImplementedError("This is a strategy method. You should implement this!")


# 2. Конкретные стратегии
class GuestAuth(AuthStrategy):
    def authenticate(self, user: str = "guest"):
        """
        Авторизации гостя
        """
        logger.info(f"Guest authorization: {user}")


class UserAuth(AuthStrategy):
    def authenticate(self, user: str):
        """
        Авторизации обычного пользователя
        """
        logger.info(f"Regular user Authorization: {user}")


# 3. Контекст
class AuthContext:
    def __init__(self, strategy: AuthStrategy = UserAuth()):
        self._strategy = strategy

    def set_strategy(self, strategy: AuthStrategy):
        self._strategy = strategy

    def login(self, user: str = "user_1"):
        return self._strategy.authenticate(user)
