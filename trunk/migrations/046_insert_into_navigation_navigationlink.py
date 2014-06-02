from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.InsertRows(
    table_name = 'navigation_navigationlink',
    columns = [u'id', u'text', u'link', u'rank'],
    insert_rows = ((1L, u'More RSS Feeds', u'/rss-feeds.html', 20L),
 (2L, u'Home', u'/', 2L),
 (3L, u'Podcast', u'/podcast/', 5L),
 (4L, u'Blog', u'/blog/', 5L),
 (5L, u'About Me', u'/about-me.html', 15L),
 (6L, u'About This Site', u'/about-this-site.html', 17L),
 (7L, u'Podcasting Help', u'/podcast/podcasting-help.html', 35L),
 (8L, u'Contact Me', u'/contact-me.html', 18L),
 (9L, u'About Us', u'/podcast/about-nick-and-gareth.html', 16L),
 (10L, u'Home', u'/podcast/', 2L),
 (11L, u'Podcast feed', u'/podcast/podcast-feed.xml', 45L),
 (12L, u'Blog feed', u'/blog/rss/posts.xml', 1L)),
    delete_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
