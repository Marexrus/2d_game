#Тут будут функции для движения и все что с этим связанно
import pygame

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

speed=0.8
def move(keys):
    #cords=[0,0]
    """global speed
    speed_max=2
    speed_min=0
    kf=0.02

    if keys[pygame.K_UP]:
        if speed[1] > -speed_max:
            speed[1]-=kf

    if keys[pygame.K_DOWN]:
        if speed[1] < speed_max:
            speed[1]+=kf

    if keys[pygame.K_LEFT]:
        if speed[0] > -speed_max:
            speed[0]-=kf

    if keys[pygame.K_RIGHT]:
        if speed[0] < speed_max:
            speed[0]+=kf
    
    if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        if speed[0] != 0 or speed[1] != 0: 
            if speed[0] < 0:
                speed[0]+=kf
            else:
                speed[0]-=kf
            
            if speed[1] < 0:
                speed[1]+=kf
            else:
                speed[1]-=kf
        if speed[0] <= kf:
            speed[0]=0
        if speed[1] <= kf:
            speed[1]=0
    
    player.x+=speed[0]
    player.y+=speed[1]"""

    cords=[0,0]
    speed_max=2
    speed_min=0.8
    global speed
    kf=1.02

    if keys[pygame.K_UP]:
        if speed < speed_max:
            speed*=kf
        cords[1]-=speed

    if keys[pygame.K_DOWN]:
        if speed < speed_max:
            speed*=kf
        cords[1]+=speed

        
    if keys[pygame.K_LEFT]:
        if speed < speed_max:
            speed*=kf
        cords[0]-=speed

        
    if keys[pygame.K_RIGHT]:
        if speed < speed_max:
            speed*=kf
        cords[0]+=speed
    
    if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and speed > speed_min:
        speed/=kf

    print(speed)

    return cords  