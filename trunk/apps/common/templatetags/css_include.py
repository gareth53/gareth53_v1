from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('apps/common/_css_include.html')
def css_include():
    ie_files = []

    for x in settings.CSS_IE_FILES:
        ie_files.append({'expr': x[0], 'path': x[1] })
        
    if settings.CSS_USE_SINGLEFILE:
        single_file = "%s%s" % (settings.CSS_COMBINED_DIR, settings.CSS_COMBINED_FILE)
        combined_ie_files = []
        for iefile in ie_files:
            this_path = iefile.values()[1]
            combined_file_path = "%s%s" % (settings.CSS_COMBINED_DIR, this_path.split("/")[-1])

            if settings.CSS_MINIFY:
                combined_file_path = combined_file_path.replace(".css","-minified.css")

            new_ie_obj = { 
                'expr' : iefile.values()[0],
                'path' : combined_file_path }
            combined_ie_files.append(new_ie_obj)

        if settings.CSS_MINIFY:
            single_file = single_file.replace(".css","-minified.css")
        
        return {
            'files': (single_file,),
            'ie_files': combined_ie_files,
            'combined_files': True }
    else:
        return {
            'files': settings.CSS_FILES,
            'ie_files': ie_files,
            'combined_files': False }