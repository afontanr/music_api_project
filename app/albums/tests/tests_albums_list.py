import pytest
from django.urls import reverse
from rest_framework import status
from app.artists.models import Artist
from app.albums.models import Album, Track, MediaType, Genre


@pytest.mark.django_db
class TestAlbumListView:

    def setup_method(self):
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

        self.url = reverse("albums-list")

    def test_get_albums_success(self, client):
        """Endpoint return all albums correctly"""
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["results"][0]["title"] == "...And Justice For All"
        assert response.json()["results"][0]["artist"] == 50

    def test_pagination(self, client):
        """Pagination works right"""
        for i in range(15):
            Album.objects.create(title=f"Album {i}", artist=self.artist)

        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert "pagination" in response.json()
        assert "results" in response.json()
        assert len(response.json()["results"]) <= 10

    def test_invalid_page(self, client):
        """If not exists a page returns 404"""
        response = client.get(self.url + "?page=9999")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["detail"] == "Page not found"
