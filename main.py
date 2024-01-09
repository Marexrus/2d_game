import pygame
import random
import time
from math import *
from movement import *
from classes import *
import sys

print(objects)


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

player=Rect(WIDTH/2-20,HEIGHT/2-20,20,20)
c1=Rect(300,100,20,20)

Button(screen,sys.exit,Rect(WIDTH-100,HEIGHT-60,80,40),'Exit',text_pos=[15,15],size=30)

running = True
while running:
    screen.fill(GRAY)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mpos = pygame.mouse.get_pos()
    mrect = Rect(mpos[0],mpos[1],1,1)
    pressed = pygame.mouse.get_pressed()

    keys = pygame.key.get_pressed()
    cords = move(keys)
    
    player.x += cords[0]
    player.y += cords[1]
    
    #collide(player,[c1])
    


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
