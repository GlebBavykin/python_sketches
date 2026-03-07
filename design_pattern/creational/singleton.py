from typing import Any, Optional, Self


class Singleton:
    __instance: Optional[Self] = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, data: Any) -> None:
        if not hasattr(self, "_initialised"):
            self.__data = data
            self._initialised = True

    def get_data(self):
        return self.__data

    def set_data(self, data: Any) -> None:
        self.__data = data
