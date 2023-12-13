import json


def saveDict(path: str, data: dict) -> None:
    """saves a dictionary or a list of hashable objects to a json file at the specified path"""

    with open(path, "w") as json_file:
        json.dump(data, json_file)


def readDict(path: str) -> dict | list:
    """loads a json file from provided path and return it as a dictionary"""

    with open(path, "r") as json_file:
        try:
            return json.load(json_file)
        except:
            print("error in loading file")
            return {}
