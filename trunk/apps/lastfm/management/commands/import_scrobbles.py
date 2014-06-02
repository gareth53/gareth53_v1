from optparse import make_option

from django.core.management.base import NoArgsCommand

from gareth53.apps.lastfm.utils import import_scrobbles
from gareth53.apps.lastfm.models import *


class Command(NoArgsCommand):
    """
    Imports scrobbles from last.fm's API
    """

    help = """
    This imports scrobbles from last.fm's API. Run from cron.
    """.strip()
    option_list = NoArgsCommand.option_list + (
        make_option('--verbose', action='store_true', dest='verbose'),
    )

    def handle_noargs(self, **options):        
        if options.get('verbose', False):
            print "IMPORTING SCROBBLES"
        for user in User.objects.all():
            if user.lastfm_username:
                if options.get('verbose', False):
                    print "Importing scrobbles for Last.fm account named '%s'" % user.lastfm_username
                import_scrobbles(user)
