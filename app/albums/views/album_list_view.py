from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView

from app.albums import services
from app.albums.serializers import AlbumSerializer
from app.pagination import CustomPagination


class AlbumListView(ListAPIView):
    pagination_class = CustomPagination
    serializer_class = AlbumSerializer

    @swagger_auto_schema(operation_description="Get all albums",
                         responses={
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
        return services.get_albums_with_tracks()
