from django.shortcuts import render, redirect
from .models import Especialidades,  DadosMedico
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.

def cadastro_medico(request):
    if request.method == 'GET':
        especialidades = Especialidades.objects.all()#cria uma variavel que armazena os atributos de especialidades salvo no banco de dados
        
        #essa é a forma de exportar essa variável para o html. Lá chamamos ela através da tag do django {%%}
        return render(request, 'cadastro_medico.html', {'especialidades': especialidades})
    elif request.method == 'POST':
        crm = request.POST.get('crm')
        cim = request.FILES.get('cim')
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        rg = request.FILES.get('rg')
        foto = request.FILES.get('foto') 
        especialidade = request.POST.get('especialidade')
        descricao = request.POST.get('descricao')
        valor_consulta = request.POST.get('valor_consulta')

        dados_medico = DadosMedico(
            crm = crm,
            cedula_identidade_medica = cim,
            nome = nome,
            cep = cep,
            rua = rua,
            bairro = bairro,
            numero = numero,
            rg = rg,
            foto_perfil = foto,
            especialidade_id = especialidade,
            descricao = descricao,
            valor_Consulta = valor_consulta,      
            user = request.user
        )

        dados_medico.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')

        return redirect('/medicos/abrir_horarios')