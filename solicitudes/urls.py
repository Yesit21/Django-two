from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('', views.solicitud_create, name='create'),
    path('confirm/', views.confirm, name='confirm'),
]
