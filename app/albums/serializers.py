from rest_framework import serializers
from .models import Album, Track

class TrackSerializer(serializers.ModelSerializer):
    media_type = serializers.CharField(source='media_type.name', read_only=True)
    genre = serializers.CharField(source='genre.name', read_only=True)

    class Meta:
        model = Track
        fields = (
            'id', 'name', 'composer', 'milliseconds', 'bytes', 'unit_price',
            'media_type', 'genre'
        )

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True, source='album')

    class Meta:
        model = Album
        fields = ('id', 'title', 'artist', 'tracks')


class AlbumSummarySerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name', read_only=True)
    total_tracks = serializers.IntegerField(read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'title', 'artist_name', 'total_tracks')

