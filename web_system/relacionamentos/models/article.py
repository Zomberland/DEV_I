from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from .base_model import BaseModel
from relacionamentos.models.reporter import Reporter


class Article(BaseModel):
    title = models.CharField(max_length = 100,
                             verbose_name= 'title',
                             help_text=('insira o titulo de reportagem'))
    pub_date = models.DateField(verbose_name= ('published in'))
    reporter = models.ForeignKey(Reporter, on_delete= models.RESTRICT,)

    def __str__(self):
        return f"{self.title} by {self.reporter.name if self.reporter is not None else ''}"

    def clean(self):
        today = date.today()

        try:
            if self.pub_date != today:
                raise ValidationError("a data não pode ser diferente de hoje.")

        except ValueError:
            pass
