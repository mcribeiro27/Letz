import requests
import json


def test_authenticate():
    
    url = 'http://127.0.0.1:5000/trainer/authenticate'
    headers = {
        'Content-Type': 'application/json',

    }
    payload = {
        "email": "ash@pokemon.com",
        "password": "coxinha123"
    }
    resposta = requests.post(url, headers=headers, data=json.dumps(payload))
    response_content = json.loads(resposta.content.decode('utf-8'))
    token = response_content['access_token']
    return token

token = test_authenticate()

def test_post_status():
    
    
    url = 'http://127.0.0.1:5000/trainer/1/pokemon'
    headers = {
        'Content-Type': 'application/json',
        'Authorization':'Bearer ' + token
    }
    payload = {
        "name": "Fluffy",
        "level": 4,
        "pokemon_id": 12
    }
    resposta = requests.post(url, headers=headers, data=json.dumps(payload))
    assert resposta.status_code == 201

def test_get_status():
    headers = {
        'Content-Type': 'application/json'
    }
    url = 'http://127.0.0.1:5000/trainer/1/pokemon'

    resposta = requests.get(url, headers=headers)
    assert resposta.status_code == 200

def test_get_by_id_status():
    headers = {
        'Content-Type': 'application/json'
    }
    url = 'http://127.0.0.1:5000/trainer/1/pokemon/1'

    resposta = requests.get(url, headers=headers)
    assert resposta.status_code == 200

def test_delete_status():

    headers = {
        'Content-Type': 'application/json',
        'Authorization':'Bearer ' + token
    }
    url = 'http://127.0.0.1:5000/trainer/1/pokemon/1'

    resposta = requests.delete(url, headers=headers)
    assert resposta.status_code == 200