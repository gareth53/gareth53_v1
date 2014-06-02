DOCUMENTATION FOR GARETH53.CO.UK CLIENT SIDE BUILD
LAST CHANGE: 20.01.09

CONTENTS
========

1. Markup Structure
1.1. Page IDs
1.2. Page Classes
1.3. Site Classes
2. Date Conventions
3. Other People's Code




MARKUP STRUCTURE
================

The following ELEMENTS indentified with an ID are present on EVERY page:

- p#skip_container
containing links that skip to ID elements within the page, generally only a 'skip to navigation' link, but could be more.

- div#page
contains all 'page' content, thus allowing the centering of the site

- div#content
the container for the column divs

- div#col1
the site is built around three columns, the width of the columns is dependent upon the class of the body

- div#col2
the second column, generally always the same width, but could be altered by the class of the body.

- div#col3
third column may be hidden by the body class, if that class is set to less than three columns

- div.col-child
when a column consists of multiple modules, each is wrapped in a div.col-child

- #sitetitle
either a h1 (for the homepage) or a paragraph.

- ul#nav-main
the first, or main, set of navigation links, may have a nested ul element on one or more children for sub-navigation

- ul#nav-footer
the secondary navigation that appears at the foot of the page


CLASS PATTERNS

The following class patterns appear throughout the site and affect the layout.

- body.col2
adjusts the width of col1 and the margin-right of col2

- body.col3
adjusts the width of col1 and the margin-right of col2


CLASS Patterns
==============
The following class patterns occur repeatedly throughout the site without being specific to the site section, layout or page.

- li.first-child

- li.last-child


- li.alt
alt meaning 'alternate' and allows for 'striping' every other li

- tr.alt
alt meaning 'alternate' and allows for 'striping' every other row in a table


- a.more
alows for custom icons

- a.rss
allows us to add an RSS icon to the link

p.listen a
this is used by the jquery, replacing the paragraph with a flash player that attempts to play the mp3 file that is epxected to be the href value of the anchor.


PODCAST STYLING
===============
Styling for podcast pages are defined using podcast.css
The styles are namespace using BODY#PODCAST 

Here the navigation UL is floated left rather than appearing above the DIV#CONTENT

The DIV#CONTENT is narrower and has no float clearing.




DATE CONVENTIONS
================

long date convention (for use on a 'node' page e.g. a blog post or an article, or a podcast episode)
9:12am, Mon 23 Jan 2009

django filter = "g:ia, D j M Y"


short date convention (for use on a 'collection' page where multiple dates will be shown in a list)
9:12am, 23 Jan

django filter = "g:ia, j M"

short date convention if the year variable is not the current year
23 Jan 2009

django filter = "j M Y"





jQuery 1.2.1 from docs.jquery.com

YUI reset CSS and font-reset.css


Flash Audio Player from 1pixelout.net

http://www.1pixelout.net/code/audio-player-wordpress-plugin/

http://www.macloo.com/examples/audio_player/index.html


Hosting by: WebFaction



