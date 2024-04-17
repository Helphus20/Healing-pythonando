from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, "cadastro.html") #vai direto para a pasta templates
    elif request.method == 'POST':
        return HttpResponse('TÔ TESTANDO CALAIO')
