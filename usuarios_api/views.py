from django.shortcuts import render

from .services.jsonplaceholder import (actualizar_usuario_patch,
                                       actualizar_usuario_put, enviar_usuario)


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
        "usuarios_api/crear_usuario.html",
        contexto,
    )


def actualizar_usuario(request):
    contexto = {}

    if request.method == "POST":
        operacion = request.POST.get("operacion")

        usuario_id = request.POST.get("usuario_id")
        nombre = request.POST.get("nombre")
        username = request.POST.get("username")
        email = request.POST.get("email")

        try:
            if operacion == "put":
                usuario = actualizar_usuario_put(
                    usuario_id=usuario_id,
                    nombre=nombre,
                    username=username,
                    email=email,
                )

            elif operacion == "patch":
                usuario = actualizar_usuario_patch(
                    usuario_id=usuario_id,
                    email=email,
                )

            else:
                contexto["error"] = (
                    "Operación no válida."
                )
                return render(
                    request,
                    "usuarios_api/actualizar_usuario.html",
                    contexto,
                )

            contexto["usuario"] = usuario
            contexto["operacion"] = operacion

        except Exception as error:
            print(f"Error al consumir la API: {error}")

            contexto["error"] = (
                "No fue posible actualizar el usuario."
            )

    return render(
        request,
        "actualizar_usuario.html",
        contexto,
    )
