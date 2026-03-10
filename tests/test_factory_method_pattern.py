import json
from pathlib import Path

import pytest
import yaml

from design_pattern.creational.factory_method_pattern import JsonSettings, YamlSettings, PickleSettings

TEST_CONFIG = dict(a=1, b=2, c=3)
CONFIG_PATH = "my_file.pickle"


@pytest.mark.parametrize("concrete_settings, outcome", [
    (JsonSettings(TEST_CONFIG), json.dumps(TEST_CONFIG)),
    (YamlSettings(TEST_CONFIG), yaml.dump(TEST_CONFIG)),
    (PickleSettings(TEST_CONFIG), Path(CONFIG_PATH)),
])
def test_factory_method_pattern(concrete_settings, outcome):
    """
        Test factory method pattern
    """
    assert concrete_settings.save_config() == outcome
