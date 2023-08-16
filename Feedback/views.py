from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from RU_home.models import Pessoa

@login_required
def ver_feedback(request):
    return render(request, 'pagina_feedback.html')