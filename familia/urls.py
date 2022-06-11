
from django.urls import path

from familia import views


urlpatterns = [
    path('', views.index, name="index"),
    path('agregar/', views.agregar, name="agregar"),
    path('listado/', views.listado, name="listado"),
  
]