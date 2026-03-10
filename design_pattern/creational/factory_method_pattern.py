from __future__ import annotations

import json
import pickle
from abc import abstractmethod, ABC
from pathlib import Path
from typing import Any
from typing import Optional

import yaml

CONFIG_PATH = "my_file.pickle"


class AbstractSaver(ABC):
    @abstractmethod
    def get_config(self) -> Any:
        pass

    @abstractmethod
    def set_config(self, config: dict) -> None:
        pass


class JsonSaver(AbstractSaver):
    """
        Save settings into JSON string
    """

    def __init__(self):
        self.data: Optional[dict] = None

    def get_config(self) -> str:
        return json.dumps(self.data)

    def set_config(self, data: dict) -> None:
        self.data = data


class YamlSaver(AbstractSaver):
    """
        Save settings into YAML string
    """

    def __init__(self):
        self.data: Optional[dict] = None

    def get_config(self) -> str:
        return yaml.dump(self.data)

    def set_config(self, data: dict) -> None:
        self.data = data


class PickleSaver(AbstractSaver):
    """
        Save settings into PICKLE file
    """

    def __init__(self):
        self.data: Optional[dict] = None

    def get_config(self) -> Path:
        path = Path(CONFIG_PATH)
        with open(path, 'wb') as f:
            pickle.dump(self.data, f)
        return path

    def set_config(self, data: dict) -> None:
        self.data = data


class AbstractSettings(ABC):
    def __init__(self, setting: dict) -> None:
        self.setting = setting

    @abstractmethod
    def get_saver(self) -> AbstractSaver:
        raise NotImplementedError("This is a factory method. You should implement this!")

    def save_config(self) -> Any:
        saver = self.get_saver()
        saver.set_config(self.setting)
        return saver.get_config()


class JsonSettings(AbstractSettings):
    def get_saver(self) -> AbstractSaver:
        return JsonSaver()


class PickleSettings(AbstractSettings):
    def get_saver(self) -> AbstractSaver:
        return PickleSaver()


class YamlSettings(AbstractSettings):
    def get_saver(self) -> AbstractSaver:
        return YamlSaver()
