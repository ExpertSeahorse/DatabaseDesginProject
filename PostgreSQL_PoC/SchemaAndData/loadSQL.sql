
\copy premium(username, firstname, lastname, dob, country, subscriptionplan) FROM './premium.csv'
WITH DELIMITER ',' CSV HEADER;

\copy guest(username, firstname, lastname, dob, country) FROM './guest.csv'
WITH DELIMITER ',' CSV HEADER;

\copy artist(username, firstname, lastname, dob, country, displayname, verified) FROM './artist.csv'
WITH DELIMITER ',' CSV HEADER;

\copy song(songid, title, length, explicit, filelocation, createdby) FROM './song.csv'
WITH DELIMITER ',' CSV HEADER;

\copy userplaylist(playlistid, title, length, numsongs, creator) FROM './userplaylist.csv'
WITH DELIMITER ',' CSV HEADER;

\copy album(playlistid, title, length, numsongs, recordlabel, type, creator) FROM './album.csv'
WITH DELIMITER ',' CSV HEADER;

\copy follows(follower, following) FROM './follows.csv'
WITH DELIMITER ',' CSV HEADER;

\copy likes(username, songid) FROM './likes.csv'
WITH DELIMITER ',' CSV HEADER;

\copy userplaylistsongs(playlistid, songid) FROM './userplaylistsongs.csv'
WITH DELIMITER ',' CSV HEADER;

\copy albumsongs(playlistid, songid) FROM './albumsongs.csv'
WITH DELIMITER ',' CSV HEADER;
