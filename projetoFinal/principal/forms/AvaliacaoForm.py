from django import forms
from principal.models import Avaliacao
from django.core.exceptions import NON_FIELD_ERRORS, FieldError

class AvaliacaoForm(forms.ModelForm):

    class Meta:
        model = Avaliacao
        fields = ['autor', 'texto', 'nota', 'restaurante']

        labels = {
            'nota': 'Como classificaria o restaurante?',
        }

        help_texts = {
            'texto': '<span aria-hidden="true">Obrigatório, </span>mínimo de 10 caracteres',
        }

        widgets = {
            'autor': forms.HiddenInput(),
            'restaurante': forms.HiddenInput(),
            'texto': forms.TextInput(attrs = {'v-model': 'comentario', 'v-on:focusout': 'registrarMudancaInputForm', 'aria-describedby': 'errors-form-texto', 'required': 'true', 'aria-required': 'true'}),
            'nota': forms.RadioSelect(attrs = {'v-model': 'radioNota', 'v-on:change': 'registrarMudancaInputForm', 'aria-describedby': 'errors-form-nota', 'class': 'sr-only', 'required': 'true', 'aria-required': 'true'})
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Você já fez uma avaliação. Caso queira, edite a avaliação já existente.",
            },
        }