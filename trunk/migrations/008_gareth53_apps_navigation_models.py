from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `navigation_navigationlink` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `text` varchar(200) NOT NULL,
        `link` varchar(75) NOT NULL,
        `rank` integer NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `navigation_navigation` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(100) NOT NULL,
        `description` longtext NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `navigation_navigation_links` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `navigation_id` integer NOT NULL,
        `navigationlink_id` integer NOT NULL,
        UNIQUE (`navigation_id`, `navigationlink_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `navigation_navigation_links` ADD CONSTRAINT `navigation_id_refs_id_24c3ba3d` FOREIGN KEY (`navigation_id`) REFERENCES `navigation_navigation` (`id`);
""", """
    ALTER TABLE `navigation_navigation_links` ADD CONSTRAINT `navigationlink_id_refs_id_28278353` FOREIGN KEY (`navigationlink_id`) REFERENCES `navigation_navigationlink` (`id`);
"""], sql_down=["""
    DROP TABLE `navigation_navigation_links`;
""", """
    DROP TABLE `navigation_navigation`;
""", """
    DROP TABLE `navigation_navigationlink`;
"""])
