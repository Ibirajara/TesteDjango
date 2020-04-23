from django.shortcuts import render
from cargo.models import Cargo
from .models import Funcionario
from .forms import funcForm

def listarFuncionarios(request):
    cargos = Cargo.objects.count()
    funcionarios = Funcionario.objects.all()
    verr = 'Não existem funcionários cadastrados!'
    return render(request, 'listarfuncionarios.html', {'funcionarios': funcionarios, 'v_erro': verr, 'cargos': cargos})

def incluirFuncionario(request):
    return render(request, 'mensagemincluircargo.html')
    '''
    form = funcForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listarFuncionarios')
    return render(request, 'salvarfuncionario.html', {'form': form})'''

