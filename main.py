import pygame 
import time

# screen size 
WINDOW_W = 1000
WINDOW_H = 600
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tetris")

bk_image = pygame.image.load("tet.jpg")

play = True
while  play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play=False
         
    screen.blit(bk_image,(0,0))
    pygame.display.flip()



pygame.quit()
