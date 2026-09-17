import requests

JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/users"


def enviar_usuario(nombre, username, email):
    payload = {
        "name": nombre,
        "username": username,
        "email": email,
    }

    response = requests.post(
        JSONPLACEHOLDER_URL,
        json=payload,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()