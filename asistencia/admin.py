from django.contrib import admin
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'documento_identidad', 'fecha_asistencia', 'hora_ingreso', 'hora_salida', 'presente', 'get_duracion')
    list_filter = ('presente', 'fecha_asistencia', 'hora_ingreso')
    search_fields = ('nombre_completo', 'documento_identidad', 'correo_electronico')
    date_hierarchy = 'fecha_asistencia'
    ordering = ('-fecha_asistencia', '-hora_ingreso')
    list_per_page = 25
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre_completo', 'documento_identidad', 'correo_electronico')
        }),
        ('Información de Asistencia', {
            'fields': ('fecha_asistencia', 'hora_ingreso', 'hora_salida', 'presente')
        }),
        ('Observaciones', {
            'fields': ('observaciones',),
            'classes': ('collapse',)
        }),
    )
    
    def get_duracion(self, obj):
        """Calcula la duración de la asistencia"""
        if obj.hora_ingreso and obj.hora_salida:
            from datetime import datetime, timedelta
            ingreso = datetime.combine(datetime.today(), obj.hora_ingreso)
            salida = datetime.combine(datetime.today(), obj.hora_salida)
            duracion = salida - ingreso
            horas = duracion.seconds // 3600
            minutos = (duracion.seconds % 3600) // 60
            return f"{horas}h {minutos}m"
        return "-"
    get_duracion.short_description = 'Duración'
    
    def has_add_permission(self, request):
        """Permite agregar registros desde el admin"""
        return True
    
    def has_delete_permission(self, request, obj=None):
        """Permite eliminar registros"""
        return True
    
    def has_change_permission(self, request, obj=None):
        """Permite editar registros"""
        return True

# Personalización del sitio de administración
admin.site.site_header = "Universidad Cooperativa de Colombia"
admin.site.site_title = "Sistema de Gestión Académica"
admin.site.index_title = "Panel de Administración - Asistencias"
