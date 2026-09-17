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


def actualizar_usuario_put(usuario_id, nombre, username, email):
    url = f"{JSONPLACEHOLDER_URL}/{usuario_id}"

    payload = {
        "name": nombre,
        "username": username,
        "email": email,
    }

    response = requests.put(
        url,
        json=payload,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


def actualizar_usuario_patch(usuario_id, email):
    url = f"{JSONPLACEHOLDER_URL}/{usuario_id}"

    payload = {
        "email": email,
    }

    response = requests.patch(
        url,
        json=payload,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()
