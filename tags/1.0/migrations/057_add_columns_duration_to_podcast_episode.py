from gareth53.apps.dmigrations.mysql import migrations as m
import datetime

migration = m.AddColumn('podcast', 'episode', 'duration', 'varchar(8) NULL')
