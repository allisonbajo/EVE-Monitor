import requests
import json


def get_constellations(baseUrl, version, server):
    response = requests.get(baseUrl + version + '/universe/constellations/?datasource=' + server)
    data = response.json()

    return data

def get_constellation_info(baseUrl, version, server, constellationId):
    response = requests.get(baseUrl + version + '/universe/constellations/' + str(constellationId))
    data = response.json()

    return data