from django.conf.urls.defaults import *
from gareth53.apps.articles.views import *
from gareth53.apps.articles.models import Article

urlpatterns = patterns('',
     (r'^(?P<category>[\w\-]+)/(?P<slug>[\w\-]+).html$', ArticlePageInCategory),
     (r'^(?P<slug>[\w\-]+).html$', ArticlePage),
)