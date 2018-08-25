import sys
from .pythonageerror import PythonageError

# Superclass whose subclasses are responsible for the generation of a playable game 
# they are also responsible for encapsulating and managing any shared state (e.g. highest score) shared
# across playinggames.

class PGame:

    def __init__(self):
        self._playinggames = []

    @property
    def gamename(self):
        raise PythonageError('gamename has not been implemented on a subclass of PGame')

    def get_playinggame(self, user):
        raise('get_playinggame was not implemented by a subclass of PGame {0}'.format(self.gamename))

