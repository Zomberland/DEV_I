from django.contrib import admin
from aula.models import Atividade
from aula.models.perfil import Perfil, PerfilAdmin

admin.site.register(Atividade)
admin.site.register(Perfil, PerfilAdmin)
