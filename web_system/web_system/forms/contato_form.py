from django.core.validators import MinLengthValidator
from django import forms


class ContatoForm(forms.Form):
    subject = forms.CharField(label='assunto',
                              max_length=100,
                              validators=[MinLengthValidator(3)],
                              help_text='Digite o assunto da mensagem')
    sender = forms.EmailField(label='Email',
                              help_text='Digite seu endereço de email principal')
    message = forms.CharField(label='Mensagem',
                              help_text='Digite sua mensagem',
                              widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False,
                                   label='Deseja receber uma copia?',)

    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.widget.attrs.update({'class': 'form-control'})
        self.fields.get('cc_myself').widget.attrs.pop('class')