from django.shortcuts import render

from .services.open_meteo import obtener_clima


def clima(request):
    contexto = {}

    if request.method == "POST":
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        try:
            data = obtener_clima(latitude, longitude)

            contexto["clima"] = data["current"]

        except Exception:
            contexto["error"] = "No fue posible obtener los datos del clima."

    return render(
        request,
        "clima.html",
        contexto,
    )