# Generated by Django 2.1.2 on 2018-12-12 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_perfil_foto_encabezado'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='seguidores',
            field=models.ManyToManyField(related_name='_perfil_seguidores_+', to='users.Perfil'),
        ),
    ]
