from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib.messages import add_message
from django.contrib import messages
from django.contrib import auth

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
            messages.add_message(request, constants.ERROR, 'A senha deve possuir pelo menos 6 dígitos')
            return redirect('cadastro') #direcionando com o name em vez do caminho da url

        if(senha != confirmar_senha):
            print('Erro 1334 - as senhas não são iguais')
            messages.add_message(request, constants.ERROR, 'As senhas digitadas não são iguais')
            return redirect('cadastro')

        users = User.objects.filter(username=username) #verifica se o nome do usuário já existe na db

        if users.exists():
            messages.add_message(request, constants.ERROR, 'Este usuário já existe, escolha outro nome de usuário')
            return redirect('cadastro')

        #cria os atributos no banco através e os preenche com os dados do formulário
        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )
        return redirect('cadastro')

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)

        if user: #se houver um usuário, será retornado uma estância do usuário do banco, caso falso, retorna none
            auth.login(request, user)
            return redirect ('pacientes/home')

        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
        return redirect ('usuarios/login')