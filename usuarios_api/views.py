from django.shortcuts import render

from .services.jsonplaceholder import enviar_usuario


def crear_usuario(request):
    contexto = {}

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        username = request.POST.get("username")
        email = request.POST.get("email")

        try:
            usuario = enviar_usuario(
                nombre=nombre,
                username=username,
                email=email,
            )

            contexto["usuario"] = usuario

        except Exception as error:
            print(f"Error al consumir la API: {error}")

            contexto["error"] = (
                "No fue posible crear el usuario."
            )

    return render(
        request,
        "crear_usuario.html",
        contexto,
    )
