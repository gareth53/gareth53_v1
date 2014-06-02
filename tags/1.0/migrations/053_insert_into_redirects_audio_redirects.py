from gareth53.apps.dmigrations.mysql import migrations as m
migration = m.InsertRows(
    table_name = 'django_redirect',
    columns = [u'id', u'site_id', u'old_path', u'new_path'],
    insert_rows = ((12L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode2-kiwi.mp3',
      u'/audio/mp3/peters-and-senior-episode2-kiwi.mp3',
      ),
      (13L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode3-swedes.mp3',
      u'/audio/mp3/peters-and-senior-episode3-swedes.mp3',
      ),
      (14L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode4-covers.m4a',
      u'/audio/mp3/peters-and-senior-episode4-covers.m4a',
      ),
      (15L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode4-covers.mp3',
      u'/audio/mp3/peters-and-senior-episode4-covers.mp3',
      ),
      (16L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode6-grunge.m4a',
      u'/audio/mp3/peters-and-senior-episode6-grunge.m4a',
      ),
      (17L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode6-grunge.mp3',
      u'/audio/mp3/peters-and-senior-episode6-grunge.mp3',
      ),
      (18L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode8-drugs.m4a',
      u'/audio/mp3/peters-and-senior-episode8-drugs.m4a',
      ),
      (19L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode8-drugs.mp3',
      u'/audio/mp3/peters-and-senior-episode8-drugs.mp3',
      ),
      (20L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode9-b-sides.mp3',
      u'/audio/mp3/peters-and-senior-episode9-b-sides.mp3',
      ),
      (21L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode9-b-sides.m4a',
      u'/audio/mp3/peters-and-senior-episode9-b-sides.m4a',
      ),
      (22L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode10-the-missing-links.m4a',
      u'/audio/mp3/peters-and-senior-episode10-the-missing-links.m4a',
      ),
      (23L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode10-the-missing-links.mp3',
      u'/audio/mp3/peters-and-senior-episode10-the-missing-links.mp3',
      ),
      (24L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode5-time.mp3',
      u'/audio/mp3/peters-and-senior-episode5-time.mp3',
      ),
      (25L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode5-time.m4a',
      u'/audio/mp3/peters-and-senior-episode5-time.m4a',
      ),
      (26L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode7-fire.mp3',
      u'/audio/mp3/peters-and-senior-episode7-fire.mp3',
      ),
      (27L,
      1L,
      u'/podcast/mp3/peters-and-senior-episode7-fire.m4a',
      u'/audio/mp3/peters-and-senior-episode7-fire.m4a',
      ),
      (28L,
      1L,
      u'/podcast/mp3/howboutthembears-peters-and-senior-episode1-pilot.mp3',
      u'/audio/mp3/howboutthembears-peters-and-senior-episode1-pilot.mp3',
      ),
  ),
    delete_ids = [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
)