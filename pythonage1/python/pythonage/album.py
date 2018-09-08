# ====================== PAlbum =================================
# Utility class making it easy to determine all images are loaded

class PAlbum:

    def __init__(self):

        # Additional construction
        self._imagedata = {}
        self.name = None

    @property
    def pending(self):
        
        return len([data for data in self._imagedata.values() if not data.loaded])
        print([data for data in self._imagedata.values() if not data.loaded])

    @property
    def loaded(self):
        
        return len(self._imagedata) > 0 and self.pending == 0

    @property
    def not_loaded(self):
        
        return not self.loaded

    def get_imagedata_named(self, name):
        
        try:
            return next([data for data in self._imagedata.values() if data.name == name])
        except StopIteration:
            raise KeyError

    def __len__(self):
        
        return len(self._imagedata)

    def append(self, image_data):
        
        self._imagedata[image_data.object_id] = image_data

    def remove_from_browser(self):
        
        pass # albums do not exist on the browser
