from .base import Base
from django.db import models
from django.contrib import admin
from aula.enumerations.genero import Genero

class Perfil(Base):
    cod = models.CharField(max_length=10, help_text="Código do perfil") 
    nome = models.CharField(max_length=255, help_text="Nome do perfil", unique=True)
    data_nascimento = models.DateField(max_length=10, help_text="Digite sua Data de Nascimento")
    bio = models.CharField(max_length=255, help_text="Fale um pouco sobre você")
    passaporte = models.CharField(max_length=10, help_text="Digite sua Passaporte")
    genero = models.CharField(
        max_length=20,
        choices=Genero.choices,
        default=Genero.NOT_SPECIFIED,
        help_text="Selecione o gênero"
    )
    cidade = models.CharField(max_length=255, help_text="Digite sua Cidade")
    pais = models.CharField(max_length=10, help_text="Digite sua Pais")

    def __str__(self):
        return f"{self.nome} - {self.get_genero_display()} - {self.cidade}/{self.pais}"

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('cod', 'nome', 'cidade', 'pais')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('nome',)
    list_filter = ('updated_at',)