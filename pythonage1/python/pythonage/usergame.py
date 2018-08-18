import sys

class PUserGame:

    def __init__(self, user):
        self.user = user
        self.albums = {}
        self.image_objects = {}
        self.scene_graph = {}
        self.pending_messages = [];
        self.render_based_flushing = False;
        print('Created UserGame')
		
    def send(self, message):
        if self.render_based_flushing:
            user.send(message)
        else:
            self.pending_messages.append(message)
            print('UserGame ' + self.user.name + ' queued message: ' + message)
