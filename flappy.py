import pygame

WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

back_img = pygame.transform.scale(pygame.image.load("flappybackground.png"), (WIDTH, HEIGHT))

def body():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(back_img, (0, 0))
        pygame.display.update()

    pygame.quit()

body()
