# Generated by Django 4.0.3 on 2022-06-07 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRitmoUrbano', '0005_alter_curso_observaciones_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='dias',
            new_name='dia',
        ),
        migrations.AlterField(
            model_name='curso',
            name='horario',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/profesores'),
        ),
    ]
