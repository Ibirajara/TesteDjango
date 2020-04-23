from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf  = models.CharField(max_length=14, verbose_name='CPF')
    cargo = models.ForeignKey('cargo.Cargo', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cargo' )
    inativo = models.BooleanField(default=False)
    nascimento = models.DateField(verbose_name='Nascimento', blank=True, null=True )

    def __str__(self):
        return self.nome