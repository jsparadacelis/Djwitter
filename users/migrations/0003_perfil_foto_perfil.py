# Generated by Django 2.1.3 on 2018-12-06 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181116_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='foto_perfil',
            field=models.ImageField(default=None, upload_to='media/perfil'),
        ),
    ]
