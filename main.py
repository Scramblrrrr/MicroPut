import pygame
from pygame import *
from lib.maps import *
from pygame.locals import *
import sys
import time
import mouse_events
from lib.sprites import *
import math
import pygame, math, sys

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
        self.par = 0
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
        self.angle = math.radians(270)
        self.speed = 7
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed
        self.positionx = self.rect.center[0]
        self.positiony = self.rect.center[1]

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

    def bumperhit(self,bumper):
        alpha = math.degrees(self.angle) - bumper.angle
        bounceangle = 180 - 2*alpha + math.degrees(self.angle)
        self.angle = math.radians(bounceangle)
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed

    def wallhit(self,wall):
        alpha = math.degrees(self.angle) - wall.angle
        bounceangle = 180 - 2*alpha + math.degrees(self.angle)
        self.angle = math.radians(bounceangle)
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed

gameBall = Ball()


# SLIDERS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 50)
BLUE = (50, 50, 255)
GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
TRANS = (1, 1, 1)

font = pygame.font.SysFont("Verdana", 12)

class Slider():
    def __init__(self, name, val, maxi, mini, pos):
        self.val = val  # start value
        self.maxi = maxi  # maximum at slider position right
        self.mini = mini  # minimum at slider position left
        self.xpos = pos  # x-location on screen
        self.ypos = 590
        self.surf = pygame.surface.Surface((100, 50))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction

        self.txt_surf = font.render(name, 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(center=(50, 15))

        # Static graphics - slider background #
        self.surf.fill((100, 100, 100))
        pygame.draw.rect(self.surf, GREY, [0, 0, 100, 50], 3)
        pygame.draw.rect(self.surf, CYAN, [10, 10, 80, 10], 0)
        pygame.draw.rect(self.surf, BLACK, [10, 30, 80, 5], 0)

        self.surf.blit(self.txt_surf, self.txt_rect)  # this surface never changes

        # dynamic graphics - button surface #
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        pygame.draw.circle(self.button_surf, BLACK, (10, 10), 6, 0)
        pygame.draw.circle(self.button_surf, CYAN, (10, 10), 4, 0)

    def draw(self):
        """ Combination of static and dynamic graphics in a copy of
    the basic slide surface
    """
        # static
        surf = self.surf.copy()

        # dynamic
        pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*80), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)  # move of button box to correct screen position

        # screen
        screen.blit(surf, (self.xpos, self.ypos))

    def move(self):
        """
    The dynamic part; reacts to movement of the slider button.
    """
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi

angle = Slider("Angle", 270, 450, 90, 455)

slides = [angle]

# END OF SLIDERS

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

class Wall(pygame.sprite.Sprite):
    def __init__(self,center_pixel):
        super().__init__()
        self.image = sprites['Wall']
        self.angle = 90
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
ball_group = pygame.sprite.Group()
ball_group.add(gameBall)
bumper1 = Bumper((80 + (141/2),54 + (141/2)))
bumper_group = pygame.sprite.Group()
bumper_group.add(bumper1)
gameBall.image = pygame.transform.scale(gameBall.image, (16, 16))

# walls

