# Generated by Django 3.1.5 on 2021-03-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresasApp', '0016_remove_empresa_cif'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='CIF',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
