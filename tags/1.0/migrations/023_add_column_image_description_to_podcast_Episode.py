from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.AddColumn('podcast', 'episode', 'image_description', 'varchar(50) NULL')
