from .pythonageerror import PythonageError
import traceback

# Timer that can be created by a playinggame and attached to the server 
class PTimer():

    def __init__(self, interval, callback, gamename):
        
        self._callback = callback
        if interval <= 0:
            raise PythonageError('Attempt to create a timer with interval {0}'.format(interval))
        
        self._countdown = interval
        self._reset_to = interval
        self._gamename = gamename

        # Additional construction
        self.dead = False
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
                print('===== TIMER SWALLOWED EXCEPTION ===')
                print('GAME: {0}'.format(self._gamename))
                print(tb)
                print('===================================')

            self._countdown = self._reset_to
