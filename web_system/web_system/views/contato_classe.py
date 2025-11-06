from web_system.forms.contato_form import ContatoForm
from django.views import View
from django.shortcuts import render

class ContatoView(View):
    @staticmethod
    def get(request):
        form = ContatoForm()
        context = {
            'form': form,
            'url_form': 'classe_contato',

        }
        return render(request, 'contato/pagina_contato.html', context)

    @staticmethod
    def post(request):
        if request.method == 'POST':
            form = ContatoForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data.get('subject')
                message = form.cleaned_data.get('message')
                sender = form.cleaned_data.get('sender')
                cc_myself = form.cleaned_data.get('cc_myself')

                recipients = ['2020008663@restinga.ifrs.edu.br']
                if cc_myself:
                    recipients.append(sender)
                # TODO: configurar o settings.py com as credenciais
                # chamada para enviar email
                # send_email(subject, message, sender, recipients)
                context = {
                    'recipients': recipients,
                    'form': form,
                }
                return render(request, 'contato/exibicao.html', context)
        elif request.method == 'GET':
            form = ContatoForm()
            context = {
                'form': form,
                'url_form': 'funcao_contato',

            }
            return render(request, 'contato/pagina_contato.html', context)