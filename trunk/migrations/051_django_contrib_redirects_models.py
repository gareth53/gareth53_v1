from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `django_redirect` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `site_id` integer NOT NULL,
        `old_path` varchar(200) NOT NULL,
        `new_path` varchar(200) NOT NULL,
        UNIQUE (`site_id`, `old_path`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `django_redirect` ADD CONSTRAINT `site_id_refs_id_4aa27aa6` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`);
"""], sql_down=["""
    DROP TABLE `django_redirect`;
"""])
