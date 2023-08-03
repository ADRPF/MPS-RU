from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def ver_cardapio(request):
    return HttpResponse('Estou no Cardápio')

def ver_pedidos(request):
    if request.method == "GET":
        nome = 'Amós'
        return render(request, 'ver_pedido.html', {'nome':nome})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        pessoa = Pessoa(nome=nome, matricula=matricula)
        pessoas = Pessoa.objects.all()
        pessoas2 = Pessoa.objects.filter(nome=nome)
        if pessoas2.exists():
            print("Usuário já cadastrado")
        else:
            print("Usuário cadastrado")
        print(pessoas[0].idade)
        #print(pessoas)
        pessoa.save()
        return HttpResponse(pessoas)

