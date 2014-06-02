"""

A template tag that writes the <script> and <link> includes for static assets
If MINIFY_JS in SETTINGS is TRUE the filename will be filename.min.js
If MINIFY_CSS in SETTINGS is TRUE the filename will be filename.min.css

Sample Usage:
{% static "a/capitalarticles/css/blah.css" %} - outputs correct URL to asset
{% static "c/js/jquery.js" %} - outputs correct URL to asset
{% static_css_print "..." %} outputs <link rel="stylesheet" media="print">

"""
from inspect import getargspec
import random, re

from django import template
from django.conf import settings
from django.utils.functional import curry

from django.conf import settings

SCRIPT = '<script type="text/javascript" src="%s"></script>'
STYLESHEET = '<link rel="stylesheet" href="%s" type="text/css">'
STYLESHEET_MEDIA = '<link rel="stylesheet" href="%s" media="%s" type="text/css">'
URL_CUTTER=re.compile('\/?[^\/]*?$')
MINIFY=re.compile('\.js$')
MINIFY_CSS=re.compile('\.css$')

URL_RE = re.compile(
    r'^https?://' # http:// or https://
    r'(?:(?:[A-Z0-9-]+\.)+[A-Z]{2,6}|' #domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|/\S+)$', re.IGNORECASE)
    
def make_url(url, context=None):
    if context:
        url = template.Template(url).render(context)  
    if url.startswith("/"):
        url = url.replace("/","",1)

    try:
        if settings.MINIFY_JS:
            url=MINIFY.sub(".min.js",url)
    except:
        pass
    try:
        if settings.MINIFY_CSS:
            url=MINIFY_CSS.sub(".min.css",url)
    except:
        pass
    # we might already have an absolute url,
    # for instance for a third party image
    # in which case we'll just use that
    # otherwise it's a local image and wants the 
    # transformation applying
    if not URL_RE.match(url):
        if settings.STATIC_URL.endswith('/') and url.startswith('/'):
            url = settings.STATIC_URL[:-1] + url
        else:
            url = settings.STATIC_URL + url
    
    if settings.DEBUG:
        if not (getattr(settings, 'DEBUG_NO_JS_CACHEBUSTING', False) and \
                url.endswith('.js')):
            if '?' in url:
                url_separator = '&'
            else:
                url_separator = '?'
            url = url + url_separator + 'cachebust=%s' % str(random.random() * 10)
    return url

register = template.Library()

def simple_tag_with_context(func): 
    (params, xx, xxx, defaults) = getargspec(func) 
    
    class SimpleWithContextNode(template.Node): 
        def __init__(self, vars_to_resolve): 
            self.vars_to_resolve = vars_to_resolve 
    
        def render(self, context): 
            resolved_vars = [
                template.resolve_variable(var, context)
                for var in self.vars_to_resolve
            ] 
            rendered = func(context, *resolved_vars) 
            return rendered or '' 
    
    compile_func = curry(
        template.generic_tag_compiler, params[1:], defaults, func.__name__, SimpleWithContextNode
    ) 
    compile_func.__doc__ = func.__doc__ 
    register.tag(func.__name__, compile_func) 
    return func

@simple_tag_with_context
def static(context, url):
    return make_url(url, context)

@simple_tag_with_context
def static_css(context, url):
    if getattr(settings, 'SINGLE_CSS', False) and getattr(settings, 'COMPILED_CSS', False):
        if settings.SINGLE_CSS and url in settings.COMPILED_CSS:
            return ""
    return STYLESHEET % make_url(url, context)

@simple_tag_with_context
def static_css_screen(context, url):
    if getattr(settings, 'SINGLE_CSS', False) and getattr(settings, 'COMPILED_CSS', False):
        if settings.SINGLE_CSS and url in settings.COMPILED_CSS:
            return ""
    return STYLESHEET_MEDIA % (make_url(url, context), 'screen')

@simple_tag_with_context
def static_css_print(context, url):
    return STYLESHEET_MEDIA % (make_url(url, context), 'print')

@simple_tag_with_context
def static_js(context, url):
    if getattr(settings, 'SINGLE_JS', False) and getattr(settings, 'COMPILED_JS', False):
        if settings.SINGLE_JS and url in settings.COMPILED_JS:
            return ""
    return SCRIPT % make_url(url, context)
