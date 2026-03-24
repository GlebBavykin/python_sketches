import json

import pytest
import yaml

from design_patterns.creational.factory_method_pattern import (
    JsonSaver,
    YamlSaver,
)

TEST_CONFIG = {
    "appName": "MyApp",
    "version": "1.0.0",
    "logging": {"level": "info", "debugMode": True, "filePath": "/var/log/myapp.log"},
    "featuresEnabled": ["featureA", "featureB", "featureC"],
}


@pytest.mark.parametrize(
    "concrete_settings, outcome",
    [
        (JsonSaver, json.dumps),
        (YamlSaver, yaml.dump),
    ],
)
def test_factory_method_pattern(concrete_settings, outcome):
    """
    Test factory method pattern
    """
    assert concrete_settings(TEST_CONFIG).save_config() == outcome(TEST_CONFIG)
