import json
import pickle
from pathlib import Path
from typing import Optional

import pytest

from design_pattern.creational.factory import Settings, Saver

TEST_CONFIG = dict(a=1, b=2, c=3)
CONFIG_PATH = "my_file.pickle"


class JsonSaver(Saver):
    """
        Save settings into JSON
    """
    def __init__(self):
        self.data: Optional[dict] = None

    def save(self) -> str:
        return json.dumps(self.data)

    def set_config(self, data: dict) -> None:
        self.data = data


class PickleSaver(Saver):
    """
        Save settings into pickle file
    """
    def __init__(self):
        self.data: Optional[dict] = None

    def save(self) -> Path:
        path = Path(CONFIG_PATH)
        with open(path, 'wb') as f:
            pickle.dump(self.data, f)
        return path

    def set_config(self, data: dict) -> None:
        self.data = data


@pytest.fixture(scope="class")
def settings() -> Settings:
    """
        Setting instance
    """
    return Settings(TEST_CONFIG)


@pytest.mark.parametrize("saver, outcome", [
    (JsonSaver(), json.dumps(TEST_CONFIG)),
    (PickleSaver(), Path(CONFIG_PATH)),
])
def test_create_two_instances(settings: Settings, saver: Saver, outcome):
    """
        Setting different savers to one setting instance
    """
    settings.set_factory_method(saver)
    assert settings.save_config() == outcome
