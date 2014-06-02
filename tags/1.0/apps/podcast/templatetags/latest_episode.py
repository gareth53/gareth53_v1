from django import template
from gareth53.apps.podcast.models import Episode

register = template.Library()

@register.inclusion_tag('podcast/_latest_episode.html', takes_context=True)
def latest_episode(context):
    latest = Episode.objects.all().filter(status=1).order_by('-pub_date')[0]
    return { 'latest' : latest, }