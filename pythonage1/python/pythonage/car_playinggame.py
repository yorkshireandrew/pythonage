from playinggame import *
import time

class Car_PlayingGame(PPlayingGame):

    def __init__(self, user, server_services):
        super().__init__(user, server_services) # First thing must be initialise our super class
        
        self.car_imagedata = self.create_imagedata('img/car_side1_4.bmp')
        self.car_album = self.create_album()
        self.car_album.append(self.car_imagedata)
        self.car_loaded = False
        
        server_services.create_timer('someuser', 100, self.check_car_loaded)

    def check_car_loaded(self):
        print('check car loaded called')
        
        if not self.car_loaded and self.car_album.loaded:
            self.car_loaded = True
            print('album loaded')
            car_image = self.create_image(self.car_imagedata, 100, 100)
            translate = self.create_translate(0,0)
            translate.append(car_image)
            translate2 = self.create_translate(0,0)
            translate2.append(translate)
            self.translate = translate
            self.translate2 = translate2
            self.translate2.render()

        if self.car_loaded:
            self.translate.x += 10
            self.translate.update()
            self.translate2.render()
        
        


        
    
