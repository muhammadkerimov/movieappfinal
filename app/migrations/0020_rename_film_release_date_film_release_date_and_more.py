# Generated by Django 5.1.1 on 2024-09-09 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_series_series_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='film_release_date',
            new_name='release_date',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='series_release_date',
            new_name='release_date',
        ),
    ]
