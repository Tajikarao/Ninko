import yaml

from utils.config import Config
from utils.singleton import Singleton


class Database(metaclass=Singleton):
    def __init__(self) -> None:
        self.config = Config()
        self.tld = self.init_tld()
        self.tld_infos = self.init_tld_infos()

    def init_tld(self):
        with open(self.config.data["database"]["TLD"]) as TLD:
            return self.yaml_to_json(TLD)

    def init_tld_infos(self):
        with open(self.config.data["database"]["TLD_infos"]) as TLD_infos:
            return self.yaml_to_json(TLD_infos)

    def yaml_to_json(self, yamlF):
        return yaml.safe_load(yamlF)
