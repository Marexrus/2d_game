import pygame
#Тут будут функции для движения и все что с этим связанно

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

def move(keys):
    speed_min = 0
    speed_max = 1
    speed_current = 0.5 
    cords = [0, 0] # x,y

    if keys[pygame.K_UP]:
        if speed_current < speed_max and speed_current > speed_min:
            speed_current*=1.2 
            cords[1]-=speed_current
    elif speed_current < speed_max and speed_current > speed_min:
        speed_current/=1.2 
        cords[1]+=speed_current

    if keys[pygame.K_DOWN]:
        if speed_current < speed_max and speed_current > speed_min:
            speed_current*=1.2 
            cords[1]+=speed_current
    elif speed_current < speed_max and speed_current > speed_min:
        speed_current/=1.2 
        cords[1]-=speed_current
        
    if keys[pygame.K_LEFT]:
        if speed_current < speed_max and speed_current > speed_min:
            speed_current*=1.2 
            cords[1]-=speed_current
    elif speed_current < speed_max and speed_current > speed_min:
        speed_current/=1.2 
        cords[1]+=speed_current
    if keys[pygame.K_RIGHT]:
        if speed_current < speed_max and speed_current > speed_min:
            speed_current*=1.2 
            cords[1]+=speed_current
    elif speed_current < speed_max and speed_current > speed_min:
        speed_current/=1.2 
        cords[1]-=speed_current
 
    return cords    