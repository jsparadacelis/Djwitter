# Generated by Django 2.1.2 on 2018-12-12 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20181212_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='seguidor',
        ),
    ]
