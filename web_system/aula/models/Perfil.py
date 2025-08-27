from .base import Base
from django.db import models

class Perfil:
    data_nascimento = models.DateField(maxlength=10, help_text="Digite sua Data de Nascimento")
    bio = models.CharField(max_length=255, help_text="Fale um pouco sobre você")
    passaporte = models.CharField(max_length=10, help_text="Digite sua Passaporte")
    genero = models.CharField(max_length=9, help_text="Digite sua Genero")
    cidade = models.CharField(max_length=255, help_text="Digite sua Cidade")
    pais = models.CharField(max_length=10, help_text="Digite sua Pais")

    def __str__(self):
        return (f"{self.id}"
                f"{self.data_nascimento}"
                f"{self.cidade}"
                f"{self.pais}")