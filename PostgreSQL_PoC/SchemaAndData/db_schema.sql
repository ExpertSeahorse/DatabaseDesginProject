
-- Changelog --

-- Likes are now limited to premium users (premium --> song)
-- Follows now limited to premium users  (premium --> artist)
-- playlistsongs split into two tables:
	-- albumsongs
	-- userplaylistsongs


-- users
CREATE TABLE users (
	username VARCHAR (15) PRIMARY KEY,
	firstname VARCHAR (20),
	lastname VARCHAR (20),
	dob DATE,
	country VARCHAR (25)
);

--guest (inherits from users)
CREATE TABLE guest (
	username VARCHAR(15) PRIMARY KEY
) INHERITS (users);


--artists --guest (inherits from users)
CREATE TABLE artist (
	--artist_username VARCHAR (15) REFERENCES users (username),
	username VARCHAR(15) PRIMARY KEY,
	displayname VARCHAR (15),
	verified BOOLEAN
) INHERITS (users);


--premium users --guest (inherits from users)
CREATE TABLE premium (
	username VARCHAR(15) PRIMARY KEY,
	subscriptionplan INTEGER -- created as integer now; may use ENUM type in the future as plans become defined
) INHERITS (users);

--follows
-- *** FOLLOWS ARE NOW FROM PREMIUM --> ARTIST ONLY ***
CREATE TABLE follows (
	follower VARCHAR(15) REFERENCES premium (username),
	following VARCHAR(15) REFERENCES artist (username),
	CONSTRAINT pk_primary PRIMARY KEY (follower, following)
);

--song
CREATE TABLE song (
	songid INTEGER PRIMARY KEY,
	title VARCHAR (30),
	length INTEGER,
	explicit BOOLEAN,
	filelocation VARCHAR (50),
	createdby VARCHAR (15) REFERENCES artist (username)
);

--likes
-- ** LIKES ARE NOW LIMITED TO PREMIUM USERS ONLY **
CREATE TABLE likes (
	username VARCHAR(15) REFERENCES premium (username), 
	songid INTEGER REFERENCES song (songid),
	CONSTRAINT pk_likes PRIMARY KEY (username, songid)
);

--playlist
CREATE TABLE playlist (
	playlistid INTEGER PRIMARY KEY,
	title VARCHAR (30),
	length INTEGER,
	numsongs INTEGER
);

--album (inherits from playlist)
CREATE TABLE album (
	playlistid INTEGER PRIMARY KEY,
	recordlabel VARCHAR (20),
	type INTEGER,  -- May want to migrate to an ENUM later as types become defined
	creator VARCHAR (15) REFERENCES artist (username)
) INHERITS (playlist);

--userplaylist
CREATE TABLE userplaylist (
	playlistid INTEGER PRIMARY KEY,
	creator VARCHAR (15) REFERENCES premium (username)
) INHERITS (playlist);

--album songs
CREATE TABLE albumsongs (
	playlistid INTEGER REFERENCES album (playlistid),
	songid INTEGER REFERENCES song (songid),
	CONSTRAINT playlist_pk PRIMARY KEY (playlistid, songid)
);

--playlist songs
CREATE TABLE userplaylistsongs (
	playlistid INTEGER REFERENCES userplaylist (playlistid),
	songid INTEGER REFERENCES song (songid),
	CONSTRAINT userplaylist_pk PRIMARY KEY (playlistid, songid)
);
