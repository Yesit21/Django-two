from django.db import models


class Solicitud(models.Model):
    TIPO_ACADEMICA = 'academica'
    TIPO_ADMINISTRATIVA = 'administrativa'
    TIPO_TECNICA = 'tecnica'
    TIPO_OTRA = 'otra'

    TIPO_CHOICES = [
        (TIPO_ACADEMICA, 'Académica'),
        (TIPO_ADMINISTRATIVA, 'Administrativa'),
        (TIPO_TECNICA, 'Técnica'),
        (TIPO_OTRA, 'Otra'),
    ]

    nombre_solicitante = models.CharField("Nombre del solicitante", max_length=150)
    documento = models.CharField("Documento de identidad", max_length=50)
    email = models.EmailField("Correo electrónico")
    telefono = models.CharField("Teléfono de contacto", max_length=30, blank=True)
    tipo_solicitud = models.CharField("Tipo de solicitud", max_length=20, choices=TIPO_CHOICES)
    asunto = models.CharField("Asunto", max_length=200)
    descripcion = models.TextField("Descripción detallada")
    fecha_solicitud = models.DateField("Fecha de la solicitud")
    archivo_adj = models.FileField("Archivo adjunto", upload_to='solicitudes/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.asunto}"
