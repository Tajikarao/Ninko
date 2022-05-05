import json

import yaml

from utils.config import Config
from utils.singleton import Singleton


class Database(metaclass=Singleton):
    def __init__(self) -> None:
        self.config = Config()
        self.tld = self.init_tld()

    def init_tld(self):
        with open(self.config.data["database"]["TLD"]) as TLD:
            return self.yaml_to_json(TLD)

    def update_tld(self, domaine):
        self.tld = self.init_tld()
        self.tld["domaines"][domaine] = []

        yaml.dump(
            self.tld,
            open(self.config.data["database"]["TLD"], "w+"),
            default_flow_style=False,
        )

    def update_tld_ip(self, domaine, ip):
        self.tld = self.init_tld()

        current_ip_list = self.tld["domaines"][domaine].append(ip)

        yaml.dump(
            self.tld,
            open(self.config.data["database"]["TLD"], "w+"),
            default_flow_style=False,
        )

    def is_not_present_in_tld(self, domaine):
        if domaine in self.tld["domaines"]:
            return False

        return True

    def is_ip_present_in_tld(self, domaine, ip):
        if domaine in self.tld["domaines"]:
            if ip in self.tld["domaines"][domaine]:
                return True

        return False

    def yaml_to_json(self, yamlF):
        return yaml.safe_load(yamlF)
