from __future__ import annotations

import json
from abc import abstractmethod, ABC
from typing import Any
from typing import Optional

import yaml


class AbstractSaver(ABC):
    def __init__(self, data: Optional[dict] = None):
        self.data: Optional[dict] = data

    def set_config(self, data: dict) -> None:
        self.data = data

    @abstractmethod
    def save_config(self) -> Any:
        raise NotImplementedError("This is a factory method. You should implement this!")


class JsonSaver(AbstractSaver):
    """
    Save settings into JSON string
    """

    def save_config(self) -> str:
        return json.dumps(self.data)


class YamlSaver(AbstractSaver):
    """
    Save settings into YAML string
    """

    def save_config(self) -> str:
        return yaml.dump(self.data)
