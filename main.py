import pygame
from pygame import *
from lib.maps import *
from pygame.locals import *
import sys
import time
import mouse_events
from lib.sprites import *
import math


pygame.init()   # starts the pygame environment
# instantiate screen object
screenx = 640
screeny = 640
screen = pygame.display.set_mode((screenx, screeny))
pygame.display.set_caption('Micro Putt')
game_font = pygame.font.SysFont('comicsansms', 24)
icon = sprites['Golf Ball']
pygame.display.set_icon(icon)

class Game:
    """
    Game class handles all the permanent game stats such as score, game mode, current maps
    Also keeps track of the game state such as mode (splash screen, main game, paused, etc)
    """
    def __init__(self):
        self.gameMode = 'splash'
        self.ballState = 'splash'
        self.gameStage = 1
        self.speedSelector = 'hidden'
        #blalblblbala
        #something

# mx, my = pygame.mouse.get_pos()

class Ball(pygame.sprite.Sprite):
    """
    Attributes: directionX, directionY, initialAngle, currentAngle, speed, image
    Methods:    update(), collide()
    """
    def __init__(self):
        super().__init__()
        self.image = sprites['Golf Ball']
        self.rect = self.image.get_rect()
        self.rect.center = (165, 500)
        self.angle = math.radians(180+95)
        self.speed = 0
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed
        self.positionx = self.rect.center[0]
        self.positiony = self.rect.center[1]
        #self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed
        self.positionx += self.dx
        self.positiony += self.dy
        self.rect.center = (self.positionx, self.positiony)
        if self.speed > 0:
            self.speed = self.speed - 0.025
        else:
            self.speed = 0
        #print(self.dx, self.dy)
        #print(self.positionx,self.positiony)

    def bumperhit(self,bumper):
        alpha = math.degrees(self.angle) - bumper.angle
        bounceangle = 180 - 2*alpha + math.degrees(self.angle)
        self.angle = math.radians(bounceangle)
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed


