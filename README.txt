This is a 'clone' of Spotify designed to rely heavily on a database as the final project in our database class.
Users are sorted into 3 categories: Guest, Premium, and Artist.
	Guests can alter their user setting and search the database for songs, artists, playlists, etc
	Premium users can create playlists and do everything else a guest can
	Artists can create albums and do everything else a guest can

There is a functional mp3 player built into the application that pops open in another terminal window, however
mp3 files for all the songs in the db seed are not included.


Requirements:
	- python 3[.9.9]
	- PostgreSQL db running on the local machine
		- the credentials for accessing this database should be filled in the db.py file
	- All python packages in requirements.txt installed

The menu is run by running "python[3] .\topMenu.py" with the optional 'd' command line arguement to auto sign in as HaroldMusic, a Premium user