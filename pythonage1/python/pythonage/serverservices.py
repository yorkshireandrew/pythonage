from timerinfo import *

# Encapsulates services the server provides to playablegames
class PServerServices():

    def __init__(self):
        self.timer_info = {}
        self.timer_users_next_id = {}

    def _next_timer_id(self, user_id):
        try:
            timer_users_next_id = self.timer_users_next_id[user_id]
        except: KeyError
            timer_users_next_id = 0

        self.timer_users_next_id[user_id] += 1    
        return timer_users_next_id

    def create_timer(self, user_id, interval, callback):
        timer_id = self._next_timer_id(user_id)
        key = '{0}_{1}'.format(user_id, timer_id)

        self.timer_info[key] = PTimerInfo(interval, callback)     
        return key

    def create_timeout(self, user_id, interval, callback):
        timer_id = self._next_timer_id(user_id)
        key = '{0}_{1}'.format(user_id, timer_id)

        self.timer_info[key] = PTimerInfo(interval, callback, once_only=True)     
        return key

    def remove_timer(self, key):
        try:
            self.timer_info[key].dead = True # Flag it to be dormant and get removed on next server tick
        except KeyError:
            print('some user tried to remove timer {0} which did not exist'.format(key))

    def tick(self): # Periodically called by the server
        undertakers_list = []
        timer_infos = self.timer_info
        
        for timer_info_key in timer_infos.keys():
            timer_info = timer_infos[timer_info_key]            
            timer_info.handle_tick()
            if timer_info.dead:
                undertakers.append(timer_info_key)

        for timer_info_key in undertakers_list:
            del timer_infos[timer_info_key]
            
            
        

    
        
        
        
            
        


        
    
