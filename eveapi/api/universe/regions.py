import requests
import json


def get_regions(baseUrl, version, server):
    response = requests.get(baseUrl + version + '/universe/regions/?datasource=' + server)
    data = response.json()

    return data

def get_region_info(baseUrl, version, server, regionId):
    response = requests.get(baseUrl + version + '/universe/regions/' + str(regionId))
    data = response.json()

    return data