# stage 1
wall_group_V = pygame.sprite.Group()
wall_group_H = pygame.sprite.Group()
wall1 = Wall((90,540))
wall1.image = pygame.transform.scale(wall1.image, (200, 1))
wall1.angle = 0
wall_group_H.add(wall1)
wall2 = Wall((96,52))
wall2.image = pygame.transform.scale(wall2.image, (1, 500))
wall2.angle = 90
wall_group_V.add(wall2)
wall3 = Wall((280,198))
wall3.image = pygame.transform.scale(wall3.image, (1, 350))
wall3.angle = 90
wall_group_V.add(wall3)
wall4 = Wall((280,198))
wall4.image = pygame.transform.scale(wall4.image, (300, 1))
wall4.angle = 0
wall_group_H.add(wall4)
wall5 = Wall((571, 53))
wall5.image = pygame.transform.scale(wall5.image, (1, 150))
wall5.angle = 90
wall_group_V.add(wall5)
wall6 = Wall((82, 56))
wall6.image = pygame.transform.scale(wall6.image, (500,1))
wall6.angle = 0
wall_group_H.add(wall6)



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
                mouseEvents.mouseDown(game, stage, state, gameBall, pygame.mouse.get_pos())
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
    Score = maps['Score']
    mouseEvents = mouse_events.MouseEvents(screen)
    while game.gameMode == 'play':
        time.sleep(1/60)
        mixer.music.load('./sounds/Elsie.mp3')
        # mixer.music.play(-1)
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
                    mouseEvents.mouseDown(game, stage, state, gameBall, pygame.mouse.get_pos())
            renderMap(mapFile=currentMap, row=0, column=0)
            renderMap(mapFile=currentStage, row=0, column=0)
            renderMap(mapFile=Hole, row=495, column=115)
            bumper_group.draw(screen)
            wall_group_H.draw(screen)
            wall_group_V.draw(screen)
            mx, my = pygame.mouse.get_pos()
            if game.ballState == 'free':
                renderMap(mapFile=Ball, row=(mx-16), column=(my-16))
            pygame.draw.rect(surface=currentMap, color=(82, 82, 77), rect=((560, 600), (80, 40)))
            splashScreen("Next", 570, 600)
            if game.ballState == 'placed':
                time.sleep(1/60)
                gameBall.positionx = mx+8
                gameBall.positiony = my+8
                bdx = mx+8
                bdy = my+8
                gameBall.rect.center = (bdx, bdy)
                ball_group.draw(screen)
                game.ballState = 'selecting speed'
            while game.ballState == 'selecting speed':
                # attempting slider
                time.sleep(1/60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("Exiting...")
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        mx, my = pygame.mouse.get_pos()
                        print("x:", mx, "y:", my)
                        mouseEvents.mouseDown(game, stage, state, gameBall, pygame.mouse.get_pos())
                        for s in slides:
                            if s.button_rect.collidepoint(pos):
                                s.hit = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                        for s in slides:
                            s.hit = False
                            gameBall.angle = math.radians(angle.val)
                            renderMap(mapFile=currentMap, row=0, column=0)
                            renderMap(mapFile=currentStage, row=0, column=0)
                            renderMap(mapFile=Hole, row=495, column=115)
                            bumper_group.draw(screen)
                            wall_group_H.draw(screen)
                            wall_group_V.draw(screen)
                            ball_group.draw(screen)
                            pygame.draw.line(surface=screen,
                                             color=(122,165,221),
                                             start_pos=gameBall.rect.center,
                                             end_pos= (gameBall.rect.center[0] + 100 * math.cos(gameBall.angle), gameBall.rect.center[1]+100*math.sin(gameBall.angle)),
                                             width=5)
                for s in slides:
                    if s.hit:
                        s.move()
                for s in slides:
                    s.draw()
                pygame.display.flip()
                print(angle.val)
                #     end of slider attempt
                renderMap(mapFile=SpeedChart, row=575, column=100)
                if gameBall.speed >= 1 and gameBall.speed <= 6:
                    game.ballState = 'moving'
                pygame.display.flip()
            if game.ballState == 'moving':
                gameBall.update()
                ball_group.draw(screen)
                pygame.display.flip()
                bumper_hits = pygame.sprite.spritecollide(gameBall,bumper_group, False, pygame.sprite.collide_mask)
                if bumper_hits:
                    gameBall.bumperhit(bumper1)
                for wall in wall_group_V:
                    wall_hits_V = pygame.sprite.spritecollide(gameBall,wall_group_V, False, pygame.sprite.collide_mask)
                    if wall_hits_V:
                        gameBall.wallhit(wall1)
                for wall in wall_group_H:
                    wall_hits_H = pygame.sprite.spritecollide(gameBall,wall_group_H, False, pygame.sprite.collide_mask)
                    if wall_hits_H:
                        gameBall.wallhit(wall2)
                if gameBall.rect.center[0] in range(510,525) and gameBall.rect.center[1] in range(120,150):
                    gameBall.speed = 0
                    print("SCORE")
                    game.ballState = 'score'
            if game.ballState == 'score':
                renderMap(mapFile=Score, row=300, column=300)
                pygame.display.flip()
                print('Good Job')
                print('Par: ',game.par)
                time.sleep(1.5)
                game.gameStage += 1
                game.ballState = 'free'
                gameBall.speed = 7
            #     if ballsprite center is over black (hole), ball disappears, score
            if gameBall.speed == 0:
                if game.ballState != 'score':
                    print("Stopped!")
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
                            mouseEvents.mouseDown(game, stage, state, gameBall, pygame.mouse.get_pos())
                    game.ballState = 'stopped'
                    gameBall.speed = 7
            while game.ballState == 'stopped':
                # attempting slider
                time.sleep(1 / 60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("Exiting...")
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        mx, my = pygame.mouse.get_pos()
                        print("x:", mx, "y:", my)
                        mouseEvents.mouseDown(game, stage, state, gameBall, pygame.mouse.get_pos())
                        for s in slides:
                            if s.button_rect.collidepoint(pos):
                                s.hit = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                        for s in slides:
                            s.hit = False
                            gameBall.angle = math.radians(angle.val)
                            renderMap(mapFile=currentMap, row=0, column=0)
                            renderMap(mapFile=currentStage, row=0, column=0)
                            renderMap(mapFile=Hole, row=495, column=115)
                            bumper_group.draw(screen)
                            wall_group_H.draw(screen)
                            wall_group_V.draw(screen)
                            ball_group.draw(screen)
                            pygame.draw.line(surface=screen,
                                             color=(122, 165, 221),
                                             start_pos=gameBall.rect.center,
                                             end_pos=(gameBall.rect.center[0] + 100 * math.cos(gameBall.angle),
                                                      gameBall.rect.center[1] + 100 * math.sin(gameBall.angle)),
                                             width=5)
                for s in slides:
                    if s.hit:
                        s.move()
                for s in slides:
                    s.draw()
                pygame.display.flip()
                print(angle.val)
                #     end of slider attempt
                renderMap(mapFile=SpeedChart, row=575, column=100)
                if gameBall.speed >= 1 and gameBall.speed <= 6:
                    game.ballState = 'moving'
                pygame.display.flip()
                    #^^^ code allowing user to re-swing
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
                    mouseEvents.mouseDown(game, stage, state, gameBall, pygame.mouse.get_pos())
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
                    mouseEvents.mouseDown(game, stage, state, gameBall, pygame.mouse.get_pos())
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
                    mouseEvents.mouseDown(game, stage, state, gameBall, pygame.mouse.get_pos())
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
                    mouseEvents.mouseDown(game, stage, state, gameBall, pygame.mouse.get_pos())
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

try:    # error handling
    f = open('High Score.txt', 'x')
    f.close()
except FileExistsError:
    print("File exists...\nProceding to open existing file...")
f = open('High Score.txt', 'r')
PreviousHS = f.readline()
f.close()
print("PreviousHS: ", PreviousHS)
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
