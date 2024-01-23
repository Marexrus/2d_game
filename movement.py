import pygame
import classes
#Тут будут функции для движения и все что с этим связанно

WIDTH = 700
HEIGHT = 700

def collide(player, objects):
    # print(player.x)
    Num_of_collisions = player.collidelist(objects)
    side = ''
    if Num_of_collisions >= 0:
        current_object = objects[Num_of_collisions]
        plane1 = False
        plane2 = False
        relpos = [current_object.x - player.x, current_object.y - player.y]
        relpos[0] *= (player.height + current_object.height) / (player.width + current_object.width)
        relpos[1] *= (player.width + current_object.width) / (player.height + current_object.height)
        if relpos[1] < relpos[0]:
            plane1 = False
        else:
            plane1 = True
        if relpos[1] < -relpos[0]:
            plane2 = False
        else:
            plane2 = True

        if plane1 and plane2:
            player.y = current_object.y - player.height
            side = 'up'

        if plane1 and not plane2:
            player.x = current_object.x + current_object.width
            side = 'right'

        if not plane1 and plane2:
            player.x = current_object.x - player.width
            side = 'left'

        if not plane1 and not plane2:
            player.y = current_object.y + current_object.height
            side = 'down'
        objects[Num_of_collisions] = current_object

        return side
    return None

speed=[0,0]
dir={'up':False,"down":False,"left":False,"right":False}
center = classes.Rect(WIDTH / 2, HEIGHT / 2, 1, 1,camera=False,collision=False,drawing=False)
dfmove=[0,0]
kslip=[15,15]

def move(keys,player,static_camera):
    global speed,dir,dfmove,kslip

    if static_camera:
        s=3

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.y -= s
            dir['up']=True
        else:
            dir['up']=False
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.y += s
            dir['down']=True
        else:
            dir['down']=False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= s
            dir['left']=True
        else:
            dir['left']=False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += s
            dir['right']=True
        else:
            dir['right']=False

        dfmove[0] = float(center.x - player.x) / kslip[0]
        dfmove[1] = float(center.y - player.y) / kslip[1]
        if dfmove[0] > 0 and dfmove[0] < 1:
            dfmove[0] = 1
        if dfmove[1] > 0 and dfmove[1] < 1:
            dfmove[1] = 1
        dfmove[0] = int(dfmove[0])
        dfmove[1] = int(dfmove[1])
        player.x += dfmove[0]
        player.y += dfmove[1]

        for el in classes.objects:
            if el.id == 'rect':
                if el.camera:
                    el.x += dfmove[0]
                    el.y += dfmove[1]
    else:
        kf=0.1
        speed_max=3

        if keys[pygame.K_UP]:
            dir['up']=True
            if speed[1] > -speed_max:
                speed[1]-=kf
            else:
                speed[1]+=kf
        else:
            dir['up']=False

        if keys[pygame.K_DOWN]:
            dir['down']=True
            if speed[1] < speed_max:
                speed[1]+=kf
            else:
                speed[1]-=kf
        else:
            dir['down']=False

        if keys[pygame.K_LEFT]:
            dir['left']=True
            if speed[0] > -speed_max:
                speed[0]-=kf
            else:
                speed[0]+=kf
        else:
            dir['left']=False

        if keys[pygame.K_RIGHT]:
            dir['right']=True
            if speed[0] < speed_max:
                speed[0]+=kf
            else:
                speed[0]-=kf
        else:
            dir['right']=False
        
        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            speed[0]/=1.3
            speed[1]/=1.3

        player.y+=speed[1]
        player.x+=speed[0]

    return_mas=[player,dir,speed]
    
    return return_mas