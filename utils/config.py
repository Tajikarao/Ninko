import yaml

from utils.singleton import Singleton


class Config(metaclass=Singleton):
    def __init__(self) -> None:
        self.config_file: str = "config.yaml"
        self.data: dict = self.set_data()

    def set_data(self):
        with open(self.config_file) as f:
            return yaml.safe_load(f)
