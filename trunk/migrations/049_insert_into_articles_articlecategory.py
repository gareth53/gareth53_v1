from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.InsertRows(
    table_name = 'articles_articlecategory',
    columns = [u'id', u'title', u'slug', u'description', u'pages_title', u'mainNavigation_id', u'footerNavigation_id'],
    insert_rows = ((1L, u'Podcast', u'podcast', u'', u'The Nick & Gareth Podcast', 3L, 4L),
 (2L, u'articles', u'articles', u'', u'gareth53', 1L, 2L),
 (3L, u'Master', u'test', u'', u'Gareth<span id="titleNo">53</span>', 1L, 2L)),
    delete_ids = [1, 2, 3]
)
