from typing import Optional
from uuid import uuid1, uuid8

from faker import Faker
from pydantic import BaseModel, Field, StrictBool, StrictStr

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
