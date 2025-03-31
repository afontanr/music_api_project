import pytest
from rest_framework.test import APIClient
from rest_framework import status
from app.artists.models import Artist
from app.albums.models import Album

endpoint = "/api/artists/{}/albums/"

@pytest.fixture
def api_client():
    return APIClient()

def setup_method(self):
    self.client = APIClient()
    self.artist = Artist.objects.create(name="The Beatles")
    self.album1 = Album.objects.create(title="Abbey Road", artist=self.artist)


@pytest.mark.django_db
def test_get_artist_albums_success(client):
    """Must retrieve all albums of an artist"""
    artist = Artist.objects.create(name="The Beatles")
    Album.objects.create(title="Abbey Road", artist=artist)

    response = client.get(f"/api/artists/{artist.id}/albums/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_invalid_artist_id(client):
    """Must retrieve 400 if ID is not positive"""
    response = client.get("/api/artists/-1/albums/")
    assert response.status_code == 400

@pytest.mark.django_db
def test_artist_not_found(client):
    """Retrieve 404 if artist doesn't exist."""
    response = client.get("/api/artists/999999/albums/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["detail"] == "Artist not found"

@pytest.mark.django_db
def test_pagination(client):
    """Check correct pagination."""
    artist = Artist.objects.create(name="The Beatles")
    Album.objects.create(title="Abbey Road", artist=artist)
    Album.objects.create(title="Abbey Road", artist=artist)
    Album.objects.create(title="Abbey Road", artist=artist)
    Album.objects.create(title="Abbey Road", artist=artist)
    Album.objects.create(title="Abbey Road", artist=artist)
    Album.objects.create(title="Abbey Road", artist=artist)
    Album.objects.create(title="Abbey Road", artist=artist)
    Album.objects.create(title="Abbey Road", artist=artist)
    Album.objects.create(title="Abbey Road", artist=artist)
    Album.objects.create(title="Abbey Road", artist=artist)
    Album.objects.create(title="Abbey Road", artist=artist)
    response = client.get(f"/api/artists/{artist.id}/albums/" + "?page=1&page_size=1")
    assert response.status_code == status.HTTP_200_OK
    assert "pagination" in response.data
    assert response.data["pagination"]["total_items"] == 11
    assert response.data["pagination"]["total_pages"] == 2
