from __future__ import annotations

from abc import abstractmethod, ABC
from typing import Any, Optional


class Saver(ABC):
    @abstractmethod
    def save(self) -> Any:
        pass

    @abstractmethod
    def set_config(self, config: Any) -> None:
        pass


class Settings:
    def __init__(self, setting) -> None:
        self.factory_method: Optional[Saver] = None
        self.setting = setting

    def set_factory_method(self, factory_method: Saver) -> None:
        self.factory_method = factory_method

    def save_config(self) -> Any:
        if self.factory_method is not None:
            self.factory_method.set_config(self.setting)
            return self.factory_method.save()
        return None
