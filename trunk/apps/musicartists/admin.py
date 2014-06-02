from django.contrib import admin
from gareth53.apps.musicartists.models import *

class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',) }

class TrackAdmin(admin.ModelAdmin):
    def artist(obj):
        if obj.artist:
            return obj.artist.name
        else:
            return "Unknown"

    list_display = ('track_title', 'track_year', artist,)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title','album_artist','release_year',)
    prepopulated_fields = {'slug': ('title',) }

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
