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
    mensagem = "boa noite"
    if 12 > agora.hour > 6:
        mensagem = "bom dia"
    elif 0 < agora.hour <= 6:
        mensagem = "boa madrugada"

    completo = f"<html><body><h1>{mensagem.capitalize()} visitante" \
               f"<br />{agora}</h1>{request.META["REMOTE_ADDR"]}</body></html>"

    #return HttpResponse(completo)
    return render(request, 'saudacao.html', {completo: 'mensagem'})

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



