from django.urls import path

from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('criar/publicacao', views.criar_publicacao, name='criar_publicacao'),
    path('deleta/<int:publicacao_id>', views.deleta_publicacao, name='deleta_publicacao'),
    path('edita/<int:publicacao_id>', views.edita_publicacao, name='edita_publicacao'),
    path('atualiza_publicao', views.atualiza_publicacao, name='atualiza_publicacao'),
    #path('teste', views.comentario_publicacao, name='cadastra_comentario'),
]
