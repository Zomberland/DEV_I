from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
import random
import string
from django.http import HttpResponse
from django.views import View
from relacionamentos.models import Reporter

def reporter_list(request):
    reporter= Reporter.objects.all()

    contexto = {
        'reporter' : reporter,
    }
    return render(request, 'exemplos/reporter.html', contexto)

def reporter_detail(request, pk):
    mensagem = Reporter.objects.get(id=pk)
    contexto = {
        'mensagem' : mensagem,

    }

    return render(request, 'reporter_detail.html', contexto)

def reporter_delete(request, reporter_id):
    reporter = get_object_or_404(Reporter, pk=reporter_id)
    try:
        if request.method == 'POST':
            v_reporter_id = request.POST.get("reporter_id", None)
            if int(v_reporter_id) == reporter_id:
                reporter.delete()
                return redirect('relacionamentos:reporter_funcao_list')

        else:
            contexto = {
                'reporter' : reporter,
            }
            return render(request, 'exemplos/delete.html', contexto)

    except Exception as e:
        contexto = {}
        print(e)
        return render(request, 'exemplos/reporter.html', contexto)

def gerar_codigo(request, reporter_id):
    reporter = get_object_or_404(Reporter, pk=reporter_id)
    try:
        letters = string.ascii_letters + string.digits
        reporter.nome = ''.join(random.choice(letters) for _ in range(10))
        reporter.save()
        return redirect('relacionamentos:reporter_funcao_list')
    except:
        print(f'Erro ao gerar codigo para o reporter {reporter}')
        return redirect('relacionamentos:reporter_funcao_list')
