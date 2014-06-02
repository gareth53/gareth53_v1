import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader

from gareth53.apps.blog.models import Entry
from gareth53.apps.podcast.models import Episode
from gareth53.utils import get_domain_name
from gareth53.paginator import DiggPaginator

def homepage(request):
    latest_posts = Entry.objects.all().filter(status=1).order_by('-pub_date')[:4]
    latest_pods = Episode.objects.all().filter(status=1).order_by('-pub_date')[:5]
    posts_object = DiggPaginator(latest_posts, 4, body=5, padding=2)
    return render_to_response('home.html', {'posts': posts_object, 'pods': latest_pods, 'page_id': 'homepage', 'site':get_domain_name() })