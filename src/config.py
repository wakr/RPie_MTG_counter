import json

from logic.utils import resolve_relative_path

config_data = None

with open(resolve_relative_path(__file__, './config.json')) as f:
    config_data = json.loads(f.read())
