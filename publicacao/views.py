from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Publicacao, Comentario
from django.contrib import auth, messages
from user.models import Usuario

def index(request):
    #Filtarando e ordenando
    publicacoes = Publicacao.objects.order_by('-data_publicacao').filter(publicada=True) # Select * from publicacao where publicada = True order by data_publicacao desc
    dados = {
        'publicacoes' : publicacoes,
    }
    for publicacao in publicacoes:
        print(publicacao)
    return render(request,"index.html",dados)

def publicacao(request, publicacao_id):
    publicacoes = get_object_or_404(Publicacao, pk=publicacao_id) #Pega o Objeto ou dá erro 404
    comentarios = Comentario.objects.filter(publicacao=publicacao_id)
    publicacoes_a_exibir = {
        'publicacoes': publicacoes,
        'comentarios': comentarios
    }
    return render(request,"publicacao.html", publicacoes_a_exibir)

def buscar(request):
    lista_publicacaos = None
    if 'buscar' in request.GET:# se tem o paramentro buscar dentro do GET
        lista_publicacaos = publicacao.objects.order_by('-data_publicacao').filter(publicada=True)
        nome_da_busca= request.GET['buscar']
        if buscar: #Se buscar tiver preenchido
            lista_publicacaos = lista_publicacaos.filter(nome_publicacao__icontains=nome_da_busca) # o __icontains funciona como um like do SQL
    dados = {
        'publicacaos': lista_publicacaos
    }

    return render(request, 'buscar.html', dados)


def comentario_publicacao(request, publicacao_id):
    print("entrou na funação do comentario")
    if request.method == 'POST':
        titulo_comentario = request.POST['titulo_comentario']
        comentario_texto = request.POST['comentario']
        print("Entrou no primeiro if : "+titulo_comentario+" comen: "+comentario_texto)
        if campo_vazio(titulo_comentario):
            messages.error(request, 'O titulo do Comentario não pode ficar vazio')
            return  redirect('publicacao',publicacao_id)
        if campo_vazio(comentario_texto):
            messages.error(request, 'O campo comentario não pode ficar vazio')
            return  redirect('publicacao',publicacao_id)
        print("Passou dos IFs")
        usuario = get_object_or_404(Usuario,pk=request.user.id)
        print(usuario)
        publicacao = get_object_or_404(Publicacao, pk=publicacao_id)
        print(publicacao)
        comentario = Comentario.objects.create(publicacao = publicacao, usuario = usuario, titulo = titulo_comentario, descricao= comentario_texto)
        comentario.save()
        print(comentario)
        return  redirect('publicacao',publicacao_id)
    return  render(request,"teste.html")

def campo_vazio(campo):
    return not campo.strip()
