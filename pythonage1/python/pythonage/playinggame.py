import sys

from .pythonageerror import PythonageError
from .album import PAlbum
from .imagedata import PImageData
from .image import PImage
from .translate import PTranslate
from .rotate import PRotate
from .timer import PTimer
from .timeout import PTimeout
from .sound import PSound
from .pixelmap import PPixelMap
from .line import PLine
from .text import PText
from .circle import PCircle
from .javascriptstyle import JavascriptStyle

# Superclass encapsulating a particular users version of a game.
# Subclass this to create a game which responds to a user connecting and playing.
# It provides methods to the subclass allowing it to create and control pythonage objects.
class PPlayingGame:

    def __init__(self, user, game):
        
        self._user = user
        self._game = game

        if not game.gamename:
            raise PythonageError('PPlayingGame constructor was passed a Game with no gamename')    

        # Additional construction
        self._objects = {}
        self._next_object_id = 0

    @property
    def gamename(self):
        
        return self._game.gamename

    def __len__(self):
        
        return len(self._objects)
    
    def __setitem__(self, key, value):
        
        self._objects[key] = value

    def __getitem__(self, key):
        
        return self._objects[key]  
		
 #   def send(self, message):
 #       user.send(message)

    def create_album(self):
        
        new_album = PAlbum()
        self._objects[self._next_object_id] = new_album
        self._next_object_id += 1
        return new_album

    def create_imagedata(self, new_src):
        
        new_imagedata = PImageData(self._next_object_id, new_src, self._user)
        self._objects[self._next_object_id] = new_imagedata
        self._next_object_id += 1
        return new_imagedata

    def create_image(self, image_data_object, width, height, visible=True):
        
        new_image = PImage(self._next_object_id, image_data_object, width, height, visible, self._user)
        self._objects[self._next_object_id] = new_image
        self._next_object_id += 1
        return new_image

    def create_translate(self, x, y, visible=True):
        
        new_translate = PTranslate(self._next_object_id, x, y, visible, self._user)
        self._objects[self._next_object_id] = new_translate
        self._next_object_id += 1
        return new_translate

    def create_rotate(self, angle, visible=True):
        
        new_rotate = PRotate(self._next_object_id, x, y, visible, self._user)
        self._objects[self._next_object_id] = new_rotate
        self._next_object_id += 1
        return new_rotate

    def create_timer(self, interval, callback):
        
        timer = PTimer(interval, callback, self.gamename)
        self._user.append_timer_to_server(timer)
        return timer

    def create_timeout(self, interval, callback):
        
        timeout = PTimeout(interval, callback, self.gamename)
        self._user.append_timer_to_server(timeout)
        return timeout

    def create_sound(self, src):
        new_sound = PSound(self._next_object_id, src, self._user)
        self._objects[self._next_object_id] = new_sound
        self._next_object_id += 1
        return new_sound

    def create_pixelmap_from_imagedata(self, imagedata, width, height, visible=True):
        new_pixelmap = PPixelMap(self._next_object_id, width, height, visible, self._user)
        new_pixelmap.from_imagedata(imagedata)
        self._objects[self._next_object_id] = new_pixelmap
        self._next_object_id += 1
        return new_pixelmap

    def create_pixelmap_from_string(self, width, height, oversample, string_array, visible=True):
        new_pixelmap = PPixelMap(self._next_object_id, width, height, visible, self._user)
        data_height = len(string_array)
        data_width = len(string_array[0])
        new_pixelmap.from_string(data_width, data_height, oversample, string_array)
        self._objects[self._next_object_id] = new_pixelmap
        self._next_object_id += 1
        return new_pixelmap       

    def create_line(self, x1, y1, x2, y2, style='black', width=5, visible=True):
        js_style = JavascriptStyle.compute_style(style)
        
        new_line = PLine(self._next_object_id, x1, y1, x2, y2, js_style, width, visible, self._user)
        self._objects[self._next_object_id] = new_line
        self._next_object_id += 1
        return new_line

    def create_text(self, x, y, text, font='20px Georgia', style='black', visible=True):
        js_style = JavascriptStyle.compute_style(style)
        
        new_text = PText(self._next_object_id, x, y, font, js_style, text, visible, self._user)
        self._objects[self._next_object_id] = new_text
        self._next_object_id += 1
        return new_text

    def create_circle(self, radius, style='black', visible=True):
        js_style = JavascriptStyle.compute_style(style)
        
        new_circle = PCircle(self._next_object_id, radius, js_style, visible, self._user)
        self._objects[self._next_object_id] = new_circle
        self._next_object_id += 1
        return new_circle

    def remove_timer_from_server(self, timer):
        
        self._user.remove_timer_from_server(timer)

    def remove_timeout_from_server(self, timeout):
        
        self._user.remove_timer_from_server(timeout)

    def remove_all_timers_from_server(self, timer):
        
        self._user.remove_all_timers_from_server()

    def remove_all_from_browser(self):

        self._user.remove_all_from_browser()

    def handle_imagedata_loaded(self, object_id):
        
        self._objects[object_id].handle_imagedata_loaded()

    def update_keys(self, key_list):
        
        self._user.update_keys(key_list)

    def this_key_is_pressed(self, key):
        
        return self._user.is_pressed(key)

    @property
    def clicked(self):
        return self._user.clicked

    def reset_clicked(self):
        self._user.reset_clicked()

    @property
    def click_x(self):
        return self._user.click_x

    @property
    def click_y(self):
        return self._user.click_y

    @property
    def render_complete_notification(self):
        return self._user.render_complete_notification

    @render_complete_notification.setter
    def render_complete_notification(self, new_value):
        self._user.render_complete_notification = new_value

    @property
    def rendering(self):
        return self._user.rendering

    def log_on_client(self, message):
        self._user.log_on_client(message)

    @property
    def store_messages(self):
        return self._user.store_messages

    @store_messages.setter
    def store_messages(self, new_value):
        self._user.store_messages = new_value
    
    

        
        
