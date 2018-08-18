import sys

class PythonageUserGame:

    def __init__(self, user):
        self.user = user
        self.albums = {}
        self.image_objects = {}
        self.scene_graph = {}
        self.pending_commands = [];
        self.render_based_flushing = False;
        print('Created PythonageUserGame')
