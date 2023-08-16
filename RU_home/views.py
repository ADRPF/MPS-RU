from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
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
        user = authenticate(request, username=nome, password=senha)
        pessoa = Pessoa.objects.filter(nome=nome, senha=senha)
        if user is not None:
            login(request, user)
            return redirect('Feedback:ver_feedback')
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

        if not User.objects.filter(username=nome).exists():
            user = User.objects.create_user(username=nome, password=senha)
            user.save()
            print("Usuário cadastrado")
            return render(request, 'pagina_login.html')
        else:
            print("Usuário já cadastrado")
    return render(request, 'pagina_cadastro.html')
def fazer_logout(request):
    logout(request)
    return redirect('logar')

