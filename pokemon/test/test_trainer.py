import requests
import json


def test_post_status():
    url = 'http://127.0.0.1:5000/trainer/'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "nickname": "ash",
        "first_name": "Ash",
        "last_name": "Kutchum",
        "email": "ash@pokemon.com",
        "password": "coxinha123",
        "team": "Team Valor"
    }
    resposta = requests.post(url, headers=headers, data=json.dumps(payload))
    assert resposta.status_code == 200

def test_get_status():
    headers = {
        'Content-Type': 'application/json'
    }
    url = 'http://127.0.0.1:5000/trainer/'

    resposta = requests.get(url, headers=headers)
    assert resposta.status_code == 200

def test_get_by_id_status():
    headers = {
        'Content-Type': 'application/json'
    }
    url = 'http://127.0.0.1:5000/trainer/1'

    resposta = requests.get(url, headers=headers)
    assert resposta.status_code == 200

def test_delete_status():
    headers = {
        'Content-Type': 'application/json'
    }
    url = 'http://127.0.0.1:5000/trainer/2'

    resposta = requests.delete(url, headers=headers)
    assert resposta.status_code == 200
