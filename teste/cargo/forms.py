from django.forms import ModelForm
from .models import Cargo

class cargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = ['nome_cargo', 'descricao', 'salario']
