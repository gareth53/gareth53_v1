from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    ALTER TABLE `blog_blogcategory` MODIFY `use_count` integer NULL 
"""], sql_down=["""
    """])