from django.shortcuts import render, redirect, HttpResponse
from django.views import View

class PrimeiraView(View):
    @staticmethod
    def get(request):
        mensagem = request.META['REMOTE_ADDR']
        return HttpResponse(mensagem, status=200)