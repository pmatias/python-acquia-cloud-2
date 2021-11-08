import json
from typing import Dict


def load_fixture(path: str) -> Dict:
    """Load fixture from a json-file.

    :param path: path to the file
    :return: formatted dict
    """
    with open(path) as f:
        result = f.read()
    return json.loads(result)
