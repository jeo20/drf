from django.contrib import admin
from django.urls import include, path

from api_externa.views import usuarios

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api_externa/usuarios/", usuarios, name="usuarios"),
]
