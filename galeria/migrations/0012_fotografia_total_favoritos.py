# Generated by Django 4.1.7 on 2023-02-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0011_fotografia_favorito'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='total_favoritos',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
