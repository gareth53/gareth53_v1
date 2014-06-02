from django.contrib import admin
from gareth53.apps.articles.models import *

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',) }
    list_display = ('title', 'pub_date', 'status',)        
    search_fields = ['title', 'body_html']
    list_filter = ('title', 'pub_date', 'status')
    class Media:
        js = (
                    '/assets/js/tiny_mce/tiny_mce.js',
                    '/assets/js/tiny_mce/textareas.js',
                )

class PromoAdmin(admin.ModelAdmin):

    def link(obj):
        if obj.headline_link:
            return obj.headline_link
        if obj.article_link:
            return obj.article_link
        return "None"
        
    list_display = ('name', 'headline', link,)
    class Media:
        js = (
                    '/assets/js/tiny_mce/tiny_mce.js',
                    '/assets/js/tiny_mce/textareas.js',
                )




admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
admin.site.register(Promo, PromoAdmin)