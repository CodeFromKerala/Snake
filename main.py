'''
Snake Game made by CodeFromKerala
Python V3.10.6
Pygame V2.1.2 - SDL 2.0.18
'''

# Importing Needed Libraries
import pygame
import random

# Screen Setup
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Frames Per Second
FPS = 5

# Head of Snake Class
class Head(pygame.Rect):
    def __init__(self):
        super().__init__(10, 10, 10, 10)
        self.image = pygame.image.load('./gfx/head.png')
        self.direction = "South"
    def update(self):
        if self.direction == "South":
            self.y += 10
        if self.direction == "North":
            self.y -= 10
        if self.direction == "East":
            self.x += 10
        if self.direction == "West":
            self.x -= 10
        display.blit(self.image, self)

# Segments of Snake Class
class Segment(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(10, 10, x, y)
        self.image = pygame.image.load("./gfx/head.png")
    def update(self):
        display.blit(self.image, self)

class Food(pygame.Rect):
    def __init__(self):
        super().__init__(10, 10, random.randint(1, 450), random.randint(1, 450))

# Main Game Loop
def main():
    run = True
    head = Head()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    head.direction = "North"
                if event.key == pygame.K_DOWN:
                    head.direction = "South"
                if event.key == pygame.K_RIGHT:
                    head.direction = "East"
                if event.key == pygame.K_LEFT:
                    head.direction = "West"
        display.fill((255, 255, 255))
        head.update()
        pygame.display.update()
    pygame.quit()

# Checking if file is not imported
if __name__ == "__main__":
    main()