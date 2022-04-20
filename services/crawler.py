from services.webresolver import Webresolver
from utils.database import Database


class Crawler:
    def __init__(self) -> None:
        self.webresolver = Webresolver()
        self.database = Database()

    def start(self):
        print(self.database.config.data)
        print(self.database.tld)
        print(self.database.tld_infos)
