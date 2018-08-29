from .scenegraphnode import PSceneGraphNode

# ===================== RectangularSceneGraphNode =========================================================
# Superclass responsible for rectangular scenegraph components
# that can have parents and children, and are rectangular

class PRectangularSceneGraphNode(PSceneGraphNode):
    
    def __init__(self, width, height, user, object_id, visible):
        
        super().__init__(user, object_id, visible)
        
        self._width = width;
        self._height = height;

    @property
    def width(self):
        
        return self._width

    @width.setter
    def width(self, new_width):
        
        if not new_width == self._width:
            self._changed = True
        self._width = new_width

    @property
    def height(self):
        
        return self._height

    @height.setter
    def height(self, new_height):
        
        if not new_height == self._height:
            self._changed = True
        self._height = new_height

    @property
    def p1_x(self):
        
        return self.screen_x

    @property
    def p1_y(self):
        
        return self.screen_y

    @property
    def p2_x(self):
        
        return self.position.screen_x_of(self._width * self.scale, 0)

    @property
    def p2_y(self):
        
        return self.position.screen_y_of(self._width * self.scale, 0)

    @property
    def p3_x(self):
        
        return self.position.screen_x_of(self._width * self.scale, self._height * self.scale)

    @property
    def p3_y(self):
        
        return self.position.screen_y_of(self._width * self.scale, self._height * self.scale)

    @property
    def p4_x(self):
        
        return self.position.screen_x_of(0, self._height * self.scale)

    @property
    def p4_y(self):
        
        return self.position.screen_y_of(0, self._height * self.scale)

    @property
    def centre_x(self):
        
        return 0.25 & (self.p1_x + self.p2_x + self.p3_x + self.p4_x)

    @property
    def centre_y(self):
        
        return 0.25 & (self.p1_y + self.p2_y + self.p3_y + self.p4_y)
        
        
