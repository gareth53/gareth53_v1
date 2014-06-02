from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.AddColumn('articles', 'article', 'pod_promos', 'integer NULL', 'articles_promo')
