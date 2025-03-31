"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from app.albums.views.album_list_view import AlbumListView
from app.albums.views.album_summary_view import AlbumSummaryView
from app.albums.views.album_track_view import AlbumTracksView
from app.artists.views.artist_album_view import ArtistAlbumsView
from app.artists.views.artist_list_view import ArtistListView
from app.converters import AnyIntConverter

schema_view = get_schema_view(
    openapi.Info(
        title="Music API",
        default_version='v1',
        description="Documentation of the API for albums, artists and track",
        contact=openapi.Contact(email="afontanr@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

register_converter(AnyIntConverter, 'anyint')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/artists/', ArtistListView.as_view(), name='artists-list'),
    path('api/artists/<anyint:artist_id>/albums/', ArtistAlbumsView.as_view(), name='artist-albums'),
    path('api/albums/', AlbumListView.as_view(), name='albums-list'),
    path('api/albums/<anyint:album_id>/tracks/', AlbumTracksView.as_view(), name='album-tracks'),
    path('api/albums/summary/', AlbumSummaryView.as_view(), name='album-summary'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
