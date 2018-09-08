from .scenegraphnode import PSceneGraphNode

# ===================== PCircle ============
# Represents a circle on the canvas

class PCircle(PSceneGraphNode):

    def __init__(self, object_id, radius, style, visible, user):
        
        super().__init__(user, object_id, visible)

        self._radius = radius
        self._style = style
        user.send('nc,{0},{1},{2},{3}'.format(object_id, radius, style, self.command_from_bool(visible)))

    @property
    def radius(self):
        
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        
        if not new_radius == self._radius:
            self._changed = True
        self._radius = new_radius

    # Style and line properties
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
            self._user.send('uc,{0},{1},{2},{3}'.format(self._object_id, self._radius, self._style, self.command_from_bool(self._visible)))

        super().update()

    @property
    def centre_x(self):
        
        return self.screen_x

    @property
    def centre_y(self):
        
        return self.screen_y
