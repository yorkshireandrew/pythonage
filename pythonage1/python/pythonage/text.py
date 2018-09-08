from .scenegraphnode import PSceneGraphNode
from .pythonageerror import PythonageError

# ===================== PText ============
# Represents text on the canvas

class PText(PSceneGraphNode):

    def __init__(self, object_id, x, y, font, style, text, visible, user):
        super().__init__(user, object_id, visible)

        self._x = x
        self._y = y
        self._font = font #TODO validation
        self._style = style
        self._text = text;
        to_send = text.replace(',','{{comma}}')
        user.send('ntxt,{0},{1},{2},{3},{4},{5},{6}'.format(object_id, x, y, font, self._style, to_send, self.command_from_bool(visible)))

    # Readonly properties
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def font(self):
        return self._font

    @property
    def style(self):
        return self._style

    # Writable properties

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        if not new_text == self._text:
            self._changed = True
        self._text = new_text

    def update(self):
        if self._changed:
            to_send = self._text.replace(',','{{comma}}')
            self._user.send('utxt,{0},{1},{2}'.format(self._object_id, to_send, self.command_from_bool(self._visible)))

        super().update()
