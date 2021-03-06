import contextlib
import re

import requests

from utils.config import Config


class Webresolver:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.config = Config()
        self.base_url: str = "https://webresolver.nl"

    def get_old_domaine_ip_list(self, domaine: str):
        ip_history = self.session.get(
            f"{self.base_url}/api.php?key={self.config.data['webresolver_key']}&json&action=domaininfo&string={domaine}"
        ).json()["ip_history"]

        return [selector["ip_address"] for selector in ip_history]
