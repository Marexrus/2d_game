import pygame
#Тут будут функции для движения и все что с этим связанно

def collide(hero, objects):
    # print(hero.x)
    Num_of_collisions = hero.collidelist(objects)
    side = ''
    if Num_of_collisions >= 0:
        current_object = objects[Num_of_collisions]
        plane1 = False
        plane2 = False
        relpos = [current_object.x - hero.x, current_object.y - hero.y]
        relpos[0] = (hero.height + current_object.height) / (hero.width + current_object.width)
        relpos[1]= (hero.width + current_object.width) / (hero.height + current_object.height)
        if relpos[1] < relpos[0]:
            plane1 = False
        else:
            plane1 = True
        if relpos[1] < -relpos[0]:
            plane2 = False
        else:
            plane2 = True

        if plane1 and plane2:
            hero.y = current_object.y - hero.height
            side = 'up'

        if plane1 and not plane2:
            hero.x = current_object.x + current_object.width
            side = 'right'

        if not plane1 and plane2:
            hero.x = current_object.x - hero.width
            side = 'left'

        if not plane1 and not plane2:
            hero.y = current_object.y + current_object.height
            side = 'down'
        objects[Num_of_collisions] = current_object

        return side
    return None

def move():
    speed = 1 
    cords = [0, 0] # x,y
    
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            cords[1]-=speed
            return cords
        elif event.type == pygame.KEYDOWN:
            cords[1]+=speed
            return cords
        elif event.type == pygame.K_LEFT:
            cords[0]-=speed
            return cords
        elif event.type == pygame.K_RIGHT:
            cords[0]+=speed
            return cords