from scenegraphnode import SceneGraphNode
from pythonageerror import PythonageError

# ===================== PPixelMap ============
# Represents an array of pixels, that can be rendered at an aboslute position. It does not care about translate or rotate nodes.

class PPixelMap(PSceneGraphNode):

    def __init__(self, object_id, x, y, visible, user):
        super().__init__(user, object_id, visible)
        
        self._x = x;
        self._y = y;

    def from_imagedata(self, image_data):
        self._user.send('npmfid,{0},{1},{2},{3},{4}'.format(self._object_id, image_data.object_id, self._x, self._y, self.command_from_bool(self._visible)))

    def from_string(self, width, height, scaling, string_array):
        first_line_length = len(string_array[0])
        big_string = ''
        for line in string_array:
            if not len(line) == first_line_length:
                raise PythonageError('While creating a pixelmap the string array was unequal')
            big_string += line

        self._user.send('npmfs,{0},{1},{2},{3},{4},{5},{6},{7}'.format(self._object_id, self._x, self._y, width, height, scaling, big_string, self.command_from_bool(self._visible)))

    def make_blue_transparent(self):

        self._user.send('mbt,{0}'.format(self._object_id))

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
            self._user.send('upm,{0},{1},{2}'.format(self._object_id, self._angle, self.command_from_bool(self._visible)))

        super().update()
