# Generated by Django 5.0.3 on 2024-03-13 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestorEstudiantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='apellido',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nota',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
    ]