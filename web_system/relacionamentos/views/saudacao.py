from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.views import View
from datetime import datetime

class SaudacaoView(View):
    def get(self, request):
        agora = datetime.now()
        hora = agora.hour

        if 6 < hora < 12:
            mensagem = "Bom dia"
        elif 0 < hora <= 6:
            mensagem = "Boa madrugada"
        elif 12 <= hora < 18:
            mensagem = "Boa tarde"
        else:
            mensagem = "Boa noite"

        contexto = {
            'mensagem': mensagem,
            'hora_atual': agora.strftime('%H:%M:%S'),
            'data_atual': agora.strftime('%d/%m/%Y'),
            'ip': request.META.get('REMOTE_ADDR', 'IP não identificado')
        }

        return render(request, 'saudacao_classe.html', contexto)