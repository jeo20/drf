from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("clima.urls")),
    path("usuarios/", include("usuarios_api.urls")),
    path("actualizar/", views.actualizar_usuario, name="actualizar_usuario"),
]
