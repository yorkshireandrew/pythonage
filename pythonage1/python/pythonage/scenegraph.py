import sys
from pythonageerror import *

def command_from_bool(input_bool):
    if input_bool:
        return 't'
    else:
        return 'f'

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
        # print('registering imagedata {0} {1} in album'.format(image_data.object_id, type(image_data.object_id)))
        self._imagedata[image_data.object_id] = image_data
  

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


# ===================== SceneGraphNode =========================================================
# Superclass responsible for scenegraph components that can have parents and children
class PSceneGraphNode:
    
    def __init__(self, user, object_id, visible):
        self._user = user
        self._object_id = object_id
        self._visible = visible

        # Additional construction 
        self._children = []
        self.parent = None
        self.name = None
        self._changed = False

    def __iter__(self):
        return iter(self._children)

    def append(self, child):
        if child.parent:
            child.parent.detach(child)
            
        self._user.send('a,{0},{1}'.format(child.object_id, self._object_id))
        self._children.append(child)
        child.parent = self;

    def append_to(self, item_to_append_to):

        if self.parent:
            self.parent.detach(self)

        self._user.send('at,{0},{1}'.format(self._object_id, item_to_append_to.object_id))
        self.parent = item_to_append_to

    def detach(self, child):
        child_id = child.object_id

        self._user.send('dt,{0},{1}'.format(child.object_id, self._object_id))
        
        new_children = [child for child in self._children if not child.object_id == child_id]
        self._children = new_children
        child.parent = None      

    def get_named_child(self, child_name):
        try:
            return next([child for child in self._children if child.name == target_child_name])
        except StopIteration:
            raise KeyError

    def render(self):
        self._user.send('r,{0}'.format(self._object_id))

    def update(self):
        for child in self._children:
            child.update()

    @property
    def object_id(self):
        return self._object_id

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, new_visible):
        if not new_visible == self._visible:
            self._changed = True
        self._visible = visible

    
# ============= PImage ==============================================================================
# Image that can be appended to scene graph objects. Expects to be passed an valid image data object

class PImage(PSceneGraphNode):

    def __init__(self, object_id, image_data_object, width, height, visible, user):
        super().__init__(user, object_id, visible)

        self._width = width
        self._height = height

        # Check the image has loaded
        if image_data_object.not_loaded:
            if image_data_object.name == None:
                raise PythonageError('Creating the image {0} the image data {1} has not yet loaded'.format(object_id, image_data_object.object_id))
            else:
                raise PythonageError('Creating the image {0} the image data {1} has not yet loaded'.format(object_id, image_data_object.name))

        user.send('ni,{0},{1},{2},{3},{4}'.format(object_id, image_data_object.object_id, str(width), str(height), command_from_bool(visible)))

    def update(self):
        if self._changed:
            user.send('ui,{0},{1}'.format(self._object_id, command_from_bool(self._visible)))        

    
# ===================== PTranslate =============================================================
# Scene graph object representing a translation in any direction, for example up,down,left,right

class PTranslate(PSceneGraphNode):

    def __init__(self, object_id, x, y, visible, user):
        super().__init__(user, object_id, visible)
        
        self._x = x
        self._y = y

        user.send('nt,{0},{1},{2},{3}'.format(object_id, x, y, command_from_bool(visible)))

        # Additional construction
        self._changed = True

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        if not new_x == self._x:
            self._changed = True
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        if not new_y == self._y:
            self._changed = True
        self._y = new_y     
        
    def update(self):
        if self._changed:
            self._user.send('ut,{0},{1},{2},{3}'.format(self._object_id, self._x, self._y, command_from_bool(self._visible)))

        super().update()
# ===================== PRotate ============
# Represents a rotation by a given angle

class PRotate(PSceneGraphNode):

    def __init__(self, object_id, angle, visible, user):
        super().__init__(user, object_id, visible)
        
        self._angle = angle

        user.send('nr,{0},{1},{2}'.format(object_id, angle, command_from_bool(visible)))

        # Additional construction
        self._changed = True

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, new_angle):
        if not new_angle == self._angle:
            self._changed = True
        self._angle = new_angle

    def update(self):
        if self._changed:
            self._user.send('ur,{0},{1},{2}'.format(self._object_id, self._angle, command_from_bool(self._visible)))

        super().update()
            
