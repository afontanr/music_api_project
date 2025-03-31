from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView

from app.pagination import CustomPagination
from app.artists.serializers import ArtistSerializer
from app.artists.services import get_all_artists


class ArtistListView(ListAPIView):
    """
    Endpoint in order to list artists.

    Retrieve a list of artists.
    """
    pagination_class = CustomPagination
    serializer_class = ArtistSerializer

    @swagger_auto_schema(operation_description="Get all artists",
                         responses={
                             404: openapi.Response(
                                 description="Page not found",
                                 schema=openapi.Schema(
                                     type=openapi.TYPE_OBJECT,
                                     properties={
                                         'detail': openapi.Schema(
                                             type=openapi.TYPE_STRING,
                                             example="Invalid page",
                                         )
                                     }
                                 )
                             )
                         }
                         )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return get_all_artists()
