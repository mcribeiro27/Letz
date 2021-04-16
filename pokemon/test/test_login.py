import requests
import json


def test_authenticate_status():
    
    url = 'http://127.0.0.1:5000/trainer/authenticate'
    headers = {
        'Content-Type': 'application/json',

    }
    payload = {
        "email": "ash@pokemon.com",
        "password": "coxinha123"
    }
    resposta = requests.post(url, headers=headers, data=json.dumps(payload))
    assert resposta.status_code == 200
    response_content = json.loads(resposta.content.decode('utf-8'))
    token = response_content['access_token']
    return token