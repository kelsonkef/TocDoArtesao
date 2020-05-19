from django.urls import path

from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('criar/publicacao', views.criar_publicacao, name='criar_publicacao'),
    path('deleta/<int:publicacao_id>', views.deleta_publicacao, name='deleta_publicacao'),
    #path('edita/<int:receita_id>', views.edita_receita, name='edita_receita'),
    #path('atualiza_receita', views.atualiza_receita, name='atualiza_receita'),
]
