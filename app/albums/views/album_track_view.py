from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView

from app.albums import services
from app.albums.serializers import AlbumSerializer
from app.validation import validate_int_param


class AlbumTracksView(RetrieveAPIView):
    serializer_class = AlbumSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'album_id'

    @swagger_auto_schema(operation_description="Get all tracks of an album",
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
                         })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self):
        album_id = self.kwargs.get(self.lookup_url_kwarg)
        validate_int_param(album_id)
        album = services.get_album_with_tracks(album_id)
        if album is None:
            raise NotFound(detail="Album not found")
        return album
