from django.contrib import admin
from gareth53.apps.navigation.models import *

class NavigationAdmin(admin.ModelAdmin):
    def links(obj):
        returnStr = ""
        separator = ""
        navLinks = obj.links.all().order_by('rank')
        for x in navLinks:
            returnStr = u'%s%s%s' % (returnStr, separator, x.text)
            separator = "   |   "
        return returnStr
    list_display = ('name', 'description', links)
    list_filter = ('name',)

class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ('text', 'link', 'rank')        
    list_filter = ('text', 'link', 'rank')

admin.site.register(Navigation, NavigationAdmin)
admin.site.register(NavigationLink, NavigationLinkAdmin)