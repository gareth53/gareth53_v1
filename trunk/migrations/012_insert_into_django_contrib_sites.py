from gareth53.apps.dmigrations.mysql import migrations as m
migration = m.InsertRows(
    table_name = 'django_site',
    columns = [u'id', u'domain', u'name'],
    insert_rows = ((1L,
  u'www.gareth53.co.uk',
  u'Gareth53.co.uk',),),
    delete_ids = [1]
)
