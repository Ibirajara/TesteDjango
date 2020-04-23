
from django.urls import path
from . import views
urlpatterns = [
    path('listar/', views.listarCargos, name='listarCargos' ),
    path('incluir/', views.incluirCargo, name='incluirCargo'),
]
