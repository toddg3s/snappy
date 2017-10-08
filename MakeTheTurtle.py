import pygame
import os

pygame.init()
image = pygame.image.load("snappy_turtle.png")
string = pygame.image.tostring(image,"RGBA")
with open("snappy_turtle.txt", "w") as text_file:
    text_file.write(string)
