import re
import socket
from urllib.parse import urlparse

import httpx

from services.webresolver import Webresolver
from utils.database import Database


class Crawler:
    def __init__(self) -> None:
        self.webresolver = Webresolver()
        self.database = Database()
        self.session = httpx.Client(http2=True, headers={"user-agent": "Ninka"})
        self.queue = []

    def get_queue(self):
        return self.queue

    def process_page(self, url):
        content = self.session.get(url).text
        urls = re.findall(
            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            content,
        )
        self.process_domaines(urls)

    def process_domaines(self, urls):
        for url in urls:
            if domaine := urlparse(url).netloc:
                ip_list = []
                if self.database.is_not_present_in_tld(domaine):
                    self.database.update_tld(domaine)
                    ip_list.extend(self.webresolver.get_old_domaine_ip_list(domaine))

                ip_list.append(socket.gethostbyname(domaine))

                for ip in ip_list:
                    if not self.database.is_ip_present_in_tld(domaine, ip):
                        self.database.update_tld_ip(domaine, ip)

    def start(self):
        self.process_page("https://nyaa.si/")
