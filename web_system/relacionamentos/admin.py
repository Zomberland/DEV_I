from django.contrib import admin
from relacionamento.models import Person
from relacionamento.models.perfil import Perfil, PerfilAdmin

# Register your models here.
admin.site.register(Person)
