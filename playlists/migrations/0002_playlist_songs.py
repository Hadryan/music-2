# Generated by Django 3.1.3 on 2020-11-02 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_delete_playlist'),
        ('playlists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist_songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='playlists.playlist')),
                ('songs', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='songs.song')),
            ],
        ),
    ]