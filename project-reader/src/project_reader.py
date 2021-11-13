from urllib import request
from project import Project
from d8s_toml import *


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        
        decoded = toml_read(content)
        decoded_data = decoded['tool']['poetry']
        name = decoded_data['name']
        description = decoded_data['description']
        dependencies = decoded_data['dependencies']
        dev_dependencies = decoded_data['dev-dependencies']
    

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
