import sys

# Superclass whose subclasses are responsible for the generation of a playable game 
# they are also responsible for encapsulating and managing any shared state (e.g. highest score) shared
# across playinggames.

class PGame:

    def __init__(self):
        self._playinggames = []

    def get_playinggame(self, user):
        print('ERROR: get_playinggame was not implemented by a subclass of PGame')
        return None
