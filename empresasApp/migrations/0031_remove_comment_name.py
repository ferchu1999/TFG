# Generated by Django 3.1.5 on 2021-03-12 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresasApp', '0030_auto_20210310_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
