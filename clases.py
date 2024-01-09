#Тут будут все полезные классы
#id класса пишется с маленькой буквы

import pygame

class Rect:
    def __init__(self,x,y,width,height,objects):
        self.id='rect'
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.prect=pygame.Rect(self.x,self.y,self.width,self.height)
        objects.append(self)
    
    def colliderect(self, c1):
        self.prect = pygame.Rect(self.x, self.y, self.width, self.height)
        c1 = pygame.Rect(c1.x, c1.y, c1.width, c1.height)
        return self.prect.colliderect(c1)

    def collidelist(self, arr):
        self.prect = pygame.Rect(self.x, self.y, self.width, self.height)
        for el in arr:
            rr = pygame.Rect(el.x, el.y, el.width, el.height)
            arr[arr.index(el)] = rr
        return self.prect.collidelist(arr)
    
    def draw(self,screen,color=[255,0,0]):
        pygame.draw.rect(screen,(color),[self.x,self.y,self.width,self.height])
 

def label(screen,text, pos,color=[255,0,255],size=48,f=None):
    font = pygame.font.Font(f, size)
    text_render = font.render(text, False, color)
    screen.blit(text_render, pos)


class Button:
    def __init__(self,objects,screen,rect,text,bg=[97,97,97],color=[0,0,0],size=48):
        self.id='button'
        self.screen=screen
        self.rect=rect
        self.bg=bg
        self.text=text
        self.color=color
        self.size=size
        self.text_pos=[self.rect.x+10,self.rect.y+10]
        objects.append(self)
    
    def draw(self):
        pygame.draw.rect(self.screen,self.rect,self.bg)
        label(self.screen,self.text,[self.rect.x,self.rect.y])
