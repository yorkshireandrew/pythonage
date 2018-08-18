from pythonage.scenegraph import *
from pythonage.usergame import *
from pythonage.pythonageerror import *
from pythonage.user import *

user = PUser('bob', None, None)
user_game = PUserGame(user)

album = PAlbum('thealbum', user_game)

album.add_imagedata('theimagedata','somesource')

album['theimagedata'].imagedata_loaded_event()

p = PImage('pi', 'thealbum', 'theimagedata', 42, 42, True, user_game)



