from django.db.models import Prefetch

from app.albums.models import Album, Track
from app.artists.models import Artist


def get_all_artists():
    return Artist.objects.all().order_by("name")

def get_artist_albums(artist_id: int):
    tracks_qs = Track.objects.select_related('media_type', 'genre')
    return Album.objects.filter(artist_id=artist_id).order_by('title').prefetch_related(
        Prefetch('album', queryset=tracks_qs)
    )

def exists_artist(artist_id: int):
    return Artist.objects.filter(id=artist_id).exists()