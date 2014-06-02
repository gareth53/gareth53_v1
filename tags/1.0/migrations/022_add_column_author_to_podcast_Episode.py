from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.AddColumn('podcast', 'episode', 'author', 'integer NULL', 'auth_user')
