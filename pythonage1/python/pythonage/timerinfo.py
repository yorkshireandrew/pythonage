from pythonageerror import *

# Encapsulates information and functionality for each timer a user creates 
class PTimerInfo():

    def __init__(self, interval, callback, once_only = False):
        if interval <= 0:
            raise PythonageError('Attempt to create a timer with interval {0}'.format(interval))
        
        self._countdown = interval
        self._reset_to = interval
        self._callback
        self._once_only = once_only
        self.dead = False

    def handle_tick(self):
        self.countdown -= 1
        if self.countdown == 0 and not self.dead:
            try:
                self._callback()
            except Exception as e:
                print('PTimerInfo ate exception: {0}'.format(e))

            if once_only:
                self.dead = True
            else:
                self._countdown = self._reset_to
