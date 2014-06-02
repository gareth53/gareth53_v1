from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    ALTER TABLE `podcast_track` DROP `track_number`;
"""], sql_down=["""
        ALTER TABLE podcast_track ADD track_number INTEGER NULL AFTER artist_id;
    """])
