from django.http import HttpResponse
from django.views import View
from relacionamentos.models import Reporter
from django.core import serializers
from django.http import JsonResponse


class NomeView(View):
    @staticmethod
    def get(request, name=""):
        if name =="" or name == " ":
            exemplos = list(Reporter.objects.all())
        else:
            exemplos = Reporter.objects.find_by_name(name)
        tipo = str(request.GET.get("type"))
        saida = ""
        match tipo.lower():
            case "http":
                for exemplo in exemplos:
                    saida += f"<p><b>ID: </b>{exemplo.id}</p>"
                    saida += f"<p><b>NOME: </b>{exemplo.nome}</p>"
                    saida += f"<p><b>CPF: </b>{exemplo.cpf}</p>"
                    saida += f"<p><b>EMAIL: </b>{exemplo.email}</p>"
                    saida += f"<hr>"
                return HttpResponse(saida, status = 200)
            case "json":
                objeto = serializers.serialize('python', exemplos)
                return JsonResponse(objeto, safe=False)
            case _:
                return HttpResponse("Bad Request", status=400)
