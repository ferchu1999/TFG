# Generated by Django 3.1.5 on 2021-03-16 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProveedoresApp', '0002_auto_20210316_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedoresmodel',
            name='img_productos',
        ),
    ]
