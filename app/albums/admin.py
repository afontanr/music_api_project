from django.contrib import admin

from app.albums.models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('id',)
