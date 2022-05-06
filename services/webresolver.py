import re

import requests


class Webresolver:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.base_url: str = "https://webresolver.nl"

        self.endpoints: dict = {"geoip": "ajax/tools/geoip"}

    def get_domaine_geoip(self, domaine: str):
        """
        Here we do not use the API because to use it we need to register,
        which is not the case here. Moreover the geoip route does not seem to be limited in the number of attempts / seconds.
        Be careful not to abuse it before having done more tests.
        """
        solver_parse: dict = {}

        headers = {
            "referer": "https://webresolver.nl/tools/geoip",
            "x-requested-with": "XMLHttpRequest",
        }

        data = {
            "action": "PostData",
            "string": domaine,
        }

        webresolver = requests.post(
            f'{self.base_url}/{self.endpoints["geoip"]}', headers=headers, data=data
        ).text.split("<br />")

        for solved in webresolver:
            try:
                if solved_title := re.search("<b>(.*):</b>", solved)[1]:
                    if solved_content := solved.split("</b>")[1]:
                        specials = ["Country", "Continent"]
                        if solved_title in specials:
                            solved_content = re.search("> (.*)", solved_content)[1]

                        solved_title = " ".join(filter(None, solved_title.split(" ")))
                        solved_content = " ".join(
                            filter(None, solved_content.split(" "))
                        )
                        solver_parse[solved_title] = solved_content
            except:
                pass

        return solver_parse
