from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `flickr_user` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(50) NOT NULL,
        `profile_url` varchar(200),
        `profile_pic` varchar(255),
        `feed_url` varchar(200) NOT NULL,
        `slug` varchar(50) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `flickr_image` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `date_retrieved` datetime NOT NULL,
        `photo_id` varchar(100) NOT NULL,
        `photo_secret` varchar(100) NOT NULL,
        `server` varchar(100) NOT NULL,
        `server_farm` varchar(100) NOT NULL,
        `title` varchar(255) NOT NULL,
        `description` varchar(255) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
"""], sql_down=["""
    DROP TABLE `flickr_image`;
""", """
    DROP TABLE `flickr_user`;
"""])
