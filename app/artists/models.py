from django.db import models


class Artist(models.Model):
    id = models.AutoField(primary_key=True, db_column='ArtistId')
    name = models.CharField(max_length=120, db_column='Name')

    class Meta:
        managed = False
        db_table = 'artists'