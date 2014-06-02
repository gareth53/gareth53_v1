from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

from gareth53.views import * 
from gareth53.apps.articles.views import *
from gareth53.apps.articles.models import Article

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', homepage),
    (r'^blog/', include('gareth53.apps.blog.urls')),
    (r'^podcast/', include('gareth53.apps.podcast.urls')),
    
    # articles (check slugs)
     (r'^(?P<category>[\w\-]+)/(?P<slug>[\w\-]+).html$', ArticlePageInCategory),
     (r'^(?P<slug>[\w\-]+).html$', ArticlePage),

    # Django Docs, from: http://smileychris.tactful.co.nz/
#     (r'^admin/', include('gareth53.apps.django_docs.urls')),
    # Admin:
     (r'^admin/(.*)', admin.site.root),



)

if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }), 
    ) 
