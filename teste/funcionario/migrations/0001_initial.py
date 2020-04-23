# Generated by Django 3.0.5 on 2020-04-20 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('inativo', models.BooleanField(default=False)),
                ('nascimento', models.DateField(blank=True, null=True, verbose_name='Nascimento')),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cargo.Cargo', verbose_name='Cargo')),
            ],
        ),
    ]
