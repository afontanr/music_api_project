from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView

from app.albums.serializers import AlbumSerializer
from app.artists.services import exists_artist, get_artist_albums
from app.pagination import CustomPagination
from app.validation import validate_int_param


class ArtistAlbumsView(ListAPIView):
    pagination_class = CustomPagination
    serializer_class = AlbumSerializer

    @swagger_auto_schema(operation_description="Get all albums of an artist",
                         responses={
                             400: openapi.Response(
                                 description="Page not found",
                                 schema=openapi.Schema(
                                     type=openapi.TYPE_OBJECT,
                                     properties={
                                         'detail': openapi.Schema(
                                             type=openapi.TYPE_STRING,
                                             example="Id must be a positive integer",
                                         )
                                     }
                                 )
                             ),
                             404: openapi.Response(
                                 description="Page not found",
                                 schema=openapi.Schema(
                                     type=openapi.TYPE_OBJECT,
                                     properties={
                                         'detail': openapi.Schema(
                                             type=openapi.TYPE_STRING,
                                             example="Page not found",
                                         )
                                     }
                                 )
                             )
                         }
                         )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        artist_id = self.kwargs.get('artist_id')
        validate_int_param(artist_id)
        if not exists_artist(artist_id):
            raise NotFound('Artist not found')

        return get_artist_albums(artist_id)
