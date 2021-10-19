"""
We will eventually replace these with DB calls. Until then these help with designing the interface
"""
import datetime
class User:
    def __init__(self, usern, passw, firstName, lastName, email, dob, country, following, followed_by, userType, playlistType, artistName, verified, favSongs, favArtists) -> None:
        self.usern = usern
        self.passw = passw
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.dob = dob
        self.country = country
        self.following = following
        self.followed_by = followed_by

        # not Guest
        self.userType = userType
        self.playlistType = playlistType

        # Artist specific
        self.artistName = artistName
        self.verified = verified

        # Premium specific
        self.favSongs = favSongs
        self.favArtists = favArtists

userGuest = User(
    "guest",
    "pass",
    "Guest",
    "User",
    "guest@test.com",
    datetime.datetime.now(),
    "Argentina",
    ["James", "Adam"],
    ["Adam", "Jules"],
    "guest",
    "", "", False, [], []
)

userPrem = User(
    "premium",
    "pass",
    "Premium",
    "User",
    "premium@test.com",
    datetime.datetime.now(),
    "Egypt",
    ["Mike"],
    ["Adam", "George"],
    "premium",
    "playlist", "", False, ["Uptown Funk", "I Gotta Feeling"], ["Bruno Mars", "The Black Eyed Peas"]
)

userArtist = User(
    "artist",
    "pass",
    "Artist",
    "User",
    "artist@test.com",
    datetime.datetime.now(),
    "United Kingdom",
    [],
    ["Otto", "Allison Downs", "Lily-Anne"],
    "artist",
    "album", "myArtistName", True, [], []
)