import sys
import pygame




class MouseEvents:
    def __init__(self, screen):
        self.screen = screen

    def mouseDown(self, game, stage, state, mousePosition):
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
                stage.gameStage += 1
            elif state.ballState == 'free':
                if stage.gameStage == 1:
                    if mousePosition[0] in range(113, 229) and mousePosition[1] in range(489, 532):
                        print("in box")
                        state.ballState = 'placed'
                    else:
                        pass
                elif stage.gameStage == 2:
                    if mousePosition[0] in range(100, 200) and mousePosition[1] in range(100, 200):
                        print("in box")
                        state.ballState = 'placed'
                    else:
                        pass
                elif stage.gameStage == 3:
                    if mousePosition[0] in range(100, 200) and mousePosition[1] in range(100, 200):
                        print("in box")
                        state.ballState = 'placed'
                    else:
                        pass
                elif stage.gameStage == 4:
                    if mousePosition[0] in range(100, 200) and mousePosition[1] in range(100, 200):
                        print("in box")
                        state.ballState = 'placed'
                    else:
                        pass
                elif stage.gameStage == 5:
                    if mousePosition[0] in range(100, 200) and mousePosition[1] in range(100, 200):
                        print("in box")
                        state.ballState = 'placed'
                    else:
                        pass
                else:
                    pass



    # def mouseMove(self):


"""
mission for friday
make your program print a message when you click "start game" on the splash screen
make your program quit when you click quit
put
 a 'load game' in your splash screen, this wont work yet
"""