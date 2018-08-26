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
        self._layer = 0
        self._scale = 1.0

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
        self._user.rendering = True
        self._user.send('r,{0}'.format(self._object_id))

    def render_layers(self):
        self._user.rendering = True
        self._user.send('rl,{0}'.format(self._object_id))

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

    def command_from_bool(self, input_bool):
        if input_bool:
            return 't'
        else:
            return 'f'

    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, new_value):
        self._user.send('sl,{0},{1}'.format(self._object_id, new_value))

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, new_value):
        self._user.send('usc,{0},{1}'.format(self._object_id, new_value))
        
