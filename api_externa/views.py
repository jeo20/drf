import requests
from django.shortcuts import render


def usuarios(request):
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    usuarios = response.json()

    return render(
        request,
        "usuarios.html",
        {
            "usuarios": usuarios,
        },
    )
