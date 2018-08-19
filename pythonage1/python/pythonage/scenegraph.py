import sys
from pythonage.pythonageerror import *

def command_from_bool(input_bool):
    if(input_bool):
        return 't'
    else:
        return 'f'

# ============ PAlbum ==============
class PAlbum:

    def __init__(self, name, usergame):
        self._name = name
        self._usergame = usergame
        self._imagedata = {}
        self._pending = 0;
        usergame.send('na,{0}'.format(name))
        usergame.albums[name] = self

    @property
    def name(self):
        return self._name

    @property
    def pending(self):
        return self._pending

    @property
    def loaded(self):
        len(self) > 0 and self.pending == 0   

    def __len__(self):
        return len(self._imagedata)
            
    def add_imagedata(self, image_data_name, source):
        new_image_data = PImageData(image_data_name, self, source, self._usergame)
        self._imagedata[image_data_name] = new_image_data

    def __setitem__(self, key, value):
        self._imagedata[key] = value

    def __getitem__(self, key):
        return self._imagedata[key]

    def imagedata_pending_event(self):
        self._pending += 1

    def imagedata_loaded_event(self):
        self._pending -= 1      

# ============= PImageData ==========
class PImageData:

    def __init__(self, name, album, new_src, usergame):
        self._name = name
        self._album = album
        self._usergame = usergame
        self._loaded = False
        usergame.send('nid,{0},{1}'.format(name,album.name));
        
        if new_src:
            self.src = new_src  # Delegate to src setter
        self._album[name] = self

    @property
    def name(self):
        return self._name

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, new_src):
        self._loaded = False;
        self._album.imagedata_pending_event()
        self._src = new_src
        self._usergame.send('sids,{0},{1},{2}'.format(self._name, self._album.name, new_src))

    @property
    def loaded(self):
        return self._loaded

    @property
    def not_loaded(self):
        return not self._loaded

    # Callback which is called by the user when the imagedata is loaded in their browser
    def imagedata_loaded_event(self):
        self._loaded = True;
        self._album.imagedata_loaded_event()
        	
# ============= PImage ==============
class PImage:

    def __init__(self, name, album_name, image_data_name, width, height, visible, usergame):

        # Check we have an image
        try:
            album = usergame.albums[album_name]
        except KeyError:
            raise PythonageError('Creating the image {0} the album {1} did not exist'.format(name, album_name))

        try:  
            image_data = album[image_data_name]
        except KeyError:
            raise PythonageError('Creating the image {0} the image data {1} did not exist in album {2}'.format(name, image_data_name, album_name))

        # Check the image has loaded
        if image_data.not_loaded:
            raise PythonageError('Creating the image {0} the image data {1} has not yet loaded'.format(name, image_data_name))
            
        # Create fields
        self._name = name
        self._image_data_name = image_data_name
        self._width = width
        self._height = height
        self._visible = visible
        self._usergame = usergame

        usergame.send('ni,{0},{1},{2},{3},{4},{5}'.format(name, album_name, image_data_name, str(width), str(height), command_from_bool(visible)))

    @property
    def name(self):
        return self._name

# ===================== PTranslate ============

    def __init__(self, name, x, y, visible, usergame):
        self._name = name
        self._image_data_name = image_data_name
        self._x = x
        self._y = y
        self._visible = visible
        self._usergame = usergame
        
        self._changed = True
        self._children = []
        self._parent = None

    def __iter__(self):
        return iter(self._children)

    def append_image(child_name):
        try:
            child = usergame.image_objects[child_name]
        except KeyError:
            raise PythonageError('Appending image to {0}, the image {1} did not exist'.format(self.name, child_name))

        self._children.append(child)
        self._usergame.send('ai,{0},{1}'.format(self._name, child_name))

    def append_scene_graph_item(child_name):
        try:
            child = usergame.image_objects[child_name]
        except KeyError:
            raise PythonageError('Appending scene graph item to {0}, the item {1} did not exist'.format(self.name, child_name))

        self._children.append(child)
        self._usergame.send('asgi,{0},{1}'.format(self._name, child_name))

    def attach_to(self, scene_graph_item_name):
        try:
            target = usergame.scene_graph[scene_graph_item_name]
        except KeyError:
            raise PythonageError('attach_to was called on {0}, but the target scene graph item {1} did not exist'.format(self.name, scene_graph_item_name))

        if self._parent:
            self._parent,detach_child(self.name)

        self._usergame.send('at,{0},{1}'.format(self._name, target_))

        

    def detach_child(self, child_name):
        new_children = [e in self._children if e.name != child_name]
        self._children = new_children

        

    def __get__(self, child_name):
        try:
            return next(x for x in self._children if x.name == target_child_name)
        except StopIteration:
            raise KeyError

    @property
    def name(self):
        return self._name
        
