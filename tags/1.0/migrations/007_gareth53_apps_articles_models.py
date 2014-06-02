from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `articles_article` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `title` varchar(200) NOT NULL,
        `slug` varchar(50) NOT NULL,
        `body_html` longtext NOT NULL,
        `pub_date` datetime NOT NULL,
        `status` integer NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
"""], sql_down=["""
    DROP TABLE `articles_article`;
"""])
