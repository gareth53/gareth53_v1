from gareth53.apps.dmigrations.mysql import migrations as m
migration = m.InsertRows(
    table_name = 'django_redirect',
    columns = [u'id', u'site_id', u'old_path', u'new_path'],
    insert_rows = ((1L,
      1L,
      u'/podcast/episode001.html',
      u'/podcast/episode1-1.html',
      ),
      (2L,
      1L,
      u'/podcast/episode002.html',
      u'/podcast/episode1-2.html',
      ),
      (3L,
      1L,
      u'/podcast/episode003.html',
      u'/podcast/episode1-3.html',
      ),
      (4L,
      1L,
      u'/podcast/episode004.html',
      u'/podcast/episode1-4.html',
      ),
      (5L,
      1L,
      u'/podcast/episode005.html',
      u'/podcast/episode1-5.html',
      ),
      (6L,
      1L,
      u'/podcast/episode006.html',
      u'/podcast/episode1-6.html',
      ),
      (7L,
      1L,
      u'/podcast/episode007.html',
      u'/podcast/episode1-7.html',
      ),
      (8L,
      1L,
      u'/podcast/episode008.html',
      u'/podcast/episode1-8.html',
      ),
      (9L,
      1L,
      u'/podcast/episode009.html',
      u'/podcast/episode1-9.html',
      ),
      (10L,
      1L,
      u'/podcast/episode010.html',
      u'/podcast/episode1-10.html',
      ),
      (11L,
      1L,
      u'/podcast/episode011.html',
      u'/podcast/episode1-11.html',
      ),
  ),
    delete_ids = [1,2,3,4,5,6,7,8,9,10,11]
)