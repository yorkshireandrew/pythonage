import sys

# Responsible for holding a collection of active timers and ticking them
class PTimerCollection:

    def __init__(self):
        self._timers = {}
        self._next_timer_id = 0

    def append(self, timer):
        timer_id = self._next_timer_id
        self._next_timer_id += 1
        
        timer.timer_id = timer_id
        self._timers[timer_id] = timer
        print('Appended timer:{0}'.format(timer_id))

    def remove(self, timer):
        # Mark thing for deletion on the next tick
        # because a tick might already be running
        self._timers[timer.timer_id].dead = True

    def remove_all_timers(self):
        for key, timer in self._timers.items():
            print('Marked timer {0} for removal'.format(key))
            timer.dead = True
    
    def tick(self): # Periodically called by server
        undertakers_list = []
        timers = self._timers
        
        for timer_id, timer in timers.items():          
            if not timer.dead:
                timer.tick()

            if timer.dead:
                undertakers_list.append(timer_id)

        for timer_id in undertakers_list:
            del timers[timer_id]
