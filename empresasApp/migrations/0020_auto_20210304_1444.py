# Generated by Django 3.1.5 on 2021-03-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresasApp', '0019_empresa_web'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='categoria',
        ),
        migrations.AddField(
            model_name='empresa',
            name='categoria',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='categoria_empresa',
        ),
    ]
