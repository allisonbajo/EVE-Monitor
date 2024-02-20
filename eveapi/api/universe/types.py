import requests
import json


def get_types(baseUrl, version, server):
    response = requests.get(baseUrl + version + '/universe/types/?datasource=' + server)
    data = response.json()

    return data

def get_system_info(baseUrl, version, server, typeId):
    response = requests.get(baseUrl + version + '/universe/types/' + str(typeId))
    data = response.json()

    return data