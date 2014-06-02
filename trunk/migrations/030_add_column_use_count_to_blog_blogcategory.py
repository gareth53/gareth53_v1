from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.AddColumn('blog', 'blogcategory', 'use_count', 'integer NOT NULL')
