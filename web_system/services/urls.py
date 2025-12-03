from django.urls import path
from services.views import *
from services.views.estaticas import saudacao


app_name = 'services'

urlpatterns = [
    path('', api_root, name="api-root"),

    path('saudacao', saudacao, name="saudacao"),

    path('saudacao/classe', ExemplosSaudacao.as_view(), name="saudacao_classe"),

    path('calculo', calculo, name="calculo"),

    path('reporter', ReporterListService.as_view(), name='reporter_list'),
]
