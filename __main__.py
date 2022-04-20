from utils.webresolver import Webresolver 

if __name__ == "__main__":
    webresolver = Webresolver()
    geoip = webresolver.get_domaine_geoip("https://www.nandesuka.moe/")
    print(geoip)
