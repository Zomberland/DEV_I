from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views import View
from relacionamentos.models import Reporter
import string, random
from django.http import HttpResponse
from relacionamentos.forms.reporter import ReporterForm


class ReporterListView(View):
    @staticmethod
    def get(request):
        reporter = Reporter.objects.all()
        contexto = {
            'reporter': reporter,
        }
        return render(request, 'exemplos/reporter.html', contexto)


class ReporterDetailView(View):
    @staticmethod
    def get(request, pk):
        reporter = Reporter.objects.get(id=pk)
        contexto = {
            'reporter': reporter,

        }

        return render(request, 'exemplos/reporter_detail.html', contexto)

class ReporterGerarCodigoView(View):
    @staticmethod
    def get(request, reporter_id):
        reporter = get_object_or_404(Reporter, pk=reporter_id)
        try:
            letters = string.ascii_letters + string.digits
            reporter.nome = ''.join(random.choice(letters) for _ in range(10))
            reporter.save()
            return redirect('relacionamentos:reporter_funcao_list')
        except:
            print(f'Erro ao gerar codigo para o reporter {reporter}')
            return redirect('relacionamentos:reporter_funcao_list')

class ReporterDeleteView(View):
    @staticmethod
    def get(request, reporter_id):
        reporter = get_object_or_404(Reporter, pk=reporter_id)
        try:
            if request.method == 'POST':
                v_reporter_id = request.POST.get("reporter_id", None)
                if int(v_reporter_id) == reporter_id:
                    reporter.delete()
                    return redirect('relacionamentos:reporter_funcao_list')

            else:
                contexto = {
                    'reporter': reporter,
                }
                return render(request, 'exemplos/delete.html', contexto)

        except Exception as e:
            contexto = {}
            print(e)
            return render(request, 'exemplos/reporter.html', contexto)

class ReporterCreateView(View):
    @staticmethod
    def get(request):
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