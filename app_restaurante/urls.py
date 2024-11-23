from django.urls import path
from . import views


urlpatterns = [
    path('menu/', views.menu_vista, name='menu'),
    path('registro_comensal/', views.registro_comensal, name='registro_comensal'),
    path('listar_comensales/', views.listar_comensales, name='listar_comensales'),
    path('listar_comensales/registro_comensal/', views.registro_comensal, name='listar_comensales_registro'),
    path('registro_comensal/listar_comensales/', views.listar_comensales, name='registro_listar_comensales'),
    path('registro_comensal/listar_comensales/registro_comensal/', views.registro_comensal, name='registro_listar_y_registro_comensal'),
    path('eliminar_comensal/<int:cedula>/', views.eliminar_comensal, name='eliminar_comensal'),
]
