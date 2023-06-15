import json
from os import path

config_file = open(
    path.join(path.dirname(__file__), "../dict/http-error.json"),
    "r"
)

error_config = json.load(config_file)

config_file.close()
