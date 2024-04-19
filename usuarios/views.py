from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html") #vai direto para a pasta templates
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if (len(senha) < 6):
            return redirect('usuarios/cadastro')
            if(senha != confirmar_senha):
                print('Erro 1334 - as senhas não são iguais')
                return redirect('/usuarios/cadastro')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )

        return HttpResponse(f'Usuário criado com sucesso!')
