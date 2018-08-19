import sys

class PUserGame:

    def __init__(self, user):
        self._user = user
        self._objects = {}
        self.pending_messages = [];
        self.render_based_flushing = False;
        print('Created UserGame')

        def __len__(self):
        return len(self._objects)

    def __setitem__(self, key, value):
        self._objects[key] = value

    def __getitem__(self, key):
        return self._objects[key]  
		
    def send(self, message):
        if self.render_based_flushing:
            user.send(message)
        else:
            self.pending_messages.append(message)
            print('UserGame ' + self.user.name + ' queued message: ' + message)
