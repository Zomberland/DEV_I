from .base import Base
from django.db import models


class Atividade(Base):
    nome = models.CharField(max_length=100)

