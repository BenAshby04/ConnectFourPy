import pygame
from sys import exit

screen = pygame.display.set_mode((800,600))

BLACK = (0,0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
            
    screen.fill(BLACK)
    
    pygame.display.update()