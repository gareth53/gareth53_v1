from django.conf.urls.defaults import *
from django.contrib.syndication.feeds import Feed

from gareth53.apps.podcast.views import *
from gareth53.apps.podcast.models import *

#feeds = {
#    'posts': AllPosts,
#    'categories' : CategorisedPosts,
#}

urlpatterns = patterns('',
     (r'^$', podcastHub),
     (r'^episode(?P<season_number>(\d+))-(?P<episode_number>(\d)+).html$', podcastEpisode),
     (r'^podcast-feed.xml', podcastFeed),
     (r'^artists.html$', podcastArtists),
)