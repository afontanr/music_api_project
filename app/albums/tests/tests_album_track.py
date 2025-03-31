import pytest
from django.urls import reverse
from rest_framework import status
from app.artists.models import Artist
from app.albums.models import Album, Track, MediaType, Genre


@pytest.mark.django_db
class TestAlbumTracksView:

    def setup_method(self):
        """Crea datos de prueba antes de cada test."""
        self.artist = Artist.objects.create(name="The Beatles")
        self.album = Album.objects.create(title="Abbey Road", artist=self.artist)

        media_type = MediaType.objects.create(name="CD")
        genre = Genre.objects.create(name="Rock")

        self.track = Track.objects.create(
            name="Come Together",
            album=self.album,
            media_type=media_type,
            genre=genre,
            composer="John Lennon, Paul McCartney",
            milliseconds=259000,
            bytes=8500000,
            unit_price=1.29
        )

        self.url = reverse("album-tracks", kwargs={"album_id": self.album.id})
        self.invalid_url = reverse("album-tracks", kwargs={"album_id": 9999})

    def test_get_album_tracks_success(self, client):
        """Endpoint returns correctly track of the album"""
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["id"] == self.album.id
        assert response.json()["title"] == "Abbey Road"
        assert len(response.json()["tracks"]) == 1
        assert response.json()["tracks"][0]["name"] == "Come Together"

    def test_invalid_album_id(self, client):
        """Endpoint returns 400 if album_id is not a positive integer"""
        response = client.get(reverse("album-tracks", kwargs={"album_id": -1}))
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_album_not_found(self, client):
        """If album doesn't exist, returns 404.'"""
        response = client.get(self.invalid_url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["detail"] == "Album not found"
