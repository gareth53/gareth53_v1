from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    DROP TABLE `podcast_episode_tracks`;
"""], sql_down=[     """
        CREATE TABLE `podcast_episode_tracks` (
            `id` integer AUTO_INCREMENT NULL PRIMARY KEY,
            `episode_id` integer NULL,
            `track_id` integer NULL,
            UNIQUE (`episode_id`, `track_id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        ;
    """])
