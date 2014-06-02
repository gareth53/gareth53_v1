from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `podcast_tracklisting` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `track_number` integer NOT NULL,
        `track_id` integer NOT NULL,
        `episode_id` integer NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `podcast_tracklisting` ADD CONSTRAINT `episode_id_refs_id_b58e318` FOREIGN KEY (`episode_id`) REFERENCES `podcast_episode` (`id`);
"""], sql_down=["""
    DROP TABLE `podcast_tracklisting`;
"""])
