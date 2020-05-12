from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from publicacao.models import Publicacao

# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        email = request.POST['email']
        if campo_vazio(nome):
            messages.error(request,'O Campo Nome Não Pode Ficar Vazio')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'O Campo Email Não Pode Ficar Em Branco')
            return redirect('cadastro')
        if senhas_nao_sao_iguais(senha,senha2):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email = email).exists():# Verificar se existe o email já cadastrado no banco de dados
            messages.error(request, 'Usuario já Cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email = email, password=senha)#Cria um objeto Usuario
        user.save()
        print("O Id do usuario é:" + str(user.id))
        messages.success(request, 'Cadastro realizado com Sucesso!')
        return redirect('login')
    return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os Campos Email e Senha Não Podem Ficar Em Branco')
            return redirect('login')
        if User.objects.filter(email=email).exists(): # verifico se existe o emial no banco de dados
            nome = User.objects.filter(email=email).values_list('username', flat=True).get() # pego o usuraio que tem o email informado
            user = auth.authenticate(request, username=nome, password=senha) # faço a autenticação com o retorno do nome do usurai do banco de dados.
            if user is not None: # verifco se o usuario não está nulo
                auth.login(request, user) # realizo o login
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')
            messages.error(request, 'Email ou senha Incorreto')
        messages.error(request, 'Email ou senha Incorreto')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
    


def campo_vazio(campo):
    return not campo.strip()

def senhas_nao_sao_iguais(senha,senha2):
    return senha !=senha2
