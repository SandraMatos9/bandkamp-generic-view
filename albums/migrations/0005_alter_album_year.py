# Generated by Django 4.0.7 on 2023-06-20 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_alter_album_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.PositiveSmallIntegerField(verbose_name=2023),
        ),
    ]
