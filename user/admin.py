from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import User

# Configuración del panel de administración
admin.site.site_header = "Administración de Usuarios"
admin.site.site_title = "Usuarios"
admin.site.index_title = "Panel de Administración"

# Registrar el modelo User en el panel de administración
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Redes sociales', {'fields': ('website',)}),
    )
