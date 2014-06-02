from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    official_URL = models.URLField(blank=True, null=True)
    wikipedia_URL = models.URLField(blank=True, null=True)
    slug = models.SlugField()
    def __unicode__(self):
        return u'%s' %(self.name)

class Album(models.Model):
    album_artist = models.ForeignKey(Artist, null=True, help_text="Leave blank for 'Various Artist' compilations")
    title = models.CharField(max_length=255)
    amazon_URL = models.URLField(blank=True, null=True)
    slug = models.SlugField()
    release_year = models.CharField("Year of release", max_length=4, blank=True)
    def __unicode__(self):
        return u'%s' %(self.title)

class Track(models.Model):
    track_title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, blank=True, null=True)
    artist = models.ForeignKey(Artist, null=True)
    track_year = models.CharField("Year of release", max_length=4, blank=True, help_text="If no year is supplied, year is inherited from the Album's year")
    # META over-rides the inherited year from the album release (for compilations and similar)
    image_large = models.URLField(blank=True, null=True, verify_exists=False)
    image_medium = models.URLField(blank=True, null=True, verify_exists=False)
    image_small = models.URLField(blank=True, null=True, verify_exists=False)

    def __unicode__(self):
        return u'%s' %(self.track_title)
