# Generated by Django 4.1 on 2024-09-11 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_actor_cinemahall_genre_movie_actors_movie_genres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemahall',
            old_name='seats_row',
            new_name='seats_in_row',
        ),
    ]
