from django.shortcuts import render, redirect, HttpResponse
from django.views import View

class PrimeiraView(View):
    def get(self, request):
        contexto = {
            'mensagem': request.META.get('REMOTE_ADDR', 'IP não identificado')
        }
        return render(request, 'primeira_view_classe.html', contexto)