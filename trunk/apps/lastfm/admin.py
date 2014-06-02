from django.contrib import admin
from gareth53.apps.lastfm.models import *

class ScrobbleAdmin(admin.ModelAdmin):
    list_display = ('lastfm_track_title', 'date_time', 'user', 'lastfm_artist', )        
    search_fields = ['lastfm_title', 'lastfm_track_title']
    list_filter = ('user', 'lastfm_artist',)

class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('lastfm_username',) }

admin.site.register(User, UserAdmin)
admin.site.register(Scrobble, ScrobbleAdmin)
