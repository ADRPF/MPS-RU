from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa
from .models import Pedido
from .models import Prato
import datetime

def ver_cardapio(request):
    return render(request, 'cardapio.html')

def pedido(request):
    if request.method == 'POST':
        prato = Prato.objects.filter(request.method.POST.get('prato-id'))

        valor = request.POST.get('valor')
        formPag = 'cred'
        senha = '1012'

        if(Pedido.objects.filter(senha=senha)):
            return HttpResponse("Pedido com senha repetida")

        pedido = Pedido(valor=valor, senha=senha, formPag=formPag)
        pedido.save()

        #prato = Prato.objects.filter(nome='Teste 1')
        return HttpResponse(pedido.numPedido)



def logar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        print(nome, senha)
        pessoa = Pessoa.objects.filter(nome=nome, senha=senha)
        if pessoa.exists():
            print("Usuário Cadastrado")
            return render(request, 'index.html')
        else:
            print("Não existe esse usuário")
    return render(request, 'pagina_login.html')

def index(request):
    return render(request, 'index.html')

def cadastrar_aluno(request):
    if request.method == "GET":
        nome = 'Amós'
        return render(request, 'pagina_cadastro.html', {'nome':nome})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')
        pessoa = Pessoa(nome=nome, matricula=matricula, senha=senha)
        pessoas = Pessoa.objects.all()
        pessoas2 = Pessoa.objects.filter(nome=nome)
        if pessoas2.exists():
            print("Usuário já cadastrado")
        else:
            print("Usuário cadastrado")
        print(pessoas[0].matricula)
        #print(pessoas)
        pessoa.save()
        #return HttpResponse(pessoas)
        return render(request, 'pagina_login.html')

