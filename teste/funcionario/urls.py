
from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listarFuncionarios, name='listarFuncionarios' ),
    path('incluir/', views.incluirFuncionario, name='incluirFuncionario'),
]
