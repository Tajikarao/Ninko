from services.webresolver import Webresolver
from utils.database import Database

import httpx
import re


class Crawler:
    def __init__(self) -> None:
        self.webresolver = Webresolver()
        self.database = Database()
        self.session = httpx.Client(http2=True, headers={'user-agent': 'Ninka'})

    def process_page(self, url):
        content = self.session.get(url).text
        urls = re.findall(r'^(?:_|\*\.)?[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$', content)
        print(urls)

    def start(self):
        print(self.database.config.data)
        print(self.database.tld)
        print(self.database.tld_infos)
        self.process_page("https://nyaa.si/")
