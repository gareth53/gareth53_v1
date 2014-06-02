from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `blog_blogcategory` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `title` varchar(200) NOT NULL,
        `slug` varchar(50) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `blog_entry` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `title` varchar(200) NOT NULL,
        `slug` varchar(50) NOT NULL,
        `body_html` longtext NOT NULL,
        `pub_date` datetime NOT NULL,
        `enable_comments` bool NOT NULL,
        `category_id` integer NULL,
        `status` integer NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `blog_entry` ADD CONSTRAINT `category_id_refs_id_7f27fd1e` FOREIGN KEY (`category_id`) REFERENCES `blog_blogcategory` (`id`);
"""], sql_down=["""
    DROP TABLE `blog_entry`;
""", """
    DROP TABLE `blog_blogcategory`;
"""])
