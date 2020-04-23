from django.db import models

class Cargo(models.Model):
    nome_cargo = models.CharField(max_length=100, verbose_name='Nome')
    descricao  = models.CharField(max_length=200, verbose_name='Descrição', blank=True, null=True)
    salario    = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.nome_cargo
    
