from django.contrib import admin
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'documento_identidad', 'fecha_asistencia', 'hora_ingreso', 'hora_salida', 'presente')
    list_filter = ('presente', 'fecha_asistencia')
    search_fields = ('nombre_completo', 'documento_identidad', 'correo_electronico')
    date_hierarchy = 'fecha_asistencia'
    ordering = ('-fecha_asistencia', '-hora_ingreso')
