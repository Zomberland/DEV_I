from django.db import models
from .base_model import BaseModel


class Magazine(BaseModel):
    nome = models.CharField(max_length=50)
    edicao = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nome} - {self.edicao}'