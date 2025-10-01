from django.urls import path
import relacionamentos.views as views_funcoes

#mesma coisa que o appname
app_name = 'relacionamentos'

urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view, name='primeira_view'),
]