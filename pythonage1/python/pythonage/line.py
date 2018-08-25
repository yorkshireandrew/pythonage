from scenegraphnode import SceneGraphNode
from pythonageerror import PythonageError

# ===================== PLine ============
# Represents a line on the canvas

class PLine(PSceneGraphNode):

    def __init__(self, object_id, x1, y1, x2, y2, style, width, visible, user):
        super().__init__(user, object_id, visible)

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self._style = style
        self._width = width

        user.send('nl,{0},{1},{2},{3},{4},{5},{6},{7}'.format(object_id, x1, y1, x2, y2, style, width, self.command_from_bool(visible)))

    # Start properties
    @property
    def x1(self):
        return self._x1

    @x1.setter
    def x1(self, new_x1):
        if not new_x1 == self._x1:
            self._changed = True
        self._x1 = new_x1

    @property
    def y1(self):
        return self._y1

    @y1.setter
    def y1(self, new_y1):
        if not new_y1 == self._y1:
            self._changed = True
        self._y1 = new_y1

    # End properties
    @property
    def x2(self):
        return self._x2

    @x2.setter
    def x2(self, new_x2):
        if not new_x2 == self._x2:
            self._changed = True
        self._x2 = new_x2

    @property
    def y2(self):
        return self._y2

    @y2.setter
    def y2(self, new_y2):
        if not new_y2 == self._y2:
            self._changed = True
        self._y2 = new_y2

    # Style and line properties
    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, new_style):
        if not new_style == self._style:
            self._changed = True
        self._style = new_style

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        if not new_width == self._width:
            self._changed = True
        self._width = new_width

    def update(self):
        if self._changed:
            self._user.send('ul,{0},{1},{2},{3},{4},{5},{6},{7}'.format(self._object_id, self._x1, self._y1, self._x2, self._y2, self._style, self._width, self.command_from_bool(self._visible)))

        super().update()
