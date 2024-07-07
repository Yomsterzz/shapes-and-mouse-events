import pygame
import random
pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill("blue")
pygame.display.update()

class Circle():
    def __init__(self, radius, color, pos, width):
        self.radius = radius
        self.color = color
        self.pos = pos
        self.width = width
        self.circle_surface = screen
    
    def display_circle(self):
        self.draw_circle = pygame.draw.circle(self.circle_surface, self.color, self.pos, self.radius, self.width)

    def increase_circle(self, radius):
        self.radius += radius
        self.draw_circle = pygame.draw.circle(self.circle_surface, self.color, self.pos, self.radius, self.width)
    
circle1 = Circle(20, "green", (50,50), 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle1.display_circle()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            circle1.increase_circle(5)
            pygame.display.update()
