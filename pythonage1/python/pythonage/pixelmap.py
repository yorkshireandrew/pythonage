from .scenegraphnode import PSceneGraphNode
from .pythonageerror import PythonageError

# ===================== PPixelMap ============
# Represents an array of pixels, that can be rendered at an aboslute position. It does not care about translate or rotate nodes.

class PPixelMap(PSceneGraphNode):

    def __init__(self, object_id, width, height, visible, user):
        super().__init__(user, object_id, visible)
        
        self._width = width;
        self._height = height;

    def from_imagedata(self, image_data):
        self._user.send('npmfid,{0},{1},{2},{3},{4}'.format(self._object_id, image_data.object_id, self._width, self._height, self.command_from_bool(self._visible)))

    def from_string(self, data_width, data_height, string_array):
        first_line_length = len(string_array[0])
        big_string = ''
        for line in string_array:
            if not len(line) == first_line_length:
                raise PythonageError('While creating a pixelmap the string array was unequal')
            big_string += line

        self._user.send('npmfs,{0},{1},{2},{3},{4},{5},{6}'.format(self._object_id, self._width, self._height, data_width, data_height, big_string, self.command_from_bool(self._visible)))

    def make_blue_transparent(self):

        self._user.send('mbt,{0}'.format(self._object_id))

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        if not new_width == self._width:
            self._changed = True
        self._x = new_x

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        if not new_height == self._height:
            self._changed = True
        self._height = new_height       

    def update(self):
        if self._changed:
            self._user.send('upm,{0},{1},{2},{3}'.format(self._object_id, self._width, self._height, self.command_from_bool(self._visible)))

        super().update()
