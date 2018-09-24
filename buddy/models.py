from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=300)
    album_title = models.CharField(max_length=3000)
    genre = models.CharField(max_length=300)
    album_logo = models.CharField(max_length=3000)

    def __str__(self):
        return self.artist + ' · ' + self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=300)
    song_title = models.CharField(max_length=300)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
