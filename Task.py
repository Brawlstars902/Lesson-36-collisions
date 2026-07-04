import pygame
import random
import sys

pygame.init()

colours = ['red','green','blue','yellow','pink','brown']
screen = pygame.display.set_mode((600,360))
background = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()

sprite_1_y_status = 'going down'
sprite_1_x_status = 'going left'
sprite_1 = pygame.Surface((50,50))
sprite_1.fill('red')
sprite_1_rect = sprite_1.get_rect(topleft = (random.randint(0,550),random.randint(0,310)))

sprite_2_y_status = 'going up'
sprite_2_x_status = 'going right'
sprite_2 = pygame.Surface((50,50))
sprite_2.fill('green')
sprite_2_rect = sprite_2.get_rect(topleft = (random.randint(0,550),random.randint(0,310)))

while True:

    screen.blit(background,(0,0))
    screen.blit(sprite_1,sprite_1_rect)
    screen.blit(sprite_2,sprite_2_rect)

# sprite_1 x
    if sprite_1_rect.left <= 0:
        sprite_1_rect.x += 5
        sprite_1_x_status = 'going right'
    elif sprite_1_rect.right >= 600:
        sprite_1_rect.x -= 5
        sprite_1_x_status = 'going left'
    else:
        if sprite_1_x_status == 'going left':
            sprite_1_rect.x -= 5
        if sprite_1_x_status == 'going right':
            sprite_1_rect.x += 5

# sprite_1 y
    if sprite_1_rect.top <= 0:
        sprite_1_rect.y += 5
        sprite_1_y_status = 'going down'
    elif sprite_1_rect.bottom >= 360:
        sprite_1_rect.y -= 5
        sprite_1_y_status = 'going up'
    else:
        if sprite_1_y_status == 'going down':
            sprite_1_rect.y += 5
        if sprite_1_y_status == 'going up':
            sprite_1_rect.y -= 5

# sprite_2 x
    if sprite_2_rect.left <= 0:
        sprite_2_rect.x += 5
        sprite_2_x_status = 'going right'
    elif sprite_2_rect.right >= 600:
        sprite_2_rect.x -= 5
        sprite_2_x_status = 'going left'
    else:
        if sprite_2_x_status == 'going left':
            sprite_2_rect.x -= 5
        if sprite_2_x_status == 'going right':
            sprite_2_rect.x += 5

# sprite_2 y
    if sprite_2_rect.top <= 0:
        sprite_2_rect.y += 5
        sprite_2_y_status = 'going down'
    elif sprite_2_rect.bottom >= 360:
        sprite_2_rect.y -= 5
        sprite_2_y_status = 'going up'
    else:
        if sprite_2_y_status == 'going down':
            sprite_2_rect.y += 5
        if sprite_2_y_status == 'going up':
            sprite_2_rect.y -= 5

    if sprite_1_rect.colliderect(sprite_2_rect):
        sprite_1.fill(random.choice(colours))
        sprite_2.fill(random.choice(colours))
        
        if sprite_1_x_status == 'going left':
            sprite_1_x_status = 'going right'
        else:
            sprite_1_x_status = 'going left'

        if sprite_1_y_status == 'going down':
            sprite_1_y_status = 'going up'
        else:
            sprite_1_y_status = 'going down'


        if sprite_2_x_status == 'going left':
            sprite_2_x_status = 'going right'
        else:
            sprite_2_x_status = 'going left'

        if sprite_2_y_status == 'going down':
            sprite_2_y_status = 'going up'
        else:
            sprite_2_y_status = 'going down'


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            pygame.quit()      

    clock.tick(60)  

    pygame.display.update()