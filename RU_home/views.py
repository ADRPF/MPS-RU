from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def ver_cardapio(request):
    return HttpResponse('Estou no Cardápio')

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

