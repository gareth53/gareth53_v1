import re
import os,sys
import string

from django.conf import settings
from django.core.management.base import NoArgsCommand

from gareth53.apps.common.lib.jsmin import jsmin

class Command(NoArgsCommand):
    """
    Combines Files - for use in combining JS files
    
    to combine the specified files run the command: ./manage.py combine_js

    requirements: the following variables area expected in your SETTINGS

    # first two vars affect what the templatetag does
    JS_USE_SINGLEFILE = True
    JS_MINIFY = True

    # these are the js files for your project
    JS_FILES = (
        '/assets/js/jquery-1.2.1.min.js',
        '/assets/js/swfobject.js',
        '/assets/js/gareth53.js',
        )

    # and this is where the combined file (and it's compressed sibling) will be
    # the compressed file will have "-minified" before the file extension, e.g. "myjsfile-minified.js"
    JS_COMBINED_FILE = '/assets/js/live-gareth53.js'

    """

    def handle_noargs(self, **options):
        if settings.JS_FILES:
            if settings.JS_COMBINED_FILE:
                filepath = "%s%s" % (settings.SITE_ROOT, settings.JS_COMBINED_FILE)
                # test that the directory exists, if not, create it.
                dirs = string.split(filepath, "/")
                target_dir = string.join(dirs[:-1], "/")
                if not os.path.exists(target_dir):
                    try:
                        os.makedirs(target_dir)
                    except:
                        print "Cannot make the destination directory for the combined file"
                # now combine the files
                print "Writing: %s" % filepath
                compiled = open(filepath ,"w")

                for file in settings.JS_FILES:
                    print "Adding: %s" % file
                    js = open("%s%s" % (settings.SITE_ROOT, file)).read() 
                    compiled.write("// START FILE: %s \n" % file)
                    compiled.write(js + "\n")
                compiled.close()
                
                # now, make the minified version
                new_file = filepath.replace(".js","-minified.js")
                original_contents = open(filepath).read()
                minified_contents = jsmin(original_contents)
                if not minified_contents:
                    minified_contents = original_contents
                open(new_file,"w").write(minified_contents)
                
            else:
                print "No JS_COMBINED_FILE variable in settings"
        else:
            print "No JS_FILES variable in settings"
