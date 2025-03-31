import pytest
from django.urls import reverse
from rest_framework import status

from app.albums.models import Album
from app.artists.models import Artist


@pytest.mark.django_db
class TestAlbumSummaryView:

    def setup_method(self):
        self.artist = Artist.objects.create(name="The Beatles")
        self.album1 = Album.objects.create(title="Abbey Road", artist=self.artist)
        self.album2 = Album.objects.create(title="Let It Be", artist=self.artist)

        self.url = reverse("album-summary")

    def test_get_album_summary_success(self, client):
        """Endpoint return correctly the summary of the albums"""
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()["results"]) == 10
        assert response.json()["results"][0]["title"] == "...And Justice For All"
        assert response.json()["results"][0]["artist_name"] == "Metallica"

    def test_album_summary_pagination(self, client):
        """Pagination works correctly"""
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert "pagination" in response.json()
        assert "results" in response.json()
        assert len(response.json()["results"]) <= 10
