# Generated by Django 3.1.5 on 2021-03-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresasApp', '0018_auto_20210304_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='web',
            field=models.URLField(null=True, verbose_name='Pagina web'),
        ),
    ]
