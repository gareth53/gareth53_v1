import re
import os,sys
import string
from optparse import make_option

from django.conf import settings
from django.core.management.base import NoArgsCommand

from gareth53.apps.common.lib.cssmin import css_minify
from gareth53.apps.common.utils import relative_to_absolute, absolute_to_relative

class Command(NoArgsCommand):
    """
    For use in combining CSS files
    
    Fixes relative image paths and compresses using compression routines
    similar to Isaac Schlueter's RegExp compression, as used by YUI Compressor.
    
    Relies on the following variables being available in SETTINGS
 
    # first two vars affect what the templatetag does
    CSS_USE_SINGLEFILE = False
    CSS_MINIFY = False
    # these are the css files for your project
    CSS_FILES = (
        '/assets/css/core.css',
        '/assets/css/master.css',
        )
    CSS_IE_FILES = (
    #      the FIRST VALUE is the conditional expression, the 2ND VALUE the filepath
            ('IE', '/assets/css/ie.css'),
        )
    # and this is where the combined file (and it's compressed sibling) will be
    # include a leading AND a trailing slash
    CSS_COMBINED_DIR = '/assets/css/combined/'
    CSS_COMBINED_FILE = 'my-css.css'
    """
    option_list = NoArgsCommand.option_list + (
        make_option('--verbose', action='store_true', dest='verbose'),
    )
    def handle_noargs(self, **options):
        if settings.CSS_FILES:
            # now check that CSS_FILES is a tuple:
            if settings.CSS_COMBINED_DIR and settings.CSS_COMBINED_FILE:
                new_file = "%s%s" % (settings.CSS_COMBINED_DIR, settings.CSS_COMBINED_FILE)
                #pass the destination and the list to a generic function
                compile_file(new_file, settings.CSS_FILES, **options)

                # now, compile the IE files, if necessary
                if settings.CSS_IE_FILES:
                    if options.get('verbose', False):
                        print "COMPILING IE-SPECIFIC FILES"
                    for ie_file in settings.CSS_IE_FILES:
                        # take the name of the base compiled file and add the IE-specific name
                        new_ie_file = settings.CSS_COMBINED_DIR + ie_file[1].split('/')[-1]
                        # pass the destination filename and a list of the base file + this file
                        compile_file(new_ie_file, (new_file, ie_file[1]), **options)
            else:
                print "CSS_COMBINED_FILE and CSS_COMBINED_DIR variables are required in settings"
        else:
            print "No CSS_FILES variable in settings"

def compile_file(filepath, files, **options):
    # test that the directory exists, if not, create it.
    dirs = string.split(filepath, "/")
    target_dir = string.join(dirs[:-1], "/")
    if not os.path.exists(target_dir):
        try:
            os.makedirs(target_dir)
        except:
            print "ERROR: Cannot make the destination directory: %s (%s)" % (target_dir, filepath)
    # now combine the files
    if options.get('verbose', False):
        print "CREATING: %s" % filepath
    compiled = open(filepath ,"w")

    for file in files:
        # get the absolute filesystem path
        path = get_file_path_for_file(file, settings.ASSET_PATHS)
        if options.get('verbose', False):
            print "Adding: %s" % path
        # open the file
        css = open(path).read()

        # fix relative paths to images
        img_ref = re.compile('url\([\'|\"]?(?P<ref>[\S]*)[\'|\"]?\)')
        img_paths = img_ref.findall(css)
        for img_path in img_paths:
            # convert them to absolute paths first
            new_img_path = relative_to_absolute(img_path, path)
            # and now to relative paths
            new_img_path = absolute_to_relative(new_img_path, filepath)
            # add a safety lock, so nothing is find-and-replaced
            # once it's already been fixed
            css = css.replace('url(' + img_path, 'urlX(' + new_img_path)
        css = css.replace('urlX(', 'url(')
        compiled.write("/* START FILE: %s */\n" % file)
        compiled.write(css + "\n")
    compiled.close()
    
    # now, make the minified version
    new_file = filepath.replace(".css","-minified.css")
    original_contents = open(filepath).read()
    minified_contents = css_minify(original_contents)
    if not minified_contents:
        minified_contents = original_contents
    open(new_file,"w").write(minified_contents)