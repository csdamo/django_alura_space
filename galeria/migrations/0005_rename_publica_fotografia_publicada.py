# Generated by Django 4.1.7 on 2023-02-20 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_publica'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='publica',
            new_name='publicada',
        ),
    ]
