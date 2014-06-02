from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.AddColumn('articles', 'article', 'category', 'integer NOT NULL', 'articles_articlecategory')
