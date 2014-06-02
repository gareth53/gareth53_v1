
from django import template
from gareth53.apps.navigation.models import Navigation, NavigationLink

register = template.Library()

@register.inclusion_tag('navigation/nav_list.html', takes_context=True)
def navigation_render(context, navSet, position):
    # position should either be "main" or "footer"
    navSet = Navigation.objects.get(name=navSet)
    navLinks = navSet.links.all().order_by('rank')
    return { 'navLinks' : navLinks, 'listId' : navSet, 'position': position, }

def build_nav(parser, token):
    try:
        tag_name, nav_name = token.split_contents()
    except:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents.split()[0]
    return NavObject(nav_name)


