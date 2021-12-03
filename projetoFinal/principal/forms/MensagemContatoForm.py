from django import forms
from principal.models import MensagemContato

class MensagemContatoForm(forms.ModelForm):
    
    class Meta:

        model = MensagemContato
        fields = ['mensagem']

        help_texts = {
            'mensagem': 'Seja sucinto, mas escreva, no mínimo, 25 caracteres.'
        }

        widgets = {
            'mensagem': forms.Textarea(attrs = {'v-model': 'mensagem', 'v-on:focusout': 'registrarMudancaInputForm', 'rows': 3, 'aria-describedby': 'errors-form-mensagem', 'required': 'required', 'aria-required': 'true'})
        }