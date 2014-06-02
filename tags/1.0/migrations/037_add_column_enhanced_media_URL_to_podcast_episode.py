from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.AddColumn('podcast', 'episode', 'enhanced_media_URL', 'varchar(200) NULL')
