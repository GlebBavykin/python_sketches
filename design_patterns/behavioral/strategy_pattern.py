from abc import ABC, abstractmethod
from typing import Optional
from uuid import uuid8, uuid1

from faker import Faker
from pydantic import BaseModel, Field, StrictStr, StrictBool

fake = Faker()


class User(BaseModel):
    """
    Пользователь
    """

    user_id: StrictStr = Field(default=None, description="Внутренний уникальный идентификатор")
    external_user_id: StrictStr = Field(default=f"{fake.name()}", description="Внешний идентификатор пользователя")
    nickname: StrictStr = Field(default=f"{fake.name()}", description="Псевдоним пользователя")
    email: StrictStr = Field(default=f"{fake.email()}", description="Email пользователя")
    password: StrictStr = Field(default=f"{fake.password()}", description="Пароль пользователя")
    session_id: StrictStr = Field(default=None, description="Сессия пользователя")
    is_guest: StrictBool = Field(default=False, description="фла, что пользователь гость")


class GuestLoginRequest(BaseModel):
    """
    Запрос на авторизацию гостя
    """

    nickname: StrictStr = Field(default=..., description="Псевдоним пользователя")
    stay_signed_in: Optional[StrictBool] = Field(default=True, description="Нужно ли сохранять токен в БД")


class LoginRequest(BaseModel):
    """
    Запрос на авторизацию пользователя
    """

    login: StrictStr = Field(default=..., description="Логин пользователя ")
    password: StrictStr = Field(default=..., description="Пароль пользователя ")
    stay_signed_in: Optional[StrictBool] = Field(default=True, description="Нужно ли сохранять токен в БД")


class AuthApi:
    """
    API авторизации пользователей
    """

    def __init__(self, headers):
        self._headers = headers

    def guest_login(self, request: GuestLoginRequest) -> User | str:
        if len(self._headers) > 0:
            return User(session_id=f"{uuid8()}", user_id=f"{uuid1()}", external_user_id=request.nickname)
        else:
            return "ERROR"

    def login(self, request: LoginRequest) -> User | str:
        if len(self._headers) > 0:
            return User(
                session_id=f"{uuid8()}", user_id=f"{uuid1()}", external_user_id=request.login, password=request.password
            )
        else:
            return "ERROR"


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
