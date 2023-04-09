import pygame
import math
from settings import *
from map import world_map
from player import Player
from ray_casting import ray_casting
from drawing import Drawing
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(BLACK)
    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)

    player.movement()
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
