from rest_framework import serializers

from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=120 )

    class Meta:
        model = Artist
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = data['name'].strip().title()
        return data
