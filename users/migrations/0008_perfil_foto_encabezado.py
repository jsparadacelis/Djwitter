# Generated by Django 2.1.3 on 2018-12-06 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181206_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='foto_encabezado',
            field=models.ImageField(null=True, upload_to='media/encabezado'),
        ),
    ]