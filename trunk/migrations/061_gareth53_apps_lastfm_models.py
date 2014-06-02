from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `lastfm_user` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `lastfm_username` varchar(255) NOT NULL,
        `profile_url` varchar(200) NOT NULL,
        `profile_pic` varchar(255) NOT NULL,
        `feed_url` varchar(200) NOT NULL,
        `slug` varchar(50) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `lastfm_scrobble` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `user_id` integer NOT NULL,
        `date_time` datetime NULL,
        `date_retrieved` datetime NULL,
        `track_id` integer NULL,
        `lastfm_track_title` varchar(255) NOT NULL,
        `lastfm_artist` varchar(255) NOT NULL,
        `lastfm_track_url` varchar(200)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `lastfm_scrobble` ADD CONSTRAINT `user_id_refs_id_310f68d8` FOREIGN KEY (`user_id`) REFERENCES `lastfm_user` (`id`);
""", """
    -- The following references should be added but depend on non-existent tables:
""", """
    -- ALTER TABLE `lastfm_scrobble` ADD CONSTRAINT `track_id_refs_id_1c3f4127` FOREIGN KEY (`track_id`) REFERENCES `musicartists_track` (`id`);
"""], sql_down=["""
    DROP TABLE `lastfm_scrobble`;
""", """
    DROP TABLE `lastfm_user`;
"""])
