from django.shortcuts import render
from .models import Cargo
from .forms import cargoForm

def listarCargos(request):
    cargos = Cargo.objects.all()
    verr = 'Não existem cargos cadastrados!'
    return render(request, 'listarcargos.html', {'cargos': cargos, 'v_erro': verr} )

    
def incluirCargo(request):
    form = cargoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listarCargos')
    return render(request, 'salvarcargo.html', {'form': form})
