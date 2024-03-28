# Generated by Django 5.0.2 on 2024-03-28 00:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas_app', '0008_alter_formadepago_options_formadepago_cuenta_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField(verbose_name='Monto')),
                ('fecha', models.DateField(null=True, verbose_name='Fecha')),
                ('descripción', models.CharField(blank=True, max_length=300, verbose_name='Descripción')),
                ('formaDePago', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finanzas_app.formadepago', verbose_name='Forma de pago')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finanzas_app.perfilusuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
            },
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField(verbose_name='Monto')),
                ('fecha', models.DateField(null=True, verbose_name='Fecha')),
                ('descripción', models.CharField(blank=True, max_length=300, verbose_name='Descripción')),
                ('cuenta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finanzas_app.cuenta', verbose_name='Cuenta asociada')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finanzas_app.perfilusuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
            },
        ),
    ]
