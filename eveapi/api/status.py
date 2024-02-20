import requests
import json


def get_status(baseUrl, version, server):
    response = requests.get(baseUrl + version + '/status/?datasource=' + server)
    data = response.json()

    return data

