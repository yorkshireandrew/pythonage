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
            self.render_complete_notification = True
            self.car_loaded = True
            print('album loaded')
            car_image = self.create_image(self.car_imagedata, 100, 100)
            car_image.scale = 0.25
            translate = self.create_translate(0,0)
            translate.append(car_image)
            translate2 = self.create_translate(0,0)
            self.translate = translate
            self.translate2 = translate2
            
            self.car_pixelmap = self.create_pixelmap_from_imagedata(self.car_imagedata, 100,100)
            self.car_pixelmap.make_blue_transparent()
            self.car_pixelmap.layer = 1
            
            self.translate2.append(self.car_pixelmap)
            self.translate2.append(translate) # translate now after car_pixelmap

            self.translate2.render_layers()

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

            self.store_messages = True
            self.dood_pixelmap = self.create_pixelmap_from_string(50, 80, 10, dood)
            self.dood_pixelmap.render()
            self.line = self.create_line(0, 10, 10, 10,'r', 2, True)
            self.line.scale = 1
            self.line.render()

            self.text = self.create_text(50,50,'Yippee',style='r')
            self.text.render()
            self.text.text = 'FOOOBARRR'
            self.text.update()
            self.text.render()
            self.store_messages = False

            self.translate3 = self.create_translate(0,0)
            self.circle = self.create_circle(10, 'O')
            self.translate3.append(self.circle)
            

        if self.car_album.loaded:
            pass
            #self.sound.play()

        if self.car_loaded:
            self.translate.x += 10
            if self.this_key_is_pressed('a'):
                self.translate.x -= 20
            print('First translate update')
            self.translate.update()
            print('Second translate update')
            self.translate2.update()
            self.translate2.render_layers()
            self.log_on_client('<foo,bar>')

            if self.clicked:
                self.reset_clicked()
                self.line.x2 = self.click_x
                self.line.y2 = self.click_y
                self.line.update()
                self.line.render()
                self.remove_all_from_browser() # should stop everything on browser

                self.translate3.x = self.click_x
                self.translate3.y = self.click_y
                self.translate3.update()
                self.translate3.render()
                self.circle.radius += 10
                
        
        


        
    
