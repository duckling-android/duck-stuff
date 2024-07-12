# Example file showing a circle moving on screen
import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
lst = [0, 1, 2, 3]
lst2 = [0, 1, 2, 3]

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

enemy_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

flag_pos = pygame.Vector2(screen.get_width() /2, screen.get_height() / 2)


def draw_rect():
    rectangles = [
        (105, 285, 20, 275),
        (200, 505, 20, 215),
        (295, 285, 20, 235),
        (295, 600, 20, 70),
        (385, 550, 20, 170),
        (0, 285, 220, 20)
    ]
    
    for r in rectangles:
        pygame.draw.rect(screen, "black", r)
        x, y, w, h = r
        reflected_x = screen.get_width()  - (x + w)
        reflected_rect = (reflected_x, y, w, h)
        pygame.draw.rect(screen, "black", reflected_rect)

def collisions():
    obstacles=[
        pygame.Rect(105, 285, 20, 275),
        pygame.Rect(200, 505, 20, 215),
        pygame.Rect(295, 285, 20, 235),
        pygame.Rect(295, 600, 20, 70),
        pygame.Rect(385, 550, 20, 170),
        pygame.Rect(0, 285, 220, 20),
        pygame.Rect(1155, 285, 20, 275),
        pygame.Rect(1060, 505, 20, 215),
        pygame.Rect(965, 285, 20, 235),
        pygame.Rect(965, -1600, 20, 70),
        pygame.Rect(875, 550, 20, 170),
        pygame.Rect(1060, 285, 220, 20)
    ]

    for r in obstacles:
        pygame.draw.rect(screen, "black", r)
        x, y, w, h =r
        

        #if x-15<=player_pos.x<x+w+10 and y-15<=player_pos.y<=y+h+15:
            #player_pos.x = x-15
        #if x-10<player_pos.x<=x+w+16 and y-15<=player_pos.y<=y+h+15:
            #player_pos.x = x+w+16
    r1= pygame.Rect(player_pos.x-16, player_pos.y-16, 32, 32)
    return r1.collidelist(obstacles)

def collisionEnemy():
    obstacles=[
        pygame.Rect(105, 285, 20, 275),
        pygame.Rect(200, 505, 20, 215),
        pygame.Rect(295, 285, 20, 235),
        pygame.Rect(295, 600, 20, 70),
        pygame.Rect(385, 550, 20, 170),
        pygame.Rect(0, 285, 220, 20),
        pygame.Rect(1155, 285, 20, 275),
        pygame.Rect(1060, 505, 20, 215),
        pygame.Rect(965, 285, 20, 235),
        pygame.Rect(965, -1600, 20, 70),
        pygame.Rect(875, 550, 20, 170),
        pygame.Rect(1060, 285, 220, 20)
    ]

    for r in obstacles:
        pygame.draw.rect(screen, "black", r)
        x, y, w, h =r
        

        #if x-15<=player_pos.x<x+w+10 and y-15<=player_pos.y<=y+h+15:
            #player_pos.x = x-15
        #if x-10<player_pos.x<=x+w+16 and y-15<=player_pos.y<=y+h+15:
            #player_pos.x = x+w+16
    r2= pygame.Rect(enemy_pos.x-16, enemy_pos.y-16, 32, 32)
    return r2.collidelist(obstacles)
        



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cyan")

    pygame.draw.circle(screen, "white", player_pos, 15)
    pygame.draw.circle(screen, "orange", enemy_pos, 15)

    draw_rect()
   
    
    keys = pygame.key.get_pressed()

    if collisions() == -1:
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
            lst.append(0)
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
            lst.append(1)
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
            lst.append(2)
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
            lst.append(3)
    else :
        if lst[-1] == 0:
            player_pos.y += 300 * dt
        if lst[-1] == 1:
            player_pos.y -= 300 * dt
        if lst[-1] == 2:
            player_pos.x += 300 * dt
        if lst[-1] == 3:
            player_pos.x -= 300 * dt
        if len(lst) > 3:
            lst.pop(0)

        

    if collisionEnemy() == -1:
        if keys[pygame.K_UP]:
            enemy_pos.y -= 300 * dt
            lst2.append(0)
        if keys[pygame.K_DOWN]:
            enemy_pos.y += 300 * dt
            lst2.append(1)
        if keys[pygame.K_LEFT]:
            enemy_pos.x -= 300 * dt
            lst2.append(2)
        if keys[pygame.K_RIGHT]:
            enemy_pos.x += 300 * dt
            lst2.append(3)
    else :
        if lst2[-1] == 0:
            enemy_pos.y += 305 * dt
        if lst2[-1] == 1:
            enemy_pos.y -= 305 * dt
        if lst2[-1] == 2:
            enemy_pos.x += 305 * dt
        if lst2[-1] == 3:
            enemy_pos.x -= 305 * dt
        if len(lst2) > 3:
            lst2.pop(0)




    if player_pos.x >=1265:
        player_pos.x=1265
    if player_pos.x <=15:
        player_pos.x=15
    if player_pos.y >= 705:
        player_pos.y=705
    if player_pos.y <=15:
        player_pos.y=15

    if enemy_pos.x >=1265:
        enemy_pos.x=1265
    if enemy_pos.x <=15:
        enemy_pos.x=15
    if enemy_pos.y >= 705:
        enemy_pos.y=705
    if enemy_pos.y <=15:
        enemy_pos.y=15
    


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
