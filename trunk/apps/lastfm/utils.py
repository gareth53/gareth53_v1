import urllib, datetime, re
import sys
from dateutil import parser

#
# install date-util using easy-install:
# easy_install-2.5 -s ~/bin -d ~/lib/python2.5 python-dateutil
#
# http://forum.webfaction.com/viewtopic.php?id=2681
#

from django.utils.html import strip_tags
from django.template.defaultfilters import slugify

#from gareth53.lib.etree import ET
from xml.etree import cElementTree as ET
# NOTE: xml.etree does NOT support attribute selector syntax until version 1.3
from gareth53.apps.lastfm.models import User, Scrobble
from gareth53.apps.musicartists.models import Track, Artist, Album
from gareth53.settings import LASTFM_API_KEY

example_url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=gareth53&api_key=my-api-key"

# The XML we get back from the channel feed looks like this:
"""
<recenttracks user="gareth53">
    <track > 
        <artist mbid="14387b0f-765c-4852-852f-135335790466">Eels</artist>
        <name>what's a fella gotta do</name>
        <streamable>1</streamable>
        <mbid></mbid>
        <album mbid=""></album>
        <url>http://www.last.fm/music/Eels/_/what%27s+a+fella+gotta+do</url>
        <image size="small">http://userserve-ak.last.fm/serve/34s/28943467.jpg</image> 
        <image size="medium">http://userserve-ak.last.fm/serve/64s/28943467.jpg</image>
        <image size="large">http://userserve-ak.last.fm/serve/126/28943467.jpg</image>
        <date uts="1244741427">11 Jun 2009, 17:30</date>
    </track>
"""

# Template for dictionary used to represent each episode
name_to_xpath = {
    'artist_name': 'artist',
    'track_title': 'name',
    'album': 'album',
    'lastfm_url': 'url',
    'images': "image",
    'date': 'date',
}

def date_from_string(str):
    """
    returns a datetime object given a LAST.FM formatted string, like so:
    14 May 2009, 12:51
    """
    months = [
        'jan', 'feb', 'mar', 'apr',
        'may', 'jul', 'jun', 'aug',
        'sep', 'oct', 'nov', 'dec']
    # remove the comma
    str = str.replace(',','')
    #remove the colon
    str = str.replace(':',' ')
    # make an array
    date_arr = str.split(" ")
    day = int(twofig(date_arr[0]))
    try:
        month = twofig(months.index(date_arr[1][:3].lower()))
    except:
        pass 
    year = int(date_arr[2])
    hour = int(twofig(date_arr[3]))
    mins = int(twofig(date_arr[4]))
    return datetime.datetime(year, int(month), day, hour, mins)

def twofig(num):
    if int(num) < 10:
        num = "0%s" % str(int(num))
    return num

def parse_items(url):
    """
    Returns a list of scrobbles for a specified account
    """
    print "parsing %s" % url
    try:
        et = ET.parse(urllib.urlopen(url))
    except SyntaxError:
        print "Could not process invalid XML: %s" % url
    array = []
    for el in et.findall('recenttracks/track'):
        item = {}
        for name, xpath in name_to_xpath.items():
            try:
                value = el.find(xpath).text
                print value
                item[name] = value
            except:
                print "EXCEPTION for %s" % xpath
                print "%s: %s" % sys.exc_info()[:2]
                item[name] = ""
        array.append(item)
    return array


def import_scrobbles(User):
    """
    Takes parsed XML feed as a dictionary and creates 
    scrobble, track, artist and album objects
    """
    base_URL = "http://ws.audioscrobbler.com/2.0/?"
    URL = "%smethod=user.getrecenttracks&user=%s&limit=100&api_key=%s" % (base_URL, User.lastfm_username, LASTFM_API_KEY)
    for tune in parse_items(URL):
        print "Creating: %s - %s (%s)" % (tune['artist_name'], tune['track_title'], date_from_string(tune['date']).strftime("%Y-%m-%d %H:%M:%S"))
        
        # todo: use get_or_create methods rather than this filter and count()
        #
        # todo: truncate values to squish them into the db (song title upto 82 chars)
        #
        # todo: create album objects
        #
        # TODO: import artwork - ATTACH TO TRACKS, NOT ALBUMS
        # 
        #
        # TODO: test, test, test - with other users.

        # Artist
        artist = Artist.objects.get_or_create(name=tune['artist_name'], slug=slugify(tune['artist_name'][:50]))[0]

        # Album
        if tune['album']:
            # we don't bind the artist to the album, because we can't be sure it's not a compilation
            # without another API call.
            album = Album.objects.get_or_create(
                        title=tune['album'],
                        slug=slugify(tune['album'][:50]))[0] 
        # Track
        track = Track.objects.get_or_create(track_title=tune['track_title'],artist=artist)
        if track[1] and tune['album']:
            track[0].album = album
#        if track[0].image_large is None and tune['images'][0]:
#            track[0].image_large = tune['images'][0]
#
#        if track[0].image_medium is None and tune['images'][0]:
#            track[0].cover_art_medium = tune['images'][1]
#
        if track[0].image_small is None and tune['images']:
            track[0].image_large = tune['images']
            track[0].save()
                
        # Scrobble
        # check for a duplicate entry first
        existing_scrobble = Scrobble.objects.filter(
                user = User,
                date_time = date_from_string(tune['date']).strftime("%Y-%m-%d %H:%M:%S"),
                lastfm_track_title = tune['track_title'],
                lastfm_artist = tune['artist_name'],
            )
        # if no objects returned, create it....
        if not existing_scrobble:
            Scrobble.objects.create(
                user = User,
                date_retrieved = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                date_time = date_from_string(tune['date']).strftime("%Y-%m-%d %H:%M:%S"),
                lastfm_track_title = tune['track_title'][0:255],
                lastfm_artist = tune['artist_name'][0:255],
                lastfm_track_url = tune['lastfm_url'],
                track = track[0],
            )
        else:
            print "SCROBBLE NOT CREATED: already exists - %s, %s (%s)" % (tune['artist_name'], tune['track_title'], date_from_string(tune['date']).strftime("%Y-%m-%d %H:%M:%S"))
            
