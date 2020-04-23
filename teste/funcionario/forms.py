from django.forms import ModelForm
from .models import Funcionario


class funcForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = [ 'nome', 'cpf', 'cargo', 'inativo', 'nascimento' ]