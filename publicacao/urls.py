from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:publicacao_id>', views.publicacao, name='publicacao'),
    path('teste/<int:publicacao_id>', views.comentario_publicacao, name='cadastra_comentario'),

]
