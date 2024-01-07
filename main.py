import pygame
import random
import time
from math import *
from rect import Rect
from collision import *


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

player=Rect(100,100,20,20)
c1=Rect(200,100,20,20)

running = True
while running:
    screen.fill(GRAY)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.x+=1
    c1.x-=1

    collide(player,[c1])

    player.draw(screen)
    c1.draw(screen,color=[0,0,255])

    pygame.display.update()
pygame.quit()
