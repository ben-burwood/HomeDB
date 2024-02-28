from typing import Any

import yaml
from django.conf import settings

def get_config_value(key: str, default: Any) -> str:
    with open(settings.CONFIG_FILE_PATH, "r") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file) or {}
    return yaml_data.get(key, default)


def update_config_value(key: str, value: str) -> None:
    with open(settings.CONFIG_FILE_PATH, "r+") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file) or {}
        yaml_data[key] = value
        yaml_file.seek(0)
        yaml.dump(yaml_data, yaml_file)
        yaml_file.truncate()
