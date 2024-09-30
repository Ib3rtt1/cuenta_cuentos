# Generated by Django 5.0.3 on 2024-09-30 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cuentos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuento',
            name='contenido',
        ),
        migrations.RemoveField(
            model_name='cuento',
            name='fecha_publicacion',
        ),
        migrations.AddField(
            model_name='cuento',
            name='archivo_pdf',
            field=models.FileField(blank=True, null=True, upload_to='cuentos/'),
        ),
    ]
