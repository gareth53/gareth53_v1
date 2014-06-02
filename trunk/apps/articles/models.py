from django.db import models
from gareth53.apps.navigation.models import Navigation

class Promo(models.Model):
    name = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    headline_link = models.CharField(max_length=200, help_text='Can be an absolute link, or a relative, over-rides the article link', blank=True, null=True)
    body_html = models.TextField()
    article_link = models.ForeignKey('Article', blank=True, null=True)
    def __unicode__(self):
        return u'%s' %(self.name)

class ArticleCategory(models.Model):
    title = models.CharField(max_length=200)
    pages_title = models.CharField(max_length=200, help_text='The TITLE you want to appear at the top of each page in this category')
    mainNavigation = models.ForeignKey(Navigation, blank=True, null=True, related_name='main_nav')
    footerNavigation = models.ForeignKey(Navigation, blank=True, null=True, related_name = 'footer_nav')
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True, help_text="Admin notes")
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Article Categories"

class Article(models.Model):
    class Meta:
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
        verbose_name_plural = 'articles'

    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body_html = models.TextField()
    pod_promos = models.ForeignKey(Promo, blank=True, null=True)
    category = models.ForeignKey(ArticleCategory, blank=True, null=True, help_text="this will affect the url, like so: /<category>/<article-slug> unless you set the category to be 'Master'")
    pub_date = models.DateTimeField('Date published')
    PUB_STATUS = (
        (0, 'Draft'),
        (1, 'Published'),
    )
    status = models.IntegerField(choices=PUB_STATUS, default=0)
    
    def __unicode__(self):
        return u'%s' %(self.title)
    
    def get_absolute_url(self):
        if self.category:
            cat = '%s/' % self.category.slug
        else:
            cat = ''
        return "/%s%s.html" % (cat, self.slug)