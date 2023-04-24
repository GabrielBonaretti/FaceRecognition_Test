import requests
import datetime
import json


def api(nome_face):
    url = "https://interclasse.azurewebsites.net/api/v1/atletas/searchimage"

    dados = {"nome_imagem": f"{nome_face}", "horario": "123"}

    response = requests.post(url, json=dados)

    print(response.status_code)
