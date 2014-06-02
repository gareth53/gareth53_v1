from gareth53.apps.dmigrations.mysql import migrations as m
import datetime
migration = m.InsertRows(
    table_name = 'podcast_track',
    columns = [u'id', u'track_title', u'album_id', u'artist_id', u'track_number', u'track_year'],
    insert_rows = ((1L, u'The Mardi Gras Rescue Mission', 4L, 5L, 5L, u''),
 (2L, u'Bug Powder Dust', 5L, 3L, 6L, u''),
 (3L, u'Ruff Stuff', 3L, 4L, 3L, u''),
 (4L, u'L Dopa', 1L, 1L, 1L, u''),
 (5L, u'Incense And Peppermints', None, 6L, 2L, u''),
 (6L, u'Junk Bond Trader', 2L, 2L, 4L, u''),
 (7L, u'Hazy Lazy Hologram', 9L, 57L, 6L, u'1991'),
 (8L, u'White', None, 31L, 2L, u''),
 (9L, u'Holiday Surprise 1-2-3', 7L, 30L, 3L, u''),
 (10L, u'Race For The Prize', 6L, 56L, 1L, u'1999'),
 (11L, u'Nadine', 8L, 29L, 6L, u''),
 (12L, u'Worlds Away', 10L, 58L, 5L, u'1999'),
 (13L, u'The Altar Boys', 11L, 44L, 1L, u'1993'),
 (14L, u'Hard As A Stone', 12L, 45L, 2L, u'2001'),
 (15L, u'Another Lonely Night', 13L, 46L, 2L, u'1993'),
 (16L, u"Ain't Too Proud To Bow", 14L, 49L, 4L, u'2000'),
 (17L, u'What May Be The Oldest', 15L, 48L, 5L, u'2002'),
 (18L, u'Skall Du Mango Hed? Naa!', 16L, 47L, 6L, u'2001'),
 (19L, u'Six Months In A Leaky Boat', 22L, 52L, 6L, u''),
 (20L, u'TV Party', 21L, 54L, 5L, u''),
 (21L, u'Big Soft Punch', 20L, 53L, 4L, u'1990'),
 (22L, u'Teresa Leaves Lonesome Town', 19L, 55L, 3L, u''),
 (23L, u'Mellowship Slinky In B Major', 17L, 50L, 1L, u''),
 (24L, u'Victoria', 18L, 51L, 2L, u''),
 (25L, u'Show Me The Way', 23L, 39L, 2L, u''),
 (26L, u'Purple Haze', 24L, 42L, 3L, u''),
 (27L, u"Don't Stop Believin'", 25L, 43L, 6L, u'2007'),
 (28L, u'Top Of The World', 26L, 41L, 3L, u'1996'),
 (29L, u"She Don't Use Jelly", 27L, 40L, 5L, u'1997'),
 (30L, u'Bohemian Rhapsody', 28L, 38L, 1L, u'1990'),
 (31L, u'Time Of Her Time', 29L, 32L, 1L, u''),
 (32L, u'Saddle Tramp', 35L, 22L, 1L, u''),
 (33L, u'Catch A Fire', 46L, 20L, 6L, u''),
 (34L, u'July', 45L, 21L, 5L, u'2001'),
 (35L, u'Tiny Spark', 44L, 60L, 4L, u'2002'),
 (36L, u'Streets Of Fire', 43L, 19L, 3L, u'2005'),
 (37L, u'High On Fire', 42L, 14L, 2L, u''),
 (38L, u'Piano Fire', 41L, 13L, 1L, u''),
 (39L, u'What Goes On', 37L, 24L, 3L, u''),
 (40L, u"Searchin'", 36L, 23L, 2L, u''),
 (41L, u'Iron Cock', 38L, 25L, 4L, u''),
 (42L, u'Angelhead', 39L, 27L, 5L, u''),
 (43L, u'Closet Case', 40L, 28L, 6L, u''),
 (44L, u'Hang On', 30L, 33L, 2L, u''),
 (45L, u'Late Century Dream', 31L, 34L, 3L, u''),
 (46L, u'Time Wraps Around Her', 32L, 35L, 4L, u'1994'),
 (47L, u"Thought's A Waste Of Time", 33L, 36L, 5L, u''),
 (48L, u'Stay Forever', 53L, 37L, 6L, u'2000'),
 (49L, u'Obsessively Yours', 47L, 11L, 1L, u'1993'),
 (50L, u'Filthy', 48L, 10L, 2L, u'1991'),
 (51L, u'Drive It All Over Me', 54L, 8L, 3L, u'1988'),
 (52L, u'Can I Kick It? (Phase 5 Mix)', 52L, 9L, 4L, u'1990'),
 (53L, u'Superfly 1990', 51L, 7L, 6L, u'1990'),
 (54L, u'Life Speeds Up', 50L, 12L, 5L, u'1982')),
    delete_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]
)
