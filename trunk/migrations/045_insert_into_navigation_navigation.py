from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.InsertRows(
    table_name = 'navigation_navigation',
    columns = [u'id', u'name', u'description'],
    insert_rows = ((1L, u'main', u'the main navigation for the core site'),
 (2L, u'footer', u'footer links for the core site'),
 (3L, u'podcast-main', u'Main navigation for the podcast section'),
 (4L, u'podcast-footer', u'footer navigation for the podcast pages')),
    delete_ids = [1, 2, 3, 4]
)