class Bumper(pygame.sprite.Sprite):

    def __init__(self,center_pixel):
        """
        :param center_pixel: where the bumper is placed on the screen
        """
        super().__init__()
        self.image = sprites['Bumper45']
        self.angle = 45
        print(self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = center_pixel


def renderMap(mapFile, row, column):
    screen.blit(mapFile, (row, column))


def splashScreen(a, b, c):

    #drawing text:
    #font.render()
    #blit()
    #render()
    #text = a string literal object
    #antialias = takes an 8 bit image and "smooths is" by remapping it to a 24 bit image
    #color
    #background
    word = game_font.render(a, None, (0, 0, 0))
    screen.blit(word, (b,c))
    pygame.display.flip()


pygame.init()
currentMap = maps['Homescreen']
stage = Game()
game = Game()
state = Game()
gameBall = Ball()
ball_group = pygame.sprite.Group()
ball_group.add(gameBall)
bumper1 = Bumper((82 + (141/2),56 + (141/2)))
bumper_group = pygame.sprite.Group()
bumper_group.add(bumper1)
gameBall.image = pygame.transform.scale(gameBall.image, (16, 16))

def main():
    mouseEvents = mouse_events.MouseEvents(screen)
    while game.gameMode == 'splash':
        game.ballstate = 'splash'
        time.sleep(1/60)    # limits event polling to 60 times per second
        for event in pygame.event.get():    # iterate the event stack
            if event.type == pygame.QUIT:
                pygame.quit()   # closes pygame
                sys.exit()      # releases system resources
            if event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                print("x:", mx, "y:", my)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print("x:", mx, "y:", my)
                mouseEvents.mouseDown(game, stage, state, pygame.mouse.get_pos())
        renderMap(mapFile=currentMap, row=0, column=0)
        pygame.draw.rect(surface=currentMap, color=(0, 255, 0), rect=((320, 200), (100, 40)))
        splashScreen("Play", 350, 205)
        pygame.draw.rect(surface=currentMap, color=(255, 0, 0), rect=((320, 400), (100, 40)))
        splashScreen("Exit", 350, 405)
        pygame.draw.rect(surface=currentMap, color=(255, 255, 0), rect=((320, 300), (100, 40)))
        splashScreen("Load", 350, 305)
        pygame.display.flip()

def play():
    currentMap = maps['Clouds']
    Hole = sprites['Hole']
    Ball = sprites['Golf Ball']
    SpeedChart = maps['SpeedChart']
    mouseEvents = mouse_events.MouseEvents(screen)
    while game.gameMode == 'play':
        time.sleep(1/60)
        mixer.music.load('./sounds/Elsie.mp3')
        mixer.music.play(-1)
        game.ballState = 'free'
        while game.gameStage == 1:
            time.sleep(1/60)
            currentStage = maps['Map1']
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exiting...")
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    mx, my = pygame.mouse.get_pos()
                    print("x:", mx, "y:", my)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print("x:", mx, "y:", my)
                    mouseEvents.mouseDown(game, stage, state, pygame.mouse.get_pos())
            renderMap(mapFile=currentMap, row=0, column=0)
            renderMap(mapFile=currentStage, row=0, column=0)
            renderMap(mapFile=Hole, row=495, column=115)
            renderMap(mapFile=SpeedChart, row=575, column=100)
            bumper_group.draw(screen)
            mx, my = pygame.mouse.get_pos()
            if game.ballState == 'free':
                renderMap(mapFile=Ball, row=(mx-16), column=(my-16))
            pygame.draw.rect(surface=currentMap, color=(82, 82, 77), rect=((560, 600), (80, 40)))
            splashScreen("Next", 570, 600)
            if game.ballState == 'placed':
                gameBall.positionx = mx+8
                gameBall.positiony = my+8
                game.ballState = 'selecting speed'
            while game.ballState == 'selecting speed':
                time.sleep(1/60)
                # renderMap(mapFile=maps['SpeedChart'], row=575, column=100)
                if gameBall.speed >= 1 and gameBall.speed <= 6:
                    game.ballState = 'moving'
            if game.ballState == 'moving':
                gameBall.update()
                ball_group.draw(screen)
                pygame.display.flip()
                bumper_hits = pygame.sprite.spritecollide(gameBall,bumper_group, False, pygame.sprite.collide_mask)
                if bumper_hits:
                    gameBall.bumperhit(bumper1)
        game.ballState = 'free'
        while game.gameStage == 2:
            currentStage = maps['Map2']
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exiting...")
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    mx, my = pygame.mouse.get_pos()
                    print("x:", mx, "y:", my)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print("x:", mx, "y:", my)
                    mouseEvents.mouseDown(game, stage, state, pygame.mouse.get_pos())
                renderMap(mapFile=currentMap, row=0, column=0)
                renderMap(mapFile=currentStage, row=0, column=0)
                renderMap(mapFile=Hole, row=125, column=80)
                mx, my = pygame.mouse.get_pos()
                if game.ballState == 'free':
                    renderMap(mapFile=Ball, row=(mx - 16), column=(my - 16))
                pygame.draw.rect(surface=currentMap, color=(82, 82, 77), rect=((560, 600), (80, 40)))
                splashScreen("Next", 570, 600)
                pygame.display.flip()
        game.ballState = 'free'
        while game.gameStage == 3:
            currentStage = maps['Map3']
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exiting...")
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    mx, my = pygame.mouse.get_pos()
                    print("x:", mx, "y:", my)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print("x:", mx, "y:", my)
                    mouseEvents.mouseDown(game, stage, state, pygame.mouse.get_pos())
                renderMap(mapFile=currentMap, row=0, column=0)
                renderMap(mapFile=currentStage, row=0, column=0)
                renderMap(mapFile=Hole, row=90, column=485)
                mx, my = pygame.mouse.get_pos()
                if game.ballState == 'free':
                    renderMap(mapFile=Ball, row=(mx - 16), column=(my - 16))
                pygame.draw.rect(surface=currentMap, color=(82, 82, 77), rect=((560, 600), (80, 40)))
                splashScreen("Next", 570, 600)
                pygame.display.flip()
        game.ballState = 'free'
        while game.gameStage == 4:
            currentStage = maps['Map4']
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exiting...")
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    mx, my = pygame.mouse.get_pos()
                    print("x:", mx, "y:", my)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print("x:", mx, "y:", my)
                    mouseEvents.mouseDown(game, stage, state, pygame.mouse.get_pos())
                renderMap(mapFile=currentMap, row=0, column=0)
                renderMap(mapFile=currentStage, row=0, column=0)
                renderMap(mapFile=Hole, row=265, column=65)
                mx, my = pygame.mouse.get_pos()
                if game.ballState == 'free':
                    renderMap(mapFile=Ball, row=(mx - 16), column=(my - 16))
                pygame.draw.rect(surface=currentMap, color=(82, 82, 77), rect=((560, 600), (80, 40)))
                splashScreen("Next", 570, 600)
                pygame.display.flip()
        game.ballState = 'free'
        while game.gameStage == 5:
            currentStage = maps['Map5']
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exiting...")
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    mx, my = pygame.mouse.get_pos()
                    print("x:", mx, "y:", my)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print("x:", mx, "y:", my)
                    mouseEvents.mouseDown(game, stage, state, pygame.mouse.get_pos())
                renderMap(mapFile=currentMap, row=0, column=0)
                renderMap(mapFile=currentStage, row=0, column=0)
                renderMap(mapFile=Hole, row=90, column=515)
                mx, my = pygame.mouse.get_pos()
                if game.ballState == 'free':
                    renderMap(mapFile=Ball, row=(mx - 16), column=(my - 16))
                pygame.draw.rect(surface=currentMap, color=(82, 82, 77), rect=((560, 600), (80, 40)))
                splashScreen("Next", 570, 600)
                if game.gameStage == 6:
                    game.gameStage = 1
                    game.gameMode = 'splash'
                pygame.display.flip()

# GAME:

currentLevel = 1
main()
while True:
    if game.gameMode == 'play':
        play()
    else:
        main()





# on launch show clouds background
# show 3 buttons ontop of background
#     1. Play
#         will prompt the game to start
#     2. High-Scores
#         will display top 5 scores with 4 digit names
#     3. Exit
#         will exit the program
#
# once play option is selected, prompt map1 to appear and allow the user to begin game
# once game has begun, allow player to drop their ball anywhere withen the dark green oval
# once ball is dropped allow player to aim and adjust ball speed
# once an imput is take from the mouse, make the ball move accordingly
# ball should have direction and speed reflected after making contact with a brown surface
# ball should disappear and play sound once it makes contact with black hole
# after this first stage it should repeat the process but change the map
# this should repeat untill all maps are completed
# user's score should be compared to previous scores and if it is in top 5 players, allow player to add their score and 4 digit name
#
