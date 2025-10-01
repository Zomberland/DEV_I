from django.shortcuts import render, redirect, HttpResponse

def primeira_view(request):
    mensagem = "Bom dia DEV I"
    return HttpResponse(mensagem, status=200)