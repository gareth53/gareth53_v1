from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, loader
from gareth53.apps.articles.models import Article
from gareth53.utils import get_domain_name

def ArticlePageInCategory(request, category, slug):
    this_post = get_object_or_404(Article.objects, slug=slug, status=1, category__slug=category)
    return render_to_response('articles/article.html', {'this_article': this_post, 'site': get_domain_name() })

def ArticlePage(request, slug):
    this_post = get_object_or_404(Article.objects, slug=slug, status=1, category__title="Master")
    return render_to_response('articles/article.html', {'this_article': this_post, 'site': get_domain_name() })
