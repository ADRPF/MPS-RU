from django.urls import path
from . import views
from Feedback import views as fviews

urlpatterns = [
    path('cardapio/', views.ver_cardapio, name="ver_cardapio"),
    path('cardapio/pedido/', views.pedido, name="fazer_pedido"),
    path('cadastro/', views.cadastrar_aluno, name="cadastrar_aluno"),
    path('login/', views.logar, name="logar"),
    path('inicio/', views.index, name="inicio"),
    path('feedback/', fviews.ver_feedback, name="escrever_feedback")
]