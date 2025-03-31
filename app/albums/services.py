from django.db.models import Prefetch, Count

from app.albums.models import Album, Track


def get_albums_with_tracks():
    tracks_qs = Track.objects.select_related('media_type', 'genre')
    return (Album.objects.all()
    .order_by('title')
    .prefetch_related(
        Prefetch('album', queryset=tracks_qs)
    ))


def get_album_with_tracks(album_id: int):
    tracks_qs = Track.objects.select_related('media_type', 'genre')
    return (Album.objects
            .filter(id=album_id)
            .prefetch_related(
                Prefetch('album', queryset=tracks_qs)
            )
            .first())


def get_album_summary():
    return (Album.objects
            .order_by('title')
            .select_related('artist')
            .only('id', 'title', 'artist__name')
            .annotate(total_tracks=Count('album')))
