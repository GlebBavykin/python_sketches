import json

import pytest
import yaml

from design_patterns.creational.factory_method_pattern import (JsonSettings,
                                                               YamlSettings)

TEST_CONFIG = {
    "appName": "MyApp",
    "version": "1.0.0",
    "logging": {"level": "info", "debugMode": True, "filePath": "/var/log/myapp.log"},
    "featuresEnabled": ["featureA", "featureB", "featureC"],
}


@pytest.mark.parametrize(
    "concrete_settings, save_outcome",
    [
        (JsonSettings(TEST_CONFIG), json.dumps(TEST_CONFIG)),
        (YamlSettings(TEST_CONFIG), yaml.dump(TEST_CONFIG)),
    ],
)
def test_factory_method_pattern(concrete_settings, save_outcome):
    """
    Test factory method pattern
    """
    assert concrete_settings.save_config() == save_outcome
