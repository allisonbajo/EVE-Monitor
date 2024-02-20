import requests
import json


def get_systems(baseUrl, version, server):
    response = requests.get(baseUrl + version + '/universe/systems/?datasource=' + server)
    data = response.json()

    return data

def get_system_info(baseUrl, version, server, systemId):
    response = requests.get(baseUrl + version + '/universe/systems/' + str(systemId))
    data = response.json()

    return data