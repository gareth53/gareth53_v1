from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Compound([
    m.AddColumn('articles', 'articlecategory', 'pages_title', 'varchar(200) NOT NULL'),
    m.AddColumn('articles', 'articlecategory', 'mainNavigation', 'integer NULL', 'navigation_navigation'),
    m.AddColumn('articles', 'articlecategory', 'footerNavigation', 'integer NULL', 'navigation_navigation'),
])

