from django.urls import path
from . import views


urlpatterns = [
    path('menu/', views.menu_vista, name='menu'),
    path('registro_comensal/', views.registro_comensal, name='registro_comensal'),
    path('listar_comensales/', views.listar_comensales, name='listar_comensales'),
    path('listar_comensales/registro_comensal/', views.registro_comensal, name='listar_comensales_registro'),
    path('registro_comensal/listar_comensales/', views.listar_comensales, name='registro_listar_comensales'),
    path('registro_comensal/listar_comensales/registro_comensal/', views.registro_comensal, name='registro_listar_y_registro_comensal'),
    path('registrar_mesa/', views.registrar_mesa, name='registrar_mesa'),
    path('listar_mesas/', views.listar_mesas, name='listar_mesas'),
    path('registrar_mesa/listar_mesas/', views.listar_mesas, name='registrar_listar_mesas'),
    path('registrar_mesa/listar_mesas/registrar_mesa/', views.registrar_mesa, name='registrar_listar_mesas'),
    path('crear_reserva/', views.crear_reserva, name='crear_reserva'),
    path('listar_reservas/', views.listar_reservas, name='listar_reservas'),
     path('listar_reservas/crear_reserva/', views.crear_reserva, name='crear_reserva'),
   
]
