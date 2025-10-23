from django.urls import path
from relacionamentos.views.estatica import primeira_view,saudacao,nome,exercicio
from relacionamentos.views import PrimeiraView
from relacionamentos.views import SaudacaoView
from relacionamentos.views import NomeView
from relacionamentos.views.reporter import reporter_list, reporter_detail, reporter_delete, gerar_codigo, reporter_create, reporter_update
from relacionamentos.views.reporter_classes import ReporterListView, ReporterDetailView
#mesma coisa que o appname
app_name = 'relacionamentos'

urlpatterns = [
    #funções

    path('funcao/teste', primeira_view, name ='primeira_view'),

    path('funcao/saudacao', saudacao, name ='saudacao'),

    path('funcao/<str:name>', nome, name = 'nome'),

    path('funcao/exercicio/<str:letra>',exercicio, name='exercicio'),

    path('classe/teste', PrimeiraView.as_view(), name='primeira_view_classe'),

    path('classe/saudacao', SaudacaoView.as_view(), name='saudacao_view_classe'),

    path('classe/nome/<str:name>', NomeView.as_view(), name='nome_view_classe'),

    path('reporter/funcao/', reporter_list, name = "reporter_funcao_list"),

    path('reporter/funcao/read/<int:pk>', reporter_detail, name="reporter_funcao_read"),

    path('reporter/funcao/delete/<int:reporter_id>', reporter_delete, name="reporter_funcao_delete"),

    path('reporter/funcao/gerar_codigo/<int:reporter_id>', gerar_codigo, name='reporter_gerar_codigo'),

    path('reporter/funcao/create', reporter_create, name = 'reporter_funcao_create'),

    path('reporter/funcao/update/<int:reporter_id>', reporter_update, name='reporter_funcao_update'),

    #classes

    path('reporter/classe', ReporterListView.as_view(), name="reporter_classe_list"),

    path('reporter/classe/read/<int:pk>', ReporterDetailView.as_view(), name="reporter_classe_detail"),

]