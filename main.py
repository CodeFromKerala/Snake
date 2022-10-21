'''
Snake Game made by CodeFromKerala
Python V3.10.6
Pygame V2.1.2 - SDL 2.0.18
'''

import pygame

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

FPS = 1

def main():
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

if __name__ == "__main__":
    main()