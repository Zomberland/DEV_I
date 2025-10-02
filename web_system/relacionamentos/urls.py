from django.urls import path
import relacionamentos.views.estatica as views_funcoes
from relacionamentos.views import PrimeiraView

#mesma coisa que o appname
app_name = 'relacionamentos'

urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view, name ='primeira_view'),

    path('funcao/saudacao', views_funcoes.saudacao, name ='saudacao'),

    path('funcao/<str:name>', views_funcoes.nome, name = 'nome'),

    path('funcao/exercicio/<str:letra>',views_funcoes.exercicio, name='exercicio'),

    path('classe/teste', PrimeiraView.as_view(), name='primeira_view_classe')
]