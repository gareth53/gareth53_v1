import datetime
from django.db import models
from gareth53.apps.musicartists.models import Track, Artist

class User(models.Model):
    """
    this links to a last.fm user
    """
    lastfm_username = models.CharField(max_length=255)
    profile_url = models.URLField(verify_exists=False)
    profile_pic = models.CharField(max_length=255)
    feed_url = models.URLField(verify_exists=False)
    slug = models.SlugField()
    def __unicode__(self):
        return u'%s' % (self.lastfm_username)

class Scrobble(models.Model):
    """
    scrobbles are auto-created by pulling an XML feed from last.fm
    """
    user = models.ForeignKey(User)
    date_time = models.DateTimeField(null=True)
    date_retrieved = models.DateTimeField(null=True)
    track = models.ForeignKey(Track, null=True, blank=True)

    lastfm_track_title = models.CharField(max_length=255, help_text="Usually over-written by a ForeignKey link to a track")
    lastfm_artist = models.CharField(max_length=255, help_text="Usually over-written by a ForeignKey link to an artist")
    lastfm_track_url = models.URLField(verify_exists=False, null=True, blank=True)
    def __unicode__(self):
        return u'%s - %s "%s"' % (self.date_time, self.lastfm_artist, self.lastfm_track_title)