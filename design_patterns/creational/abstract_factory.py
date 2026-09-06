from __future__ import annotations

import json
import pickle
from abc import ABC, abstractmethod
from enum import Enum, auto
from pathlib import Path
from typing import Any, Optional

import yaml

CONFIG_PATH = "my_file.pickle"


class SaveMode(Enum):
    JSON = auto()
    YAML = auto()
    Pickle = auto()


class AbstractSaver(ABC):
    """
    Abstract product: Save settings into an object
    """

    @abstractmethod
    def get_config(self) -> Any:
        pass

    @abstractmethod
    def set_config(self, data: dict) -> None:
        pass


class JsonSaver(AbstractSaver):
    """
    Concrete product: Save settings into JSON string
    """

    def __init__(self) -> None:
        self.data: Optional[dict] = None

    def get_config(self) -> str:
        return json.dumps(self.data)

    def set_config(self, data: dict) -> None:
        self.data = data


class YamlSaver(AbstractSaver):
    """
    Concrete product: Save settings into YAML string
    """

    def __init__(self) -> None:
        self.data: Optional[dict] = None

    def get_config(self) -> str:
        return yaml.dump(self.data)

    def set_config(self, data: dict) -> None:
        self.data = data


class PickleSaver(AbstractSaver):
    """
    Concrete product: Save settings into PICKLE file
    """

    def __init__(self) -> None:
        self.data: Optional[dict] = None

    def get_config(self) -> Path:
        path = Path(CONFIG_PATH)
        with open(path, "wb") as f:
            pickle.dump(self.data, f)
        return path

    def set_config(self, data: dict) -> None:
        self.data = data


class AbstractSettings(ABC):
    """
    Abstract Factory: Settings
    """

    def __init__(self, setting: dict) -> None:
        self.setting = setting

    @abstractmethod
    def get_saver(self) -> AbstractSaver:
        raise NotImplementedError("This is a factory method. You should implement this!")

    def save_config(self) -> Any:
        raise NotImplementedError("This is a factory method. You should implement this!")


class JsonSettings(AbstractSettings):
    """
    Concrete Factory: Json Settings
    """

    def get_saver(self) -> AbstractSaver:
        return JsonSaver()

    def save_config(self) -> str:
        saver = self.get_saver()
        saver.set_config(self.setting)
        return saver.get_config()


class PickleSettings(AbstractSettings):
    """
    Concrete Factory: Pickle Settings
    """

    def get_saver(self) -> AbstractSaver:
        return PickleSaver()

    def save_config(self) -> Path:
        saver = self.get_saver()
        saver.set_config(self.setting)
        return saver.get_config()


class YamlSettings(AbstractSettings):
    """
    Concrete Factory: Yaml Settings
    """

    def get_saver(self) -> AbstractSaver:
        return YamlSaver()

    def save_config(self) -> str:
        saver = self.get_saver()
        saver.set_config(self.setting)
        return saver.get_config()
