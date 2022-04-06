import pygame
import time

# screen size
WINDOW_W = 600
WINDOW_H = 600
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tetris")

bk_image = pygame.image.load("tet.jpg")
shape_g = pygame.image.load("shape.G..png")
shape = pygame.image.load("shape.G.png")
shape_i = pygame.image.load("shape.I.png")
shape_les = pygame.image.load("shape.les.png")
shape_t = pygame.image.load("shape.T.png")

# Initialing Color
color = (255, 100, 200)

# Drawing Rectangle

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    screen.blit(bk_image, (0, 0))
    screen.blit(shape_g, (WINDOW_W/2+50, 0))
    screen.blit(shape_i, (WINDOW_W/2-80, 0))
    screen.blit(shape_les, (WINDOW_W/2-150, 0))
    screen.blit(shape_t, (WINDOW_W/2+100, 0))
    screen.blit(shape, (WINDOW_W/2+100, 0))

    pygame.display.flip()


pygame.quit()
