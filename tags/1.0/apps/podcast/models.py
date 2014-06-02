from django.db import models
from django.contrib.syndication.feeds import Feed
from django.contrib.auth.models import User

from gareth53 import settings

"""
class Channel(models.Model):
	title
	link
	copyright
	subtitle
	author(s) (help_text="Separate names with a comma")
	summary
	image (300 x 300 pixels)
	explicit (yes/no)
	description
	owner (from contrib.auth.User)
	category (from Music/ 
"""
class Artist(models.Model):
    name = models.CharField(max_length=50)
    official_URL = models.URLField(blank=True, null=True)
    wikipedia_URL = models.URLField(blank=True, null=True)
    slug = models.SlugField()
    def __unicode__(self):
        return u'%s' %(self.name)

class Album(models.Model):
    album_artist = models.ForeignKey(Artist, null=True, help_text="Leave blank for 'Various Artist' compilations")
    title = models.CharField(max_length=100)
    amazon_URL = models.URLField(blank=True, null=True)
    slug = models.SlugField()
    release_year = models.CharField("Year of release", max_length=4, blank=True)
    artwork = models.ImageField(upload_to='img/podcast/album-artwork',blank=True)
    def __unicode__(self):
        return u'%s' %(self.title)

class Track(models.Model):
    track_title = models.CharField(max_length=30)
    album = models.ForeignKey(Album, blank=True, null=True)
    artist = models.ForeignKey(Artist, null=True)
    track_year = models.CharField("Year of release", max_length=4, blank=True, help_text="If no year is supplied, year is inherited from the Album's year")
    # META over-rides the inherited year from the album release (for compilations and similar)
    def __unicode__(self):
        return u'%s' %(self.track_title)
    def save(self):
        if self.track_year:
            pass
        else:
            if self.album and self.album.release_year:
                self.track_year = self.album.release_year
        super(Track, self).save()

class TrackListing(models.Model):
    track_number = models.IntegerField(max_length=3)
    track = models.ForeignKey('Track')
    episode = models.ForeignKey('Episode')
    def __unicode__(self):
        return u'%s - "%s"' % (self.track.artist.name, self.track)
    
class Episode(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200, blank=True, null=True, help_text='displayed on the site as an abstract')
    cover_image = models.ImageField(upload_to='img/podcast/covers',blank=True, help_text='300x300 pixels, around 15Kb in size')
    image_description = models.CharField(max_length=50, help_text="Used as the 'img' alt value, Limited to 50 characters")
    episode_number = models.IntegerField()
    season_number = models.IntegerField()
    description =  models.CharField(max_length=200, help_text='only used in the feed')
    media_URL = models.URLField(verify_exists=False, blank=True, null=True, help_text='Should be an absolute URL')
    enhanced_media_URL = models.URLField(verify_exists=False, blank=True, null=True, help_text='An enhanced media fie (for iTunes). Should be an absolute URL')
    download_duration = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=8, blank=True, null=True, help_text='In the format "hh:mm:ss", or just "mm:ss" if shorter than 1 hour')
    
    primary_keywords =  models.CharField(max_length=100, blank=True, null=True, help_text='only used in the feed, overrides artist names')
    # META upto 10 words, separated by SPACES - these appear in the RSS feed

    secondary_keywords =  models.TextField(blank=True, null=True, help_text='published on the site, for the google juice')
    # META published on the web page accompanying this epsiode, but not the RSS feed

    author_name =  models.CharField(max_length=50)
    author_email = models.EmailField("Author's email address")
    author = models.ForeignKey(User,blank=True, null=True)
    body_html = models.TextField()
    notes_and_errata = models.TextField("Notes & errata", blank=True, null=True)
    pub_date = models.DateTimeField('Date published')
    enable_comments = models.BooleanField(default=True, help_text='currently unused')
    slug = models.SlugField(blank=True, null=True)
    PUB_STATUS = (
        (0, 'Draft'),
        (1, 'Published'),
    )
    status = models.IntegerField(choices=PUB_STATUS, default=0)
    
    def get_artists(self):
        from gareth53.apps.podcast.utils import get_featured_artists
        artists_str = get_featured_artists(self)
        return artists_str.split(", ")

    def save(self, *args, **kwargs):
        # try to add missing values, based on duration
        if self.duration:
            from utils import untimeify
            self.download_duration = untimeify(self.duration)
        if not self.duration and self.download_duration:
            from utils import timeify
            self.duration = timeify(self.download_duration)
        # fall back to defaults
        if self.download_duration is None:
            self.download_duration = 0
        if self.duration is None:
            self.duration = "00:00"
        super(Episode, self).save(*args, **kwargs)    

    def get_absolute_url(self):
        return '/podcast/episode%s-%s.html' % (self.season_number, self.episode_number)
    
    def __unicode__(self):
        return u'%s' %(self.title)