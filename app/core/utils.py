import json
import os


def get_configs_as_dictionary() -> dict:
    """
    Return the config file as dictionary object.

    Returns:
        dict: The config file as dict
    """
    config_file_path = os.path.abspath('config.json')
    with open(config_file_path) as config_file:
        return json.loads(config_file.read())
