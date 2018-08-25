from .scenegraphnode import PSceneGraphNode

# ===================== PTranslate =============================================================
# Scene graph object representing a translation in any direction, for example up, down, left, right

class PTranslate(PSceneGraphNode):

    def __init__(self, object_id, x, y, visible, user):
        super().__init__(user, object_id, visible)
        
        self._x = x
        self._y = y

        user.send('nt,{0},{1},{2},{3}'.format(object_id, x, y, self.command_from_bool(visible)))

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
            self._user.send('ut,{0},{1},{2},{3}'.format(self._object_id, self._x, self._y, self.command_from_bool(self._visible)))

        super().update()
