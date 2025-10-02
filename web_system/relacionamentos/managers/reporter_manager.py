from django.db.models import QuerySet
from .base_manager import BaseManager
from datetime import date

class ReporterManager(BaseManager):
    def find_by_nome(self,nome: str)->list['Reporter']:
        if isinstance(nome , str) and len(nome)> 0:
            consulta = self.filter(nome__icontains=nome).order_by('nome')[:2]
            return list(consulta)
        else:
            raise TypeError('o nome deve ser string')

    def find_by_publication_date_sinse(self, publication_date: date)-> QuerySet['Reporter']:
        if isinstance(publication_date, date):
            today = date.today()
            consulta = self.filter(article__pub_date__ranger=(publication_date, today))
            return consulta

