from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.AddColumn('podcast', 'episode', 'download_duration', 'varchar(24) NULL')

