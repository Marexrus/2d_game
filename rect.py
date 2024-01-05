import pygame

class Rect:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.prect=pygame.Rect(self.x,self.y,self.width,self.height)
    
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