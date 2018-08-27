from .scenegraphnode import PSceneGraphNode

# ===================== PRotate ============
# Represents a rotation by a given angle

class PRotate(PSceneGraphNode):

    def __init__(self, object_id, angle, visible, user):
        super().__init__(user, object_id, visible)
        
        self._angle = angle

        user.send('nr,{0},{1},{2}'.format(object_id, angle, self.command_from_bool(visible)))

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
            self._user.send('ur,{0},{1},{2}'.format(self._object_id, self._angle, self.command_from_bool(self._visible)))

        super().update()

    def calculate_position(self, matrix):
        self.position = matrix
        rotated = matrix.rotated(self._angle)
        for child in self._children:
            child.calculate_position(rotated)
