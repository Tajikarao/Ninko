import requests
import re

class Webresolver:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.base_url: str = "https://webresolver.nl"

        self.endpoints: dict = {
            "geoip": "ajax/tools/geoip"
        }

    
    def get_domaine_geoip(self, domaine: str):
        solver_parse: dict = {}

        headers = {
            'referer': 'https://webresolver.nl/tools/geoip',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'action': 'PostData',
            'string': domaine,
        }

        webresolver = requests.post('https://webresolver.nl/ajax/tools/geoip', headers=headers, data=data).text.split("<br />")

        for solved in webresolver:
            try:
                solved_title = re.search('<b>(.*):</b>', solved).group(1)
                if solved_title:
                    solved_content = solved.split('</b>')[1]
                    if solved_content:
                        specials = ["Country", "Continent"]
                        if solved_title in specials:
                            solved_content = re.search('> (.*)', solved_content).group(1)

                        solved_title = ' '.join(filter(None, solved_title.split(' ')))
                        solved_content = ' '.join(filter(None, solved_content.split(' ')))
                        solver_parse.update({solved_title: solved_content})
            except:
                pass

        return solver_parse