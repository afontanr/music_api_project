from django.contrib import admin
from .models import Artist

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id',)