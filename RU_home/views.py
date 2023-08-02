from django.shortcuts import render
from django.http import HttpResponse

def ver_cardapio(request):
    return HttpResponse('Estou no Cardápio');

def ver_pedidos(request):
    return render(request, 'ver_pedido.html')
