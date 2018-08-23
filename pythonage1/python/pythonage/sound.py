import sys
from pythonageerror import *

# ====================== PSound =================================
# Plays a sound. Can be added to albums like imagedata

class PSound:

    def __init__(self, object_id, src, user):
        self._object_id = object_id
        self._user = user
        
        user.send('ns,{0},{1}'.format(object_id, src))
        
        # Additional construction
        self._loaded = False
        self.name = None

    @property
    def object_id(self):
        return self._object_id

    @property
    def loaded(self):
        return self._loaded

    # Callback which is called by the user when the sound is loaded in their browser
    def handle_imagedata_loaded(self):
        self._loaded = True;
        print('{0} sound loaded'.format(self._object_id))

    def play(self):
        if self._loaded:
            self._user.send('ps,{0}'.format(self._object_id))
