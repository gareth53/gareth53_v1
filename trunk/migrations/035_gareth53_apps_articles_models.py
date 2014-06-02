from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `articles_promo` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(200) NOT NULL,
        `headline` varchar(200) NOT NULL,
        `headline_link` varchar(200) NULL,
        `body_html` longtext NOT NULL,
        `article_link_id` integer NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
"""], sql_down=["""
    DROP TABLE `articles_promo`;
"""])
