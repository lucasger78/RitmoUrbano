# Generated by Django 4.0.3 on 2022-06-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRitmoUrbano', '0004_alter_alumno_observaciones_alter_curso_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='observaciones',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='observaciones',
            field=models.TextField(),
        ),
    ]