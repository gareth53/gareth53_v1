from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `podcast_artist` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(50) NOT NULL,
        `official_URL` varchar(200) NULL,
        `wikipedia_URL` varchar(200) NULL,
        `slug` varchar(50) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `podcast_album` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `album_artist_id` integer NOT NULL,
        `title` varchar(100) NOT NULL,
        `amazon_URL` varchar(200) NULL,
        `slug` varchar(50) NOT NULL,
        `release_year` varchar(4) NOT NULL,
        `artwork` varchar(100) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `podcast_album` ADD CONSTRAINT `album_artist_id_refs_id_5defcdba` FOREIGN KEY (`album_artist_id`) REFERENCES `podcast_artist` (`id`);
""", """
    CREATE TABLE `podcast_track` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `track_title` varchar(30) NOT NULL,
        `album_id` integer NULL,
        `artist_id` integer NOT NULL,
        `track_number` integer NOT NULL,
        `track_year` varchar(4) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `podcast_track` ADD CONSTRAINT `album_id_refs_id_45ec5c5` FOREIGN KEY (`album_id`) REFERENCES `podcast_album` (`id`);
""", """
    ALTER TABLE `podcast_track` ADD CONSTRAINT `artist_id_refs_id_70cd4dfa` FOREIGN KEY (`artist_id`) REFERENCES `podcast_artist` (`id`);
""", """
    CREATE TABLE `podcast_episode` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `title` varchar(50) NOT NULL,
        `subtitle` varchar(200) NULL,
        `cover_image` varchar(100) NOT NULL,
        `episode_number` integer NOT NULL,
        `season_number` integer NOT NULL,
        `description` varchar(200) NOT NULL,
        `media_URL` varchar(200) NULL,
        `primary_keywords` varchar(100) NULL,
        `secondary_keywords` longtext NULL,
        `author_name` varchar(50) NOT NULL,
        `author_email` varchar(75) NOT NULL,
        `body_html` longtext NOT NULL,
        `notes_and_errata` longtext NULL,
        `pub_date` datetime NOT NULL,
        `enable_comments` bool NOT NULL,
        `slug` varchar(50) NULL,
        `status` integer NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `podcast_episode_tracks` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `episode_id` integer NOT NULL,
        `track_id` integer NOT NULL,
        UNIQUE (`episode_id`, `track_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `podcast_episode_tracks` ADD CONSTRAINT `episode_id_refs_id_76837f6d` FOREIGN KEY (`episode_id`) REFERENCES `podcast_episode` (`id`);
""", """
    ALTER TABLE `podcast_episode_tracks` ADD CONSTRAINT `track_id_refs_id_485e58a5` FOREIGN KEY (`track_id`) REFERENCES `podcast_track` (`id`);
"""], sql_down=["""
    DROP TABLE `podcast_episode_tracks`;
""", """
    DROP TABLE `podcast_episode`;
""", """
    DROP TABLE `podcast_track`;
""", """
    DROP TABLE `podcast_album`;
""", """
    DROP TABLE `podcast_artist`;
"""])
