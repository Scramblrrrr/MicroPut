import sys
import pygame




class MouseEvents:
    def __init__(self, screen):
        self.screen = screen

    def mouseDown(self, game, stage, state, gameBall, mousePosition):
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
        elif game.gameMode == 'play':
            if mousePosition[0] in range(560, 640) and mousePosition[1] in range(600, 640):
                print('Going to next level...')
                game.gameStage += 1
            elif game.ballState == 'selecting speed' or game.ballState == 'stopped':
                if mousePosition[0] in range(575, 625) and mousePosition[1] in range(104, 168):
                    print("Speed = 6")
                    gameBall.speed = 6
                if mousePosition[0] in range(575, 625) and mousePosition[1] in range(170, 234):
                    print("Speed = 5")
                    gameBall.speed = 5
                if mousePosition[0] in range(575, 625) and mousePosition[1] in range(236, 300):
                    print("Speed = 4")
                    gameBall.speed = 4
                if mousePosition[0] in range(575, 625) and mousePosition[1] in range(302, 366):
                    print("Speed = 3")
                    gameBall.speed = 3
                if mousePosition[0] in range(575, 625) and mousePosition[1] in range(368, 432):
                    print("Speed = 2")
                    gameBall.speed = 2
                if mousePosition[0] in range(575, 625) and mousePosition[1] in range(434, 498):
                    print("Speed = 1")
                    gameBall.speed = 1
                else:
                    print("Invalid Selection")
            elif game.ballState == 'free':
                if game.gameStage == 1:
                    if mousePosition[0] in range(113, 229) and mousePosition[1] in range(489, 532):
                        print("in box")
                        game.ballState = 'placed'
                    else:
                        print('Invalid Ball Location')
                elif game.gameStage == 2:
                    if mousePosition[0] in range(380, 510) and mousePosition[1] in range(90, 150):
                        print("in box")
                        game.ballState = 'placed'
                    else:
                        print('Invalid Ball Location')
                elif game.gameStage == 3:
                    if mousePosition[0] in range(494, 530) and mousePosition[1] in range(66, 153):
                        print("in box")
                        game.ballState = 'placed'
                    else:
                        print('Invalid Ball Location')
                elif game.gameStage == 4:
                    if mousePosition[0] in range(210, 348) and mousePosition[1] in range(493, 539):
                        print("in box")
                        game.ballState = 'placed'
                    else:
                        print('Invalid Ball Location')
                elif game.gameStage == 5:
                    if mousePosition[0] in range(512, 545) and mousePosition[1] in range(45, 127):
                        print("in box")
                        game.ballState = 'placed'
                    else:
                        print('Invalid Ball Location')
                else:
                    pass




"""
mission for friday
make your program print a message when you click "start game" on the splash screen
make your program quit when you click quit
put
 a 'load game' in your splash screen, this wont work yet
"""