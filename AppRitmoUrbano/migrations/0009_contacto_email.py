# Generated by Django 4.0.3 on 2022-06-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRitmoUrbano', '0008_rename_nombre_curso_clase'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
