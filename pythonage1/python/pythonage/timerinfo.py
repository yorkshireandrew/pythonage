from pythonageerror import *
import traceback

# Encapsulates information and functionality for each timer a user creates 
class PTimerInfo():

    def __init__(self, interval, callback, once_only = False):
        if interval <= 0:
            raise PythonageError('Attempt to create a timer with interval {0}'.format(interval))
        
        self._countdown = interval
        self._reset_to = interval
        self._callback = callback
        self._once_only = once_only
        self.dead = False

    def handle_tick(self):
        self._countdown -= 1
        if self._countdown == 0 and not self.dead:
            try:
                self._callback()
            except Exception as e:
                tb = traceback.format_exc()
                print('===== TIMER SWALLOWED EXCEPTION ===')
                print(tb)
                print('===================================')

            if self._once_only:
                self.dead = True
            else:
                self._countdown = self._reset_to
