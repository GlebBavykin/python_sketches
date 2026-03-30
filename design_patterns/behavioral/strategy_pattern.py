from abc import ABC, abstractmethod

from api.mock_service import AuthApi, User, GuestLoginRequest, LoginRequest


# 1. Интерфейс Стратегии
class AuthStrategy(ABC):
    @abstractmethod
    def authenticate(self, user: User, headers: list):
        pass


# 2. Конкретные стратегии
class GuestAuth(AuthStrategy):
    def authenticate(self, user: User, headers: list):
        """
        Авторизации гостя
        """
        request = GuestLoginRequest(nickname=user.nickname)
        response = AuthApi(headers).guest_login(request)
        if response == "ERROR":
            raise AttributeError
        else:
            user.session_id = response.session_id
            user.user_id = response.user_id


class UserAuth(AuthStrategy):
    def authenticate(self, user: User, headers: list):
        """
        Авторизации обычного пользователя
        """
        request = LoginRequest(login=user.external_user_id, password=user.password)
        response = AuthApi(headers).login(request)
        if response == "ERROR":
            raise AttributeError
        else:
            user.session_id = response.session_id
            user.user_id = response.user_id


# 3. Контекст
class AuthContext:
    def __init__(self, strategy: AuthStrategy = UserAuth()):
        self._strategy = strategy

    def set_strategy(self, strategy: AuthStrategy):
        self._strategy = strategy

    def login(self, user: User, headers: list):
        return self._strategy.authenticate(user, headers)
