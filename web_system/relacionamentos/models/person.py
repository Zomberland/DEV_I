from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.db import models
from .base_model import BaseModel
from datetime import date

from ..validators import validate_cpf


class Person(BaseModel):
    name = models.Charfield(max_length=100,
                            validators=[MinLengthValidator(3)],
                            help_text=_("Nome da pessoa"),
                            verbose_name=_('name'))
    birthdate = models.DateField(verbose_name=_('Data Nascimento'),
                                 help_text=_("insira sua data de nascimento"))
    cpf = models.Charfield(max_length=11,
                           validators=[MinLengthValidator(11), validate_cpf()],
                           help_text=_("insira o seu cpf sem os pontos"))

    def __str__(self):
        return self.name

    def celan(self):
        today = date.today()

        try:
            if self.birthdate > today.replace(year=today.year - 18):
                raise ValidationError({"birtdate":
                                       _("voce precisa ter 18 anos de idade")},
                                      )
        except ValueError:
            pass