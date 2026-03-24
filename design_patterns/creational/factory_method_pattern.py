from __future__ import annotations

import json
from abc import abstractmethod, ABC
from typing import Any
from typing import Optional

import yaml


class AbstractSettings(ABC):
    def __init__(self, config: Optional[dict] = None):
        self._config: Optional[dict] = config

    @property
    def config(self) -> Optional[dict]:
        return self._config

    @config.setter
    def config(self, config: dict):
        self._config = config

    @abstractmethod
    def save_config(self) -> Any:
        raise NotImplementedError("This is a factory method. You should implement it!")


class JsonSettings(AbstractSettings):
    """
    Save settings into JSON string
    """

    def save_config(self) -> str:
        # json product
        return json.dumps(self.config)


class YamlSettings(AbstractSettings):
    """
    Save settings into YAML string
    """

    def save_config(self) -> str:
        # yaml product
        return yaml.dump(self.config)
