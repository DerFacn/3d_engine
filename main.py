import pygame
import math
from settings import *
from map import world_map
from player import Player
from ray_casting import ray_casting
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(BLACK)

    ray_casting(screen, player.pos, player.angle)
    player.movement()
    pygame.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 12)
    
    for x, y in world_map:
        pygame.draw.rect(screen, GREY, (x, y, TILE, TILE))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
