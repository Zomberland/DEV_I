from django.db import models
from .base_model import BaseModel
from relacionamentos.validators import validate_cpf
from django.core.validators import MinLengthValidator


class Reporter(BaseModel):
    nome = models.CharField(max_length = 100,
                            validators=[MinLengthValidator(3)],
                            verbose_name='Reporter',
                            help_text=('Reportar Nome'))

    cpf = models.CharField(max_length = 11,
                           validators=[MinLengthValidator(11), validate_cpf],
                           help_text=('Digite seu cpf sem os pontos'),)

    email = models.CharField(max_length = 255,)

    def __str__(self):
        return self.nome
