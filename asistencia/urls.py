from django.urls import path
from . import views

app_name = 'asistencia'

urlpatterns = [
    path('', views.registro_asistencia, name='registro'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
]
