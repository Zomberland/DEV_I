from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.views import View
from datetime import datetime

class SaudacaoView(View):
    @staticmethod
    def get(request):
        agora = datetime.now()
        mensagem = "Boa noite"
        if 12 > agora.hour > 6:
            mensagem = "Bom dia"
        elif 0 < agora.hour <= 6:
            mensagem = "Boa madrugada"

        completo = (f"<html><body><h1>{mensagem.capitalize()}"
                    f"<br />{agora}</h1></body></html>")

        return HttpResponse(completo)