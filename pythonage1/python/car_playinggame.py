from pythonage.playinggame import PPlayingGame

class Car_PlayingGame(PPlayingGame):

    def __init__(self, user, game):
        # First thing we must do is initialise our super class
        # We tell it the name of the game it is playing so it can be shown in logging
        super().__init__(user, game)
        
        self.car_imagedata = self.create_imagedata('img/car_side1_4.bmp')
        self.car_album = self.create_album()
        self.car_album.append(self.car_imagedata)
        self.car_loaded = False
        self.create_timer(100, self.check_car_loaded)
        self.sound = self.create_sound('sound/punch.wav')
        self.car_album.append(self.sound)

    def check_car_loaded(self):
        print('check car loaded called')
        self.update_keys(('a','s','w','d'))
        
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
            
            self.car_pixelmap = self.create_pixelmap_from_imagedata(self.car_imagedata, 50,50)
            self.car_pixelmap.make_blue_transparent()
            self.car_pixelmap.render()

            dood = [
                '   BBBB   ',
                '   pppp   ',
                '   pppp   ',
                '    RR    ',
                ' BBBBBBBB ',
                ' B BBBB B ',
                ' B BBBB B ',
                ' B BBBB B ',
                '   BBBB   ',
                '   YYYY   ',
                '   Y  Y   ',
                '   Y  Y   ',
                '   Y  Y   '              
                ]

            #self.dood_pixelmap = self.create_pixelmap_from_string(50, 50, 10, dood)
            #self.dood_pixelmap.render()
            self.line = self.create_line(0, 0, 100, 100,'r', 2, True)
            self.line.render()

            self.text = self.create_text(50,50,'Yippee',style='r')
            self.text.render()
            self.text.text = 'FOOOBARRR'
            self.text.update()
            self.text.render()

        if self.car_album.loaded:
            pass
            #self.sound.play()

        if self.car_loaded:
            self.translate.x += 10
            if self.key_pressed('a'):
                self.translate.x -= 20
            self.translate.update()
            #self.translate2.render()

            if self.clicked:
                self.line.x2 = self.click_x
                self.line.y2 = self.click_y
                self.line.update()
                self.line.render()
                
                
        
        


        
    
