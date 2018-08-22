from playinggame import *
import time

class Car_PlayingGame(PPlayingGame):

    def __init__(self, user, server_services):
        super().__init__(user, server_services) # First thing must be initialise our super class
        
        car_imagedata = self.create_imagedata('cardata,img/car_side1_4.bmp')
        car_album = self.create_album()
        car_album['thecar'] = car_imagedata
        while car_album.not_loaded:
            print('waiting for album load')
            time.sleep(100) # Should not really do async waiting like this but we are still in dev phase

        car_image = self.create_image(car_imagedata, 100, 100)
        translate = self.create_translate(0,0)
        translate.append()
        self.translate = translate
        # todo call render
        


        
    
