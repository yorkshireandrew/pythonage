import sys
from pythonage.pythonageerror import *

def command_from_bool(input_bool):
    if(input_bool):
        return 't'
    else:
        return 'f'

# ====================== PAlbum =================================
# Utility class making it easy to determine all images are loaded

class PAlbum:

    def __init__(self, object_id):

        # Additional construction
        self._imagedata = {}
        self.name = None
        
        # Add ourselves to usergame 
        usergame[object_id] = self

    @property
    def pending(self):
        return len([element in self._imagedata if not element.loaded])

    @property
    def loaded(self):
        len(self) > 0 and self.pending == 0

    def get_imagedata_named(self, name):
        matches = [element in self._imagedata if element.name == name]
        if len(matches) == 0:
            raise KeyError
        return matches[0]

    def __len__(self):
        return len(self._imagedata)

    def __setitem__(self, key, value):
        self._imagedata[key] = value

    def __getitem__(self, key):
        return self._imagedata[key]    

# ========================= PImageData ==============================================
# Represents image data that the client loads that can later be used to create images 

class PImageData:

    def __init__(self, object_id, new_src, usergame):
        self._object_id = object_id
        self._usergame = usergame

        usergame.send('nid,{0}'.format(object_id));

        # Additional construction
        self._loaded = False
        self.name = None
        
        if new_src:
            self.src = new_src  # Delegate to src setter

        # Add ourselves to usergame  
        usergame[object_id] = self

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, new_src):
        self._loaded = False;
        self._album.imagedata_pending_event()
        self._src = new_src
        self._usergame.send('sids,{0},{1}'.format(self._object_id, new_src))

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
    def imagedata_loaded_event(self):
        self._loaded = True;
        	
# ============= PImage ==============================================================================
# Image that can be appended to scene graph objects. Expects to be passed an valid image data object

class PImage:

    def __init__(self, object_id, image_data_object, width, height, visible, usergame):
        self._object_id = object_id
        self._width = width
        self._height = height
        self._visible = visible
        self._usergame = usergame

        # Check the image has loaded
        if image_data_object.not_loaded:
            if image_data_object.name == None:
                raise PythonageError('Creating the image {0} the image data {1} has not yet loaded'.format(object_id, image_data_object.object_id))
            else:
                raise PythonageError('Creating the image {0} the image data {1} has not yet loaded'.format(object_id, image_data_object.name))

        usergame.send('ni,{0},{1},{2},{3},{4},{5}'.format(object_id, image_data_object.object_id, str(width), str(height), command_from_bool(visible)))

        # Additional construction
        self.name = None
        self.parent = None

        # Add ourselves to usergame
        usergame[object_id] = self

    @property
    def object_id(self):
        return self._object_id
    
# ===================== PTranslate =============================================================
# Scene graph object representing a translation in any direction, for example up,down,left,right

class PTranslate

    def __init__(self, object_id, x, y, visible, usergame):
        self._object_id = object_id
        self._x = x
        self._y = y
        self._visible = visible
        self._usergame = usergame

        usergame.send('nt,{0},{1},{2},{3}'.format(object_id, str(x), str(y), command_from_bool(visible)))

        # Additional construction
        self._changed = True
        self._children = []
        self.parent = None
        self.name = None
        
        # Add ourselves to usergame
        usergame[object_id] = self
        
    def __iter__(self):
        return iter(self._children)

    def append(self, child):
        if child.parent:
            child.parent.detach(child)
            
        self._usergame.send('a,{0},{1}'.format(child.object_id, self._object_id))
        self._children.append(child)
        child.parent = self;

    def append_to(self, item_to_append_to):

        if self.parent:
            self.parent.detach(self)

        self._usergame.send('at,{0},{1}'.format(self._object_id, item_to_append_to.object_id))
        self.parent = item_to_append_to

    def detach(self, child):
        child_id = child.object_id

        self._usergame.send('dt,{0},{1}'.format(child.object_id, self._object_id))
        
        new_children = [e in self._children if e.object_id != child_id]
        self._children = new_children
        child.parent = None      

    def get_named_child(self, child_name):
        try:
            return next(x for x in self._children if x.name == target_child_name)
        except StopIteration:
            raise KeyError

    @property
    def object_id(self):
        return self._object_id

# ===================== PRotate ============
# Represents a rotation by a given angle

    def __init__(self, object_id, rotation, visible, usergame):
        self._object_id = object_id
        self._rotation = rotation
        self._visible = visible
        self._usergame = usergame

        usergame.send('nr,{0},{1},{2}'.format(object_id, str(rotation), command_from_bool(visible)))

        # Additional construction
        self._changed = True
        self._children = []
        self.parent = None
        self.name = None
        
        # Add ourselves to usergame
        usergame[object_id] = self
        
    def __iter__(self):
        return iter(self._children)

    def append(self, child):
        if child.parent:
            child.parent.detach(child)
            
        self._usergame.send('a,{0},{1}'.format(child.object_id, self._object_id))
        self._children.append(child)
        child.parent(self)

    def append_to(self, item_to_append_to):

        if self.parent:
            self.parent.detach(self)

        self._usergame.send('at,{0},{1}'.format(self._object_id, item_to_append_to.object_id))
        self.parent = item_to_append_to

    def detach(self, child):
        child_id = child.object_id

        self._usergame.send('dt,{0},{1}'.format(child.object_id, self._object_id))

        new_children = [e in self._children if e.object_id != child_id]
        self._children = new_children
        child.parent = None

    def get_named_child(self, child_name):
        try:
            return next(x for x in self._children if x.name == target_child_name)
        except StopIteration:
            raise KeyError

    @property
    def object_id(self):
        return self._object_id

