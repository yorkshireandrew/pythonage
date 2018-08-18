import sys
from pythonageerror import *

class PythonageImage:

    def __init__(self, name, album_name, image_data_name, width, height, usergame):
        # Check we have an image
        try:
            album = usergame.albums[album_name]
        except KeyError:
            raise PythonageException('Creating the image ' + name + ' the album ' + album_name + ' did not exist'

        try:  
            image_data = album
        except KeyError:
            raise PythonageException('Creating the image' + name + ' the image data ' + image_data_name + ' did not exist in album ' + album_name)

        # Create fields
        self.name = name                 
        self.album_name = album_name
        self.image_data_name = image_data_name
        self.width = width
        self.height = height
        print('Created PythonageImage')

        
