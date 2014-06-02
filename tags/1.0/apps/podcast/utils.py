from gareth53.apps.podcast.models import TrackListing

def get_featured_artists(ep):
    TrackListings = TrackListing.objects.all().filter(episode=ep).order_by('track_number')
    if TrackListings is not None:
        feat_tracks = ""
        first = True
        for listing in TrackListings:
            if first:
                feat_tracks = listing.track.artist
            else:
                feat_tracks = "%s, %s" % (feat_tracks, listing.track.artist)
            first = False
        return feat_tracks
    else:
        return ""

def featured_artists_NEW(obj):
    TrackListings = TrackListing.objects.all().filter(episode=obj).order_by('track_number')
    if TrackListings is not None:
        artist_list = []
        for listing in TrackListings:
            artist_list.append(listing.track.artist.name)
        print artist_list
        return artist_list.join(", ")
    else:
        return "No tracks"

def timeify(num):
    if int(num) == 0:
        num = 1
    num = int(int(num) / 1000)
    timeStr = ""
    minutes = int(num / 60)
    seconds = num - (minutes * 60)
    if minutes > 60:
        hours = int(minutes / 60)
        minutes = minutes - (hours * 60)
        timeStr = u'%s:' % padNum(hours)
    return u'%s%s:%s' % (timeStr, padNum(minutes), padNum(seconds)) 

def untimeify(timeStr):
    try:
        timeArr = str(timeStr).split(':')
    except:
        return timeStr
    if len(timeArr) == 3:
        num = (int(timeArr[0]) * 3600) + (int(timeArr[1]) * 60) + int(timeArr[2])
    else:
        num = (int(timeArr[0]) * 60) + int(timeArr[1])
    return int(num * 1000)