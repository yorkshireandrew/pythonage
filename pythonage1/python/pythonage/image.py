from scenegraphnode import SceneGraphNode
from pythonageerror import PythonageError

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

        user.send('ni,{0},{1},{2},{3},{4}'.format(object_id, image_data_object.object_id, str(width), str(height), self.command_from_bool(visible)))

    def update(self):
        if self._changed:
            user.send('ui,{0},{1}'.format(self._object_id, self.command_from_bool(self._visible)))
