from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
import random
import string
from django.contrib.auth.decorators import permission_required, login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.views import View

from relacionamentos.forms.reporter import ReporterForm
from relacionamentos.models import Reporter

@require_http_methods(["GET"])
def reporter_list(request):
    reporter= Reporter.objects.all()

    contexto = {
        'reporter' : reporter,
    }
    return render(request, 'exemplos/reporter.html', contexto)


@login_required
@permission_required("relacionamentos.view_reporter", raise_exception=True)
@require_http_methods(["GET"])
def reporter_detail(request, pk):
    reporter = Reporter.objects.get(id=pk)
    contexto = {
        'reporter' : reporter,

    }

    return render(request, 'exemplos/reporter_detail.html', contexto)


@login_required
@permission_required("relacionamentos.view_reporter", raise_exception=True)
@require_http_methods(["GET", "POST"])
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

@login_required
@permission_required("relacionamentos.view_reporter", raise_exception=True)
@require_http_methods(["GET"])
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


@login_required
@permission_required("relacionamentos.view_reporter", raise_exception=True)
@require_http_methods(["GET", "POST"])
def reporter_create(request):
    if request.method == 'POST':
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter_funcao_list')
    else:
        form = ReporterForm()
    contexto = {
        'form': form
    }
    return render(request, 'exemplos/create_simple.html', contexto)


@login_required
@permission_required("relacionamentos.view_reporter", raise_exception=True)
@require_http_methods(["GET", "POST"])
def reporter_update(request, reporter_id):
    reporter = get_object_or_404(Reporter, pk=reporter_id)
    if request.method == 'POST':
        form = ReporterForm(request.POST, instance=reporter)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter_funcao_list')
    else:
        form = ReporterForm(instance=reporter)
    contexto = {
        'form': form,
        'reporter': reporter,
    }
    return render(request, 'exemplos/update.html', contexto)