from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `musicartists_artist` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(255) NOT NULL,
        `official_URL` varchar(255),
        `wikipedia_URL` varchar(255),
        `slug` varchar(50) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `musicartists_album` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `album_artist_id` integer,
        `title` varchar(255) NOT NULL,
        `amazon_URL` varchar(255),
        `slug` varchar(50) NOT NULL,
        `release_year` varchar(4) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `musicartists_album` ADD CONSTRAINT `album_artist_id_refs_id_3dd1f5e6` FOREIGN KEY (`album_artist_id`) REFERENCES `musicartists_artist` (`id`);
""", """
    CREATE TABLE `musicartists_track` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `track_title` varchar(255) NOT NULL,
        `album_id` integer,
        `artist_id` integer,
        `track_year` varchar(4) NOT NULL,
        `image_large` varchar(255),
        `image_medium` varchar(255),
        `image_small` varchar(255)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `musicartists_track` ADD CONSTRAINT `album_id_refs_id_6ac3c11b` FOREIGN KEY (`album_id`) REFERENCES `musicartists_album` (`id`);
""", """
    ALTER TABLE `musicartists_track` ADD CONSTRAINT `artist_id_refs_id_1d8c6786` FOREIGN KEY (`artist_id`) REFERENCES `musicartists_artist` (`id`);
"""], sql_down=["""
    DROP TABLE `musicartists_track`;
""", """
    DROP TABLE `musicartists_album`;
""", """
    DROP TABLE `musicartists_artist`;
"""])
