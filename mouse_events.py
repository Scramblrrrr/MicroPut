import sys
import pygame

class MouseEvents:
    def __init__(self, screen):
        self.screen = screen

    def mouseDown(self, game, mousePosition):
        if game.gameMode == 'splash':
            if mousePosition[0] in range(320, 420) and mousePosition[1] in range(200, 240):
                print('You have clicked play!')
                game.gameMode = 'play'
            elif mousePosition[0] in range(320, 420) and mousePosition[1] in range(300, 340):
                print('You have clicked load!')
            elif mousePosition[0] in range(320, 420) and mousePosition[1] in range(400, 440):
                print('Exiting...')
                pygame.quit()
                sys.exit()
            else:
                print('No valid option selected!')


    # def mouseMove(self):


"""
mission for friday
make your program print a message when you click "start game" on the splash screen
make your program quit when you click quit
put
 a 'load game' in your splash screen, this wont work yet
"""