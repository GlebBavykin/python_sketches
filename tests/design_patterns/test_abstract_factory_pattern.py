import json
from pathlib import Path

import pytest
import yaml

from design_patterns.creational.abstract_factory_pattern import (
    CONFIG_PATH, AbstractSettings, JsonSettings, PickleSettings, SaveMode,
    YamlSettings)

TEST_CONFIG = {
    "appName": "MyApp",
    "version": "1.0.0",
    "logging": {"level": "info", "debugMode": True, "filePath": "/var/log/myapp.log"},
    "featuresEnabled": ["featureA", "featureB", "featureC"],
}


@pytest.mark.parametrize(
    "save_mode, outcome",
    [
        (SaveMode.JSON, json.dumps(TEST_CONFIG)),
        (SaveMode.YAML, yaml.dump(TEST_CONFIG)),
        (SaveMode.Pickle, Path(CONFIG_PATH)),
    ],
)
@pytest.mark.parametrize("settings", [AbstractSettings])
def test_abstract_factory_method_pattern(settings, save_mode, outcome):
    """
    Test abstract factory pattern
    """
    if save_mode == SaveMode.JSON:
        settings = JsonSettings(TEST_CONFIG)
    elif save_mode == SaveMode.YAML:
        settings = YamlSettings(TEST_CONFIG)
    elif save_mode == SaveMode.Pickle:
        settings = PickleSettings(TEST_CONFIG)
    assert settings.save_config() == outcome
