from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

from gareth53.apps.lastfm.models import User, Scrobble
from gareth53.apps.musicartists.models import Track, Album, Artist
from gareth53.utils import get_domain_name


def all_scrobbles(request, username='gareth53'):
    user = get_object_or_404(User.objects, lastfm_username=username)
    all_users = User.objects.all()
    all_scrobbles = Scrobble.objects.filter(user__lastfm_username=username).select_related()
    return render_to_response('lastfm/list.html', {
            'scrobbles': all_scrobbles,
            'user': user,
            'site': get_domain_name(),
            'all_users': all_users
            })
