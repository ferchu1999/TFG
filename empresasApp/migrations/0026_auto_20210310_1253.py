# Generated by Django 3.1.5 on 2021-03-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresasApp', '0025_auto_20210310_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
