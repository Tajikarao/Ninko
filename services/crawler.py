import re
from urllib.parse import urlparse

import httpx

from services.webresolver import Webresolver
from utils.database import Database


class Crawler:
    def __init__(self) -> None:
        self.webresolver = Webresolver()
        self.database = Database()
        self.session = httpx.Client(http2=True, headers={"user-agent": "Ninka"})

    def process_page(self, url):
        content = self.session.get(url).text
        urls = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", content)
        self.process_domaines(urls)

    def process_domaines(self, urls):
        for url in urls:
            domaine = urlparse(url).netloc
            if domaine:
                if not self.database.is_present_in_tld(domaine):
                    pass  # TODO: add in tld yaml

                ip_list = []  # TODO: get list of all ips find for this domaine

                for ip in ip_list:
                    if not self.database.is_present_in_tld_infos(domaine, ip):
                        pass  # TODO: add in tld yaml

    def start(self):
        print(self.database.config.data)
        print(self.database.tld)
        print(self.database.tld_infos)
        self.process_page("https://nyaa.si/")
