from django.http import HttpResponse
from django.views import View
from relacionamentos.models import Reporter


class NomeView(View):
    @staticmethod
    def get(request, name):
        exemplo = Reporter.objects.find_by_name(name)
        mensagem = ""
        for objeto in exemplo:
            mensagem += f"<html><body><h1>{objeto}<br />"
        return HttpResponse(mensagem, status=200)
