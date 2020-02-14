import requests
import pygame
import os

x = ''
y = ''
scale = ''
a = requests.get(f'http://static-maps.yandex.ru/1.x/?ll={x},{y}&spn={scale},25&l=sat')

map = 'map.png'
with open(map, "wb") as file:
    file.write(a.content)

pygame.init()
g = pygame.image.load(map)
screen = pygame.display.set_mode((600, 400))
screen.blit(g, (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map)
