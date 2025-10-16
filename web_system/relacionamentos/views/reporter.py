from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponse
from django.views import View
from relacionamentos.models import Reporter

def reporter(request):
    reporter= Reporter.objects.all()

    contexto = {
        'reporter' : reporter,
    }
    return render(request, 'reporter.html', contexto)

def reporter_detail(request, pk):
    mensagem = Reporter.objects.get(id=pk)
    contexto = {
        'mensagem' : mensagem,

    }

    return render(request, 'reporter_detail.html', contexto)

def delete(request, reporter_id):
    reporter = get_object_or_404(Reporter, pk=reporter_id)
    try:
        if request.method == 'POST':
            v_reporter_id = request.POST.get("reporter_id", None)
            if int(v_reporter_id) == reporter_id:
                reporter.delete()
                return redirect('relacionamento:reporter_funcao_list')

            else:
                contexto = {
                    'reporter' : reporter,
                }
                return render(request, 'reporter/delete.html', contexto)

    except:
        contexto = {}
        return render(request, 'reporter/list.html', contexto)