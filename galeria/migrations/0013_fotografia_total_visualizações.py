# Generated by Django 4.1.7 on 2023-02-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0012_fotografia_total_favoritos'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='total_visualizações',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
