import yaml
import os

EMPTY = """- null"""

def _check_syntax(content: str) -> bool:
    """must not use '-'\n
    must not use '#'\n
    must use ':'"""
    error = True
    for line in content.splitlines():
        if line.count(":") and not line.count("-") and not line.count("#"):
            error = False
    return not error

class config:
    def __init__(self, filepath: str):
        self.file = filepath


    def _update(self):
        with open(self.file, "r") as read_file:
            content = read_file.read().replace(EMPTY, "")
            content = content.replace("''\n", "")
        with open(self.file, "w") as file:
            file.write(content)

    def _load(self) -> (dict | None):
        with open(self.file, "r") as file:
            return yaml.safe_load(file)

    def _write(self, data: dict, mode: str = "a"):
        "must check the syntax before write it"
        with open(self.file, mode) as file:
            yaml.safe_dump(data, file)


    def find(self, config_name: str) -> bool:
        if os.path.isfile(self.file):
            content = self._load()
            if content is not None: #"https://stackoverflow.com/questions/23086383/how-to-test-nonetype-in-python"
                return config_name in content #True | False
        return False

    def add(self, config: str):
        """Don't use '-' and '#'\n
        Currently you can only give 1 main item with 1 value\n
        Automatically creates a file if it doesn't exist"""

        if not _check_syntax(config):
            return False

        if os.path.isfile(self.file):
            mode = "a"
        else:
            mode = "w"

        try:
            data = yaml.safe_load(config)
            self._write(data, mode)
            self._update()
        except Exception as error:
            print(error)
            return False

        return True

    def remove(self, config_name: str):
        if self.find(config_name):
            content = self._load()
            content.pop(config_name)
            if len(content) > 0:
                self._write(content, "w")
            else:
                self._write(EMPTY, "w")

    def change(self, config_name: str, new_value: str | bool):
        if self.find(config_name):
            data = self._load()
            data[config_name] = new_value
            self._write(data, "w")

    def get_value(self, config_name: str) -> (dict | None):
        "if file or item is not found then return None"
        if self.find(config_name):
            return self._load().get(config_name)
        else:
            return