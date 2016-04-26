"""Tests for compare module."""
import pytest
from nelkit.exceptions import NelkitException
from nelkit.modules.compare_configs.settings import CompareConfigs


BASE_DIR = 'tests/modules/compare_configs/data/'
BASE_RULES = 'tests/modules/compare_configs/data/base_rules.yml'


def test_base_function():
    """Basic test of the compare module, and check that no exceptions are raised."""
    CompareConfigs(settings_file=BASE_RULES)
    assert True


def test_invalid_config_between_missing_start():
    """Fail when loading a yaml file without a start key."""
    with pytest.raises(NelkitException) as excinfo:
        CompareConfigs(settings_file='%s/invalid_rule_between_missing_start.yml' % BASE_DIR)
    assert 'start key missing in between rule' == str(excinfo.value)
