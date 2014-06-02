from django.db import models

class User(models.Model):
    """
    this links to a flickr profile
    """
    name = models.CharField(max_length=50)
    profile_url = models.URLField(verify_exists=False, null=True)
    profile_pic = models.CharField(max_length=255, null=True, blank=True)
    feed_url = models.URLField(verify_exists=False)
    slug = models.SlugField()
    def __unicode__(self):
        return u'%s' % (self.name)

#
# http://api.flickr.com/services/rest/?method=flickr.people.getPublicPhotos&api_key=e31c3520bb3e4dafc12798e154fac40f&user_id=40517523@N00&per_page=50

#<?xml version="1.0" encoding="utf-8" ?>
#<rsp stat="ok">
#<photos page="1" pages="4" perpage="50" total="200">
#	<photo  id="3497119418"
#    	owner="40517523@N00"
#    	secret="94e61e1619"
#    	server="3300"
#    	farm="4"
#    	title="Sunrise, Kumlubuk"
#    	ispublic="1"
#    	isfriend="0" isfamily="0" />
#</photos>
#</rsp>
#
# medium image URL: http://farm4.static.flickr.com/3300/3497119418_94e61e1619.jpg?v=0
# image thumbnail:  http://farm4.static.flickr.com/3300/3497119418_94e61e1619_s.jpg

class Image(models.Model):
    """
    Images are auto-created by pulling an XML feed from flickr.com
    """
    date_retrieved = models.DateTimeField()
    photo_id = models.CharField(max_length=100, blank=True)
    photo_secret = models.CharField(max_length=100, blank=True)
    server = models.CharField(max_length=100, blank=True)
    server_farm = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return self.title
        
    @property
    def absolute_url(self):
        return "http://farm%s.static.flickr.com/%s/%s_%s.jpg" % (self.serself.idver_farm, self.server, self.photo_id, photo_secret)