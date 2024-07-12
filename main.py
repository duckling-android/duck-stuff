import pygame, sys
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Catch the flag")
clock = pygame.time.Clock()
running = True
game_state = "start_menu"
dt = 0
bg = pygame.image.load("background_grey.jpg")
lst = [0, 1, 2, 3]
lst2 = [0, 1, 2, 3]

player_pos = pygame.Vector2(screen.get_width() / 2 - 70, screen.get_height() / 2)
enemy_pos = pygame.Vector2(screen.get_width() / 2 + 70, screen.get_height() / 2)

blueflag_pos_x = 35
blueflag_pos_y = 650
blueflag_pos = (blueflag_pos_x, blueflag_pos_y)

redflag_pos = 1195, 650
redflag_pos_x = 1195
redflag_pos_y = 650

flag1 = False
flag2 = False

StartScreenIMG = pygame.image.load("start_screen.jpg")
BlueFlagIMG = pygame.image.load("blueflag.png")
RedFlagIMG = pygame.image.load("redflag.png")
FlagHoleIMG = pygame.image.load("flaghole.png")

rblue = pygame.Rect(blueflag_pos_x, blueflag_pos_y, 50, 50)
rred = pygame.Rect(redflag_pos_x, redflag_pos_y, 50, 50)
rredhole = pygame.Rect(35, 50, 60, 60)
rbluehole = pygame.Rect(1195, 50, 60, 60)

def show_start_screen():
    global game_state
    screen.fill("white")
    screen.blit(StartScreenIMG, (screen.get_width() / 2-400, screen.get_height() / 2-225))
    keys = pygame.key.get_pressed()
    font = pygame.font.SysFont("arial", 40)
    title_text = font.render("Catch the flag", True, (29, 141, 48))
    start_button = font.render("Press Space to Start", True, "black")
    screen.blit(title_text, (screen.get_width() / 2 - title_text.get_width() / 2, screen.get_height() / 4))
    screen.blit(start_button, (screen.get_width() / 2 - start_button.get_width() / 2, screen.get_height() / 2))
    if keys[pygame.K_SPACE]:
        game_state = "game"
    pygame.display.update()

def endscreenplayer():
    global game_state
    screen.fill("Blue")
    keys = pygame.key.get_pressed()
    font = pygame.font.SysFont("arial", 40)
    wintext1 = font.render("Blue player wins", True, "Black")
    ripbozo = font.render("Better luck next time", True, "Black")
    restart = font.render("Press r to restart", True, "Black")
    screen.blit(wintext1, (screen.get_width() / 2 - wintext1.get_width() / 2, screen.get_height() / 4))
    screen.blit(ripbozo, (screen.get_width() / 2 - ripbozo.get_width() / 2, screen.get_height() / 2))
    screen.blit(restart, (screen.get_width() / 2 - restart.get_width() / 2, screen.get_height() / 1.5))
    if keys[pygame.K_r]:
        game_state = "start_menu"
    pygame.display.update()

def endscreenenemy():
    global game_state
    screen.fill("orange")
    keys = pygame.key.get_pressed()
    font = pygame.font.SysFont("arial", 40)
    wintext1 = font.render("Orange player wins", True, "Black")
    ripbozo = font.render("Better luck next time", True, "Black")
    restart = font.render("Press r to restart", True, "Black")
    screen.blit(wintext1, (screen.get_width() / 2 - wintext1.get_width() / 2, screen.get_height() / 4))
    screen.blit(ripbozo, (screen.get_width() / 2 - ripbozo.get_width() / 2, screen.get_height() / 2))
    screen.blit(restart, (screen.get_width() / 2 - restart.get_width() / 2, screen.get_height() / 1.5))
    if keys[pygame.K_r]:
        game_state = "start_menu"
    pygame.display.update()




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
        reflected_x = screen.get_width() - (x + w)
        reflected_rect = (reflected_x, y, w, h)
        pygame.draw.rect(screen, "black", reflected_rect)

def collisions():
    obstacles = [
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
        x, y, w, h = r
    
    r1 = pygame.Rect(player_pos.x - 16, player_pos.y - 16, 32, 32)
    return r1.collidelist(obstacles)

def collisionblue():
    r2 = pygame.Rect(enemy_pos.x - 16, enemy_pos.y - 16, 32, 32)
    return r2.colliderect(rblue)

def collisionred():
    r1 = pygame.Rect(player_pos.x - 15, player_pos.y - 15, 30, 30)
    return r1.colliderect(rred)

def collisionblueducklings():
    bluerectangles = [
        pygame.Rect(enemy_pos.x - 15, enemy_pos.y - 15, 30, 30)
    ]
    r1 = pygame.Rect(player_pos.x - 15, player_pos.y - 15, 30, 30)
    return r1.collidelist(bluerectangles)

def collisionredducklings():
    redrectangles = [
        pygame.Rect(player_pos.x - 16, player_pos.y - 16, 32, 32)
    ]
    r2 = pygame.Rect(enemy_pos.x - 16, enemy_pos.y - 16, 32, 32)
    return r2.collidelist(redrectangles)

def collisionbluehole():
    r2 = pygame.Rect(enemy_pos.x - 16, enemy_pos.y - 16, 32, 32)
    return r2.colliderect(rbluehole)

def collisionredhole():
    r1 = pygame.Rect(player_pos.x - 15, player_pos.y - 15, 30, 30)
    return r1.colliderect(rredhole)

def collisionEnemy():
    obstacles = [
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
        x, y, w, h = r

    r2 = pygame.Rect(enemy_pos.x - 16, enemy_pos.y - 16, 32, 32)
    return r2.collidelist(obstacles)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if game_state == "start_menu":
        show_start_screen()
    elif game_state == "game":
        keys = pygame.key.get_pressed()

        # fill the screen with a color to wipe away anything from last frame
        screen.blit(bg, (0, 0))

        pygame.draw.circle(screen, "blue", player_pos, 15)
        pygame.draw.circle(screen, "orange", enemy_pos, 15)
        screen.blit(BlueFlagIMG, (blueflag_pos))
        screen.blit(RedFlagIMG, (redflag_pos))
        screen.blit(FlagHoleIMG, (35, 50))
        screen.blit(FlagHoleIMG, (1195, 50))

        draw_rect()

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
        else:
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
        else:
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

        if collisionblueducklings() != -1 and flag1:
            blueflag_pos = 35, 650

        if collisionblue():
            flag1 = True
            blueflag_pos = enemy_pos

        if collisionredducklings() != -1 and flag2:
            redflag_pos = 1195, 650

        if collisionred():
            flag2 = True
            redflag_pos = player_pos

        if collisionbluehole() and flag1:
            game_state ="win"

        if collisionredhole() and flag2:
            game_state ="win"


        if player_pos.x >= 1265:
            player_pos.x = 1265
        if player_pos.x <= 15:
            player_pos.x = 15
        if player_pos.y >= 705:
            player_pos.y = 705
        if player_pos.y <= 15:
            player_pos.y = 15

        if enemy_pos.x >= 1265:
            enemy_pos.x = 1265
        if enemy_pos.x <= 15:
            enemy_pos.x = 15
        if enemy_pos.y >= 705:
            enemy_pos.y = 705
        if enemy_pos.y <= 15:
            enemy_pos.y = 15


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
 
    elif game_state == "win":
        if flag1:
            endscreenenemy()
        if flag2:
            endscreenplayer()
pygame.quit()
sys.exit()
