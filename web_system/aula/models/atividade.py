from .base import Base
from django.db import models


class Atividade(Base):
    nome = models.CharField(max_length=100, help_text="Digite o nome do Aluno")
    preco = models.DecimalField(verbose_name='Preço',
                                max_digits=10,
                                decimal_places=2,
                                default=0.00,
                                help_text="Digite o valor em reais R$")
    turno = models.CharField(max_length=8, null=True,
                             blank=True,
                             help_text="Digite o turno da aula") #null é para tirar a obrigatoriedade, pode ser usado Blank=True(para front) tambem.
    nota = models.FloatField(default=0.0, help_text="Digite a nota do aluno")

    def __str__(self):
        return f"{self.id} - {self.nome}"

