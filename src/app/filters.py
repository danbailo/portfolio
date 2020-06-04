import json


def render_json(path_to_file):
    with open(path_to_file) as file:
        json_file = json.load(file)
    return json_file