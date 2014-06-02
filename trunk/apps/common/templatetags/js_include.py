from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('apps/common/_js_include.html')
def js_include():
    if settings.JS_USE_SINGLEFILE:
        filepath = settings.JS_COMBINED_FILE
        if settings.JS_MINIFY:
            filepath = filepath.replace(".js","-minified.js")
        files = (filepath,)
        return {
            'files': files 
            }
    else:
        return {
            'files': settings.JS_FILES
            }