from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    ALTER TABLE `podcast_track` MODIFY `artist_id` integer NULL; 
    ALTER TABLE `podcast_album` MODIFY `album_artist_id` integer NULL; 
    UPDATE podcast_album SET album_artist_id=NULL WHERE album_artist_id=59;
    DELETE FROM podcast_artist WHERE name='Various';
"""], sql_down=["""
    INSERT INTO podcast_artist (id, name, slug) VALUES (999, 'Various', 'various');
    UPDATE podcast_album SET album_artist_id=999 WHERE album_artist_id=NULL;
    ALTER TABLE `podcast_track` MODIFY `artist_id` integer NOT NULL; 
    ALTER TABLE `podcast_album` MODIFY `album_artist_id` integer NOT NULL; 

    """])