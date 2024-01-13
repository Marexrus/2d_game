import pygame

objects=[]

def mas_calc(m1,m2):
    for i in range(len(m1)):
        if m1[i] + m2[i] < 0:
            m1[i]=0
        else:
            m1[i]+=m2[i]
    return m1

class Rect:
    def __init__(self,x,y,width,height):
        self.id='rect'
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.prect = pygame.Rect(self.x, self.y, self.width, self.height)
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
        pygame.draw.rect(screen,color,self.prect)
        
def label(screen,text, pos,color=[255,0,255],size=48,f=None):
    font = pygame.font.Font(f, size)
    text_render = font.render(text, False, color)
    screen.blit(text_render, pos)

class Button:
    def __init__(self,screen,func,rect,text,text_pos=[10,10],bg=[97,97,97],color=[0,0,0],size=48):
        self.id='button'
        self.screen=screen

        self.func=func
        self.rect=rect
        self.bg=bg
        self.bg0=bg
        self.bg=self.bg0.copy()
        self.text=text
        self.color=color
        self.size=size
        self.text_pos=[self.rect.x+10,self.rect.y+10]
        #text_pos выставляется относительно фона кнопки
        self.text_pos=[self.rect.x+text_pos[0],self.rect.y+text_pos[1]]

        objects.append(self)

    def draw(self):
        pygame.draw.rect(self.screen,self.rect,self.bg)
        label(self.screen,self.text,[self.rect.x,self.rect.y])
    def draw(self,mrect):
        self.bg=self.bg0.copy()
        if self.rect.colliderect(mrect.prect):
            self.bg=mas_calc(self.bg,[-20,-20,-20])

        pygame.draw.rect(self.screen,self.bg,self.rect.prect)
        label(self.screen,self.text,self.text_pos,self.color,self.size)

    def check(self, mrect):
        # self.mrect = mrect
        if self.rect.colliderect(mrect.prect):
            self.func()