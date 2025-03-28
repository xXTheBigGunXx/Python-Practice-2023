import pygame
import pygame.mixer
import random
import time
import sys
pygame.init()

pygame.mixer.music.load("Desktop/projects/rocket_game_sound.mp3")
pygame.mixer.music.play(-1)

WIDTH, HEIGHT = 500, 750
PLAYER_MOVEMENT = 6
CH_WID, CH_HEI = 65, 180
MET_WID, MET_HEI = 100, 160
METEOR_SPEED = 5

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Window!!!")

background = pygame.transform.scale(pygame.image.load("back.jpeg"), (WIDTH, HEIGHT))
#player = pygame.transform.scale(pygame.image.load("rocket_pic.png"), (CH_WID, CH_HEI))
player = pygame.transform.scale(pygame.image.load("new_rocket.png"), (CH_WID, CH_HEI))
meteor = pygame.transform.scale(pygame.image.load("meteore.png"), (MET_WID, MET_HEI))
#meteor = pygame.transform.scale(pygame.movie.Movie("new_meteore_gif.gif"), (MET_WID, MET_HEI))

FONT = pygame.font.SysFont("helvetica", 80)
SCORE = pygame.font.SysFont("arias", 30)

Y = 0  # Initial x and y coordinates
SC = 0

clock = pygame.time.Clock()
position_list = []

PLAYER_X = WIDTH // 2 - CH_WID // 2
PLAYER_Y = HEIGHT // 2 - CH_HEI // 2

def drawer(time_passed):
    global Y, SC
    WIN.blit(background, (0, 0))
    WIN.blit(player, (PLAYER_X, PLAYER_Y))

    if time_passed > 5:
        SC += 6
    else:
        SC +=2

    time_score = SCORE.render(f"Score :{SC}" , 2, "Red")
    WIN.blit(time_score, (10, 10))
    for x in position_list:
        if Y > HEIGHT:
            Y = 0
            position()
            break
        WIN.blit(meteor, (x, Y - MET_HEI // 2))
    pygame.display.update()

def position():
    y_position = 0
    y_start = 0
    position_list.clear()
    for _ in range(2):
        y_position += int((WIDTH - MET_WID)/3)
        start_x = random.randint(y_start, y_position)
        position_list.append(start_x)
        y_start += int((WIDTH - MET_WID)/3)

def move_meteors():
    global Y
    Y += METEOR_SPEED

def check_collisions():
    player_rect = pygame.Rect(PLAYER_X, PLAYER_Y, CH_WID, CH_HEI)
    for x in position_list:
        meteor_rect = pygame.Rect(x, Y - MET_HEI // 2, MET_WID, MET_HEI)
        if player_rect.colliderect(meteor_rect):
            return True

def main():
    global PLAYER_X, PLAYER_Y, Y
    run = True
    start_time = time.time()
    position()
    
    while run:
        time_passed = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and PLAYER_X - PLAYER_MOVEMENT >= 0:
            PLAYER_X -= PLAYER_MOVEMENT
        if key[pygame.K_RIGHT] and PLAYER_X + PLAYER_MOVEMENT + 40 <= WIDTH:
            PLAYER_X += PLAYER_MOVEMENT
        if key[pygame.K_UP] and PLAYER_Y - PLAYER_MOVEMENT >= 0:
            PLAYER_Y -= PLAYER_MOVEMENT
        if key[pygame.K_DOWN] and PLAYER_Y + PLAYER_MOVEMENT + 80 <= HEIGHT:
            PLAYER_Y += PLAYER_MOVEMENT

        if check_collisions():
            lost_text = FONT.render("You have lost!!!", 2, "black")
            WIN.blit(lost_text, (WIDTH/2-lost_text.get_width()/2, HEIGHT/2-lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(1000)
            break

        move_meteors()

        check_collisions()

        drawer(time_passed)
        pygame.display.update()
        clock.tick(60)
    pygame.mixer.music.stop()
    pygame.quit()

main()
