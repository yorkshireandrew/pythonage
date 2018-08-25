from .pythonageerror import PythonageError
import traceback

# Timeout that fires only once that can be created by a playinggame and attached to the server
# Quacks like a PTimer
class PTimeout():

    def __init__(self, interval, callback, gamename):
        self._callback = callback
        self._gamename = gamename
        
        if interval <= 0:
            raise PythonageError('Attempt to create a timeout with interval {0}'.format(interval))      
        self._countdown = interval

        # Additional construction
        self.dead = False # Flag that removes the timeout from PTimerCollection
        self.timer_id = None # Controlled and used by PTimerCollection

    @property
    def gamename(self):
        return self._gamename

    def tick(self): # Called each server tick
        self._countdown -= 1
        if self._countdown == 0:
            try:
                self._callback()
            except Exception as e:
                tb = traceback.format_exc()
                print('===== TIMEOUT SWALLOWED EXCEPTION ===')
                print('GAME: {0}'.format(self._gamename))
                print(tb)
                print('=====================================')

            self.dead = True
            self._countdown = 1000
