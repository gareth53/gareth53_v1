from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, loader

from gareth53.apps.podcast.models import *


def podcastEpisode(request, season_number, episode_number):
    this_episode = get_object_or_404(Episode.objects, season_number=season_number, episode_number=episode_number, status=1)
    tracks = TrackListing.objects.all().filter(episode=this_episode).order_by('track_number')
    season_episodes = Episode.objects.all().filter(status=1).filter(season_number=season_number).order_by('-episode_number')[:50]
    return render_to_response('podcast/episode.html', {'this_episode': this_episode, 'season_episodes': season_episodes, 'tracks': tracks})
    
def podcastHub(request):
    recent_episodes = Episode.objects.all().filter(status=1).select_related('TrackListing__Track__Artist').order_by('-pub_date')[:9]
    latest = recent_episodes[0]
    return render_to_response('podcast/index.html', {'recent_episodes': recent_episodes, 'latest': latest })

# using my own template for podcast feed rather than using the built-in Django stuff
# I'm wanting an itunes friendly feed

def podcastFeed(request):
    recent_episodes = Episode.objects.all().filter(status=1).order_by('-pub_date')[:5]
    return render_to_response('podcast/podcast-feed.html', {'recent_episodes': recent_episodes })

def podcastArtists(request):
    artists = Artist.objects.all().order_by('name').exclude(name='various')
    return render_to_response('podcast/artists.html', {'artists': artists })