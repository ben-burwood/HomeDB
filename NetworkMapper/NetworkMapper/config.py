import os

CONFIG_FILE_NAME = "data.yaml"


def generate_config_file(filepath):
    if not os.path.exists(filepath):
        with open(filepath, "w") as yaml_file:
            pass
