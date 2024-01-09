import pygame
import random
import time
from math import *
from clases import *
from movement import *
import sys


WIDTH = 700
HEIGHT = 700
FPS = 144

BLACK = (0, 0, 0)
GRAY=(128,128,128)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

objects=[]

player=Rect(WIDTH/2-20,HEIGHT/2-20,20,20,objects)
c1=Rect(300,100,20,20,objects)

Button(objects,screen,sys.exit,Rect(10,10,100,60,objects),'None')

running = True
while running:
    screen.fill(GRAY)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mpos = pygame.mouse.get_pos()
    mrect = Rect(mpos[0],mpos[1],1,1,objects)
    pressed = pygame.mouse.get_pressed()

    keys = pygame.key.get_pressed()
    cords = move(keys)
    #player.x += cords[0]
    #player.y += cords[1]
    c1.x -= cords[0]
    c1.y -= cords[1]
        

    collide(player,[c1])

    label(screen,"Hello world!",[10,10],color=[0,0,0],size=30)

    for el in objects:
        if el.id == 'button':
            el.draw(mrect)
            if pressed[0]:
                el.check(mrect)

    player.draw(screen)
    c1.draw(screen,color=[0,0,255])

    pygame.display.update()
pygame.quit()
