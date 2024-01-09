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
        relpos[0] = (player.height + current_object.height) / (player.width + current_object.width)
        relpos[1]= (player.width + current_object.width) / (player.height + current_object.height)
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

def move(player):
    speed = 1 
    cords = [0, 0] # x,y
    
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            player.y-=speed
            return cords
        elif event.type == pygame.KEYDOWN:
            player.y+=speed
            return cords
        elif event.type == pygame.K_LEFT:
            player.x-=speed
            return cords
        elif event.type == pygame.K_RIGHT:
            player.x+=speed
            return cords