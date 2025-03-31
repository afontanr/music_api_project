import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from app.artists.models import Artist


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_artists(db):
    def _create(n):
        return Artist.objects.bulk_create([
            Artist(name=f"Artist {i}") for i in range(1, n+1)
        ])
    return _create


@pytest.mark.django_db
def test_get_all_artists_success(api_client, create_artists):
    """Test to verify that endpoint retrives artist correctly"""
    create_artists(5)
    url = reverse("artists-list")

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert "results" in response.data
    assert len(response.data["results"]) > 0
    assert response.data["results"][0]["name"] == "A Cor Do Som"


@pytest.mark.django_db
def test_pagination(api_client, create_artists):
    """Test to verify correct pagination"""
    create_artists(15)  # Más de una página de resultados
    url = reverse("artists-list") + "?page=2"

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert "results" in response.data
    assert "pagination" in response.data
    assert response.data["pagination"]["current_page"] == 2


@pytest.mark.django_db
def test_invalid_page(api_client):
    """Test que verifica que pedir una página inválida devuelve error 404."""
    url = reverse("artists-list") + "?page=999"  # No hay tantas páginas

    response = api_client.get(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["detail"] == "Page not found"