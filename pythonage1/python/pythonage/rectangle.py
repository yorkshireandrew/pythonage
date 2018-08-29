from .rectangularscenegraphnode import PRectangularSceneGraphNode

# ===================== PRectangle ============
# Represents a rectangle on the canvas

class PRectangle(PRectangularSceneGraphNode):

    def __init__(self, object_id, width, height, style, visible, user):
        
        super().__init__(width, height, user, object_id, visible)

        self._style = style
        user.send('nrec,{0},{1},{2},{3},{4}'.format(object_id, width, height, style, self.command_from_bool(visible)))

    # Style
    @property
    def style(self):
        
        return self._style

    @style.setter
    def style(self, new_style):
        
        if not new_style == self._style:
            self._changed = True
        self._style = new_style

    def update(self):
        
        if self._changed:
            self._user.send('urec,{0},{1},{2},{3},{4}'.format(self._object_id, self._width, self._height, self._style, self.command_from_bool(self._visible)))

        super().update()
