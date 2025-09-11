from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from .magazine import Magazine
from .base_model import BaseModel
from .reporter import Reporter


class Paper(BaseModel):
    title = models.CharField(max_length = 100,
                             verbose_name= 'title',
                             help_text=('insira o titulo de reportagem'))
    pub_date = models.DateField(verbose_name= ('published in'))
    reporter = models.ForeignKey(Reporter, on_delete= models.RESTRICT,)
    magazine = models.ManyToManyField(Magazine, null=True, blank=True,
                                      through="Publication",
                                      through_fields=("paper","magazine"))

    def __str__(self):
        return f"{self.title} by {self.reporter.nome if self.reporter is not None else ''}"

    def clean(self):
        today = date.today()

        try:
            if self.pub_date != today:
                raise ValidationError("a data não pode ser diferente de hoje.")

        except ValueError:
            pass
