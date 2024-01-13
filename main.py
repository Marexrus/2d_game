import pygame
import random
import time
from math import *
from classes import *
from movement import *


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

running = True
while running:
    screen.fill(GRAY)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    moving=move(keys,player)
    player = moving[0]
    pygame.display.set_caption(str(moving[2]))

    
    collide(player,[c1])


    label(screen,"Hello world!",[10,10],color=[0,0,0],size=30)

    player.draw(screen)
    c1.draw(screen,color=[0,0,255])

    pygame.display.update()
pygame.quit()
