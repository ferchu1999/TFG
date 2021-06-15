# Generated by Django 3.1.5 on 2021-03-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresasApp', '0003_auto_20210228_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='tipo_empresa',
            field=models.CharField(blank=True, choices=[('pequeña empresa', 'Pequeña Empresa'), ('mediana empresa', 'Mediana Empresa')], max_length=255, verbose_name='Tipo de Empresa'),
        ),
    ]
