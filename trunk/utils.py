from django.conf import settings
from django.contrib.sites.models import Site

def get_domain_name():
    domain = Site.objects.get(id=settings.SITE_ID)
    return domain.name