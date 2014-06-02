from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `articles_articlecategory` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `title` varchar(200) NOT NULL,
        `slug` varchar(50) NOT NULL,
        `description` longtext NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
"""], sql_down=["""
    DROP TABLE `articles_articlecategory`;
"""])
