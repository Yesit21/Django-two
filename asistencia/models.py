from django.db import models

class Asistencia(models.Model):
    nombre_completo = models.CharField(max_length=150, verbose_name="Nombre completo")
    documento_identidad = models.CharField(max_length=50, verbose_name="Documento de identidad")
    correo_electronico = models.EmailField(verbose_name="Correo electrónico")
    fecha_asistencia = models.DateField(verbose_name="Fecha de asistencia")
    hora_ingreso = models.TimeField(verbose_name="Hora de ingreso")
    hora_salida = models.TimeField(verbose_name="Hora de salida")
    presente = models.BooleanField(default=True, verbose_name="Presente")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    
    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        ordering = ['-fecha_asistencia', '-hora_ingreso']
    
    def __str__(self):
        return f"{self.nombre_completo} - {self.fecha_asistencia}"
