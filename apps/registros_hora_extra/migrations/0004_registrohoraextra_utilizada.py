# Generated by Django 3.2.8 on 2021-10-22 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros_hora_extra', '0003_registrohoraextra_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='utilizada',
            field=models.BooleanField(default=False),
        ),
    ]
