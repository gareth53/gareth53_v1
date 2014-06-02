from django.conf.urls.defaults import *
from gareth53.apps.lastfm.views import *

urlpatterns = patterns('',
     (r'^$', all_scrobbles),
     (r'^(?P<username>([\w\-]+)).html$', all_scrobbles),
)