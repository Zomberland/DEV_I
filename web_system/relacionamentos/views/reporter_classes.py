from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views import View
from relacionamentos.models import Reporter

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