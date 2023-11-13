from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        config = toml.loads(content)

        #print(content)

        authors = []
        for a in config['tool']['poetry']['authors']:
            authors.append(f"- {a}")

        dependencies = []
        for d in config['tool']['poetry']['dependencies']:
            dependencies.append(f"- {d}")
        
        dev_dependencies = []
        for dd in config['tool']['poetry']['group']['dev']['dependencies']:
            dev_dependencies.append(f"- {dd}")
        #print(config['tool']['poetry']['name'])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(config['tool']['poetry']['name'], config['tool']['poetry']['description'], config['tool']['poetry']['license'], authors, dependencies, dev_dependencies)
