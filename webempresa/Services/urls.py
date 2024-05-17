from django.urls import path
from .import views

urlpatterns = [
    # Paths del servicio
    path('', views.services, name="services"),
]
