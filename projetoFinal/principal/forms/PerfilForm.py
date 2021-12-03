from django import forms
from principal.models import Perfil, Frase
from django.conf import settings

class FotoRadioSelect(forms.RadioSelect):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        option['label'] = 'src="' + settings.MEDIA_URL + str(value.instance.endereco) + '" alt="' + value.instance.descricao + '"'
        return option

class FraseRadioSelect(forms.RadioSelect):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        option['label'] = '<q>' + value.instance.texto + '.</q> <span class="address">(' + value.instance.autor + ')</span>'
        return option

class PerfilForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.fields['prato_preferido'].empty_label = 'Digite o nome do prato que gostaria de escolher'

    class Meta:
        model = Perfil
        fields = ['foto_fantasia', 'prato_preferido', 'data_nascimento_fantasia', 'culinaria_favorita_fantasia', 'frase_bio']

        labels = {
            'foto_fantasia': 'Foto de perfil',
            'frase_bio': 'Citação favorita',
            'data_nascimento_fantasia': 'Data de nascimento',
            'culinaria_favorita_fantasia': 'Culinária favorita',
        }

        help_texts = {
            'foto_fantasia': 'Selecione uma dentre as imagens disponíveis, para que esta seja sua foto de perfil neste site',
            'frase_bio': 'Selecione uma dentre as frases disponíveis, para que esteja seja sua biografia neste site',
            'prato_preferido': 'Procure por seu prato favorito',
            'data_nascimento_fantasia': 'Informe a data 21/11/2027',
            'culinaria_favorita_fantasia': 'Selecione a culinária italiana',
        }

        widgets = {
            'foto_fantasia': FotoRadioSelect(attrs = {'class': 'sr-only', 'v-on:change': 'registrarMudancaInputForm', 'aria-describedby': 'errors-form-foto_fantasia', 'aria-required': 'true', 'required': 'required'}),
            'frase_bio': FraseRadioSelect(attrs = {'class': 'sr-only', 'v-on:change': 'registrarMudancaInputForm', 'aria-describedby': 'errors-form-frase_bio', 'aria-required': 'true', 'required': 'required'}),
            'prato_preferido': forms.Select(attrs = {'id': 'prato-preferido-picker', 'v-on:change': 'registrarMudancaInputForm', 'aria-describedby': 'errors-form-prato_preferido'}),
            'data_nascimento_fantasia': forms.TextInput(attrs = {'autocomplete': 'bday', 'v-on:focusout': 'registrarMudancaInputForm', 'aria-describedby': 'errors-form-data_nascimento_fantasia'}),
            'culinaria_favorita_fantasia': forms.Select(attrs = {'v-on:change': 'registrarMudancaInputForm', 'aria-describedby': 'errors-form-culinaria_favorita_fantasia', 'aria-required': 'true', 'required': 'required'}),
        }