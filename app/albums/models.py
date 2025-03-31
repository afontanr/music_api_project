from django.db import models

from app.artists.models import Artist

class Album(models.Model):
    id = models.AutoField(primary_key=True, db_column='AlbumId')
    title = models.CharField(max_length=160, db_column='Title')
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        db_column='ArtistId',
        related_name='albums'
    )

    class Meta:
        db_table = 'albums'
        managed = False

    def __str__(self):
        return self.title


class MediaType(models.Model):
    id = models.AutoField(primary_key=True, db_column='MediaTypeId')
    name = models.CharField(max_length=120, db_column='Name')

    class Meta:
        db_table = 'media_types'
        managed = False

    def __str__(self):
        return self.name

class Genre(models.Model):
    id = models.AutoField(primary_key=True, db_column='GenreId')
    name = models.CharField(max_length=120, db_column='Name')

    class Meta:
        db_table = 'genres'
        managed = False

    def __str__(self):
        return self.name

class Track(models.Model):
    id = models.AutoField(primary_key=True, db_column='TrackId')
    name = models.CharField(max_length=200, db_column='Name')
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        db_column='AlbumId',
        related_name='album'
    )
    media_type = models.ForeignKey(
        MediaType,
        on_delete=models.CASCADE,
        db_column='MediaTypeId',
        related_name='tracks'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        db_column='GenreId',
        related_name='tracks'
    )
    composer = models.CharField(max_length=220, db_column='Composer')
    milliseconds = models.IntegerField(db_column='Milliseconds')
    bytes = models.IntegerField(db_column='Bytes')
    unit_price = models.FloatField(db_column='UnitPrice')

    class Meta:
        db_table = 'tracks'
        managed = False

