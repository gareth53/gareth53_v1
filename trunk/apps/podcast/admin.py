from django.contrib import admin

from gareth53.apps.podcast.models import *
from gareth53.apps.podcast.utils import get_featured_artists
from gareth53 import settings
        
class ArtistAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'wikipedia_URL', 'official_URL')
    prepopulated_fields = {'slug': ('name',) }
    search_fields = ['name', ]
    
class AlbumAdmin(admin.ModelAdmin):
    def get_artist(obj):
        if obj.album_artist:
            return obj.album_artist.name
        else:
            return "Various"
    list_display = ('title', get_artist, 'release_year')
    prepopulated_fields = {'slug': ('title',) }
    search_fields = ['title', 'album_artist']
    list_filter = ('release_year',)

class TrackAdmin(admin.ModelAdmin):
    def track_year(obj):
        if obj.track_year:
            return obj.track_year
        elif obj.album and obj.album.release_year:
            return obj.album.release_year
        else:
            return ""
    def track_artist(obj):
        if obj.artist:
            return obj.artist.name
        else:
            return "Unknown"
    list_display = ('track_title', track_artist,'album', track_year)
    search_fields = ['track_title', 'artist', 'album',]
    list_filter = ('track_year',)

class TracklistingInline(admin.StackedInline):
    model = TrackListing

class EpisodeAdmin(admin.ModelAdmin):
    inlines = [
        TracklistingInline,
    ]
    def author_display(obj):
        if obj.author:
            return u'%s %s' % (obj.author.first_name, obj.author.last_name)
        else:
            return "Not set"
    
    def episode_number(obj):
        return obj.episode_number
    episode_number.short_description = "Ep"
    
    def season_number(obj):
        return obj.season_number
    season_number.short_description = "Season"
    
    def featured_artists(obj):
        TrackListings = TrackListing.objects.all().filter(episode=obj).order_by('track_number')
        if TrackListings is not None:
            feat_tracks = ""
            first = True
            for listing in TrackListings:
                if first:
                    feat_tracks = listing.track.artist
                else:
                    feat_tracks = "%s, %s" % (feat_tracks, listing.track.artist)
                first = False
            return feat_tracks
        else:
            return "No tracks"
        
        
    def cover_image(obj):
        if obj.cover_image:
            return u'<img src="/assets/%s" alt="%s" width="75" height="75" style="border:1px solid #666" />' % (obj.cover_image, obj.image_description)
        else:
            return ""
    cover_image.allow_tags = True
    def pub_date(obj):
        return obj.pub_date.strftime('%b, %y')

    ordering = ('-pub_date',)
    get_latest_by = 'pub_date'
    list_display = (cover_image,'title',season_number,episode_number, pub_date,'status',author_display, get_featured_artists)
    list_display_links = ('title',)
    search_fields = ['title','body_html']
    prepopulated_fields = {'slug': ('title',) }
    list_filter = ('season_number','pub_date','status',)
    fieldsets = (
        (None,
            {
            'fields':(
                'title',
                'slug',
                'subtitle',
                'status',
                'pub_date',
                'author',
                'episode_number',
                'season_number',
                'cover_image',
                'image_description',
                'media_URL',
                'enhanced_media_URL',
                'duration',
                'body_html',
                'notes_and_errata',
                'enable_comments'
                )
            }
        ),
        ('RSS Feed Metadata',
            {
            'fields':(
                'description',
                'primary_keywords',
                'secondary_keywords'
            ),
            'classes': ['collapse'],
            }
        ),
    ) 
    class Media:
        js = (
                    '/assets/js/tiny_mce/tiny_mce.js',
                    '/assets/js/tiny_mce/textareas.js',
                    '/assets/js/jquery-1.2.1.min.js',
                    '/assets/js/admin/podcast-episode.js',
                )
        css = {
                    "all": ("/assets/css/custom-admin.css",)
                }

admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(TrackListing)