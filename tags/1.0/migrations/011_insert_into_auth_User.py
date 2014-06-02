from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.InsertRows(
    table_name = 'auth_user',
    columns = [u'id', u'username', u'first_name', u'last_name', u'email', u'password', u'is_staff', u'is_active', u'is_superuser', u'last_login', u'date_joined'],
    insert_rows = ((1L,
  u'garethsenior',
  u'Gareth',
  u'Senior',
  u'gareth53@hotmail.com',
  u'sha1$19bed$7953b0a10489cdd0711d16776c0bf7b2d8e67667',
  1,
  1,
  1,
  datetime.datetime(2009, 1, 19, 19, 48, 41),
  datetime.datetime(2009, 1, 19, 19, 28, 49)),),
    delete_ids = [1]
)
