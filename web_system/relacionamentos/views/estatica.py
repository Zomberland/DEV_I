from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from relacionamentos.models import Reporter
from django.core import serializers
from django.http import JsonResponse


def primeira_view(request):
    #mensagem = "Bom dia DEV I"
    contexto = {
        'mensagem': "Bom dia DEV I"
    }
    #return HttpResponse(mensagem, status=200)
    return render(request, 'primeira.html', contexto)

def saudacao(request):
    agora = datetime.now()

    hora = agora.hour
    if 6 < hora < 12:
        mensagem = "bom dia"
    elif 0 < hora <= 6:
        mensagem = "boa madrugada"
    elif 12 <= hora < 18:
        mensagem = "boa tarde"
    else:
        mensagem = "boa noite"

    contexto = {
        'mensagem': mensagem.capitalize(),
        'hora_atual': agora.strftime('%H:%M:%S'),
        'data_atual': agora.strftime('%d/%m/%Y'),
        'ip': request.META.get('REMOTE_ADDR', 'IP não identificado')
    }

    return render(request, 'saudacao.html', contexto)

def nome(request, name):
    exemplo = Reporter.objects.find_by_nome(name)
    objeto = serializers.serialize('python', exemplo)
    return JsonResponse(objeto, safe=False)

def exercicio(request, letra):
    com_alteracao = {
        "a" : "4",
        "e" : "3",
        "i" : "1",
        "o" : "0",
        "u" : "V"
    }
    letra_qualquer = letra.lower()

    if letra_qualquer in com_alteracao:
        original = letra
        alterado = com_alteracao[letra_qualquer]
        resposta = f'sem alteração: {original}---Com alteração: {alterado}'

        return HttpResponse(resposta)
    else:
        return HttpResponse(f'não encontrado')



