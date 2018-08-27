# ========================= PImageData ==============================================
# Represents image data that the client loads that can later be used to create images 

class PImageData:

    def __init__(self, object_id, new_src, user):
        print('Created imagedata with object id {0}'.format(object_id))
        self._object_id = object_id
        self._user = user

        user.send('nid,{0}'.format(object_id));

        # Additional construction
        self._loaded = False
        self.name = None
        
        if new_src:
            self.src = new_src  # Delegate to src setter

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, new_src):
        self._loaded = False;
        self._src = new_src
        self._user.send('sids,{0},{1}'.format(self._object_id, new_src))

    @property
    def loaded(self):
        return self._loaded

    @property
    def not_loaded(self):
        return not self._loaded

    @property
    def object_id(self):
        return self._object_id

    # Callback which is called by the user when the imagedata is loaded in their browser
    def handle_imagedata_loaded(self):
        self._loaded = True;
        print('{0} image loaded'.format(self._object_id))

    def remove_from_browser(self):
        self._user.send('rem,{0}'.format(self._object_id))
