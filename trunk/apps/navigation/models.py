from django.db import models

class NavigationLink(models.Model):
    text = models.CharField(max_length=200)
    link = models.CharField(max_length=75)
    rank = models.IntegerField()
        
    def __unicode__(self):
        return u'%s' %(self.text)

class Navigation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    links = models.ManyToManyField(NavigationLink)
    def __unicode__(self):
        return "%s" % self.name
