from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("clima.urls")),
    path("usuarios/", include("usuarios_api.urls")),
]