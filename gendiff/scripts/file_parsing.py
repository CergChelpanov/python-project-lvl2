import json
import yaml


def parse_file(filepath: str) -> tuple:
    try:
        if filepath.endswith(".json"):
            return json.load(open(filepath)), "OK"
        if filepath.endswith('.yaml') or filepath.endswith('.yml'):
            return yaml.load(open(filepath), Loader=yaml.FullLoader), "OK"
    except (FileExistsError, FileNotFoundError) as error:
        return error, f"An error occurred: {error}"
    return "Unsupported file type", ""
