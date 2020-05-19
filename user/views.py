from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from publicacao.models import Publicacao
from .models import Usuario

# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        email = request.POST['email']
        nascimento = request.POST['nascimento']
        estado = request.POST['estado']
        cidade = request.POST['cidade']
        telefone = request.POST['telefone']
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
        if campo_vazio(nascimento):
            messages.error(request,'A data de nascimento não pode ')
        user = User.objects.create_user(username=nome, email = email, password=senha)#Cria um objeto Usuario
        user.save()
        usuario = Usuario.objects.create(user= user, nome = nome, data_nascimento = nascimento,
        estado = estado, cidade = cidade, email = email, telefone = telefone)
        usuario.save()
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


def dashboard(request):
    if request.user.is_authenticated: # verifico o usuario está autenticado
        print('Usuario do Django' + str(request.user.id))
        usuario = get_object_or_404(Usuario,pk=request.user.id)
        print(usuario)
        publicacoes = Publicacao.objects.order_by('-data_publicacao').filter(usuario = usuario.id)
        dados = {
            'publicacoes' : publicacoes
        }
        print(dados)
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def criar_publicacao(request):
    if request.method == 'POST':
        nome_publicacao = request.POST['nome_publicacao']
        descricao = request.POST['descricao']
        categoria = request.POST['categoria']
        preco = float(request.POST['preco'])
        foto_publicacao = request.FILES['foto_publicacao']
        usuario = get_object_or_404(Usuario,pk=request.user.id)
        publicacao = Publicacao.objects.create(usuario = usuario, nome_publicacao = nome_publicacao , descricao = descricao,
        categoria = categoria, foto_publicacao = foto_publicacao, preco =preco)
        publicacao.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/criar_publicacao.html')

def deleta_publicacao(request, publicacao_id):
    publicacao = get_object_or_404(Publicacao, pk=publicacao_id)
    publicacao.delete()
    return redirect('dashboard')


def edita_publicacao(request, publicacao_id):
    publicacao = get_object_or_404(Publicacao, pk=publicacao_id)
    publicacao_a_editar = {'publicacao':publicacao}
    return render(request, 'usuarios/edita_publicacao.html' ,publicacao_a_editar)

def atualiza_publicacao (request):
    if request.method == 'POST':
        publicacao_id = request.POST['publicacao_id']
        p = Publicacao.objects.get(pk=publicacao_id)
        p.nome_publicacao = request.POST['nome_publicacao']
        p.descricao = request.POST['descricao']
        p.preco = float(request.POST['preco'])
        p.categoria = request.POST['categoria']
        if 'foto_publicacao' in request.FILES:
            r.foto_publicacao = request.FILES['foto_publicacao']
        p.save()
        return redirect('dashboard')



def campo_vazio(campo):
    return not campo.strip()

def senhas_nao_sao_iguais(senha,senha2):
    return senha !=senha2
