from django.urls import path
from . import views

urlpatterns = [
    path('cardapio/', views.ver_cardapio, name="ver_cardapio"),
    path('pedidos/', views.ver_pedidos, name="ver_pedidos")
]