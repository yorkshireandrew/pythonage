from pythonage.playinggame import PPlayingGame

class CarLobby_PlayingGame(PPlayingGame):

    def __init__(self, user, game):
        # First thing we must do is initialise our super class
        # We tell it the name of the game it is playing so it can be shown in logging
        super().__init__(user, game)
        
        self.text = self.create_text(50,50,'Click to launch cargame',style='r')
        self.text.render()
        self.create_timer(100, self.check_for_click)

    def check_for_click(self):
        if self.clicked:
            self.launch('cargame','Launched By CarLobby')
                
        
        


        
    
