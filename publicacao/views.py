from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Publicacao
# Create your views here.

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
    print("Entrou")
    publicacoes = get_object_or_404(Publicacao, pk=publicacao_id) #Pega o Objeto ou dá erro 404
    print(publicacao)

    publicacoes_a_exibir = {
        'publicacoes': publicacoes
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