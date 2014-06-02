from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.InsertRows(
    table_name = 'blog_blogcategory',
    columns = [u'id', u'title', u'slug', u'use_count'],
    insert_rows = ((1L, u'development', u'development', 30L),
 (2L, u'podcast', u'podcast', 8L),
 (3L, u'radio', u'radio', 1L),
 (4L, u'music', u'music', 2L),
 (5L, u'personal', u'personal', 3L),
 (6L, u'film', u'film', 2L),
 (7L, u'rant', u'rant', 1L),
 (8L, u'football', u'football', 1L),
 (9L, u'tellybox', u'tellybox', 1L),
 (10L, u'design', u'design', 1L)),
    delete_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
)
