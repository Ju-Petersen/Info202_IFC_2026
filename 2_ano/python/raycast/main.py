import os
#posição da janela:
os.environ['SDL_VIDEO_WINDOW_POS'] = "center"

import pygame
import pgzrun
import path
import math

from enemy import Enemy
from player import Player
from settings import TILE, TILE_SIZE, ROWS, COLS, FOV, RES
from raycast import cast_ray, draw_walls
from world import world_map, has_wall, random_pos

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

TITLE = "Tentando Raycasting"
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

WIDTH = len(world_map[0]) * TILE_SIZE
HEIGHT = len(world_map) * TILE_SIZE
NUM_RAYS = WIDTH // RES # raios (vetores) que serão 'desenhados' a partir do movimento do player#0 são espaçoes vazios e 1 são as
DIST_PLANO = WIDTH / (2 * math.tan(FOV/2))

player = Player()

# inimigo
enemy = Enemy()
enemy_img = pygame.image.load('2_ano/python/pyzero/images/fantasma.png').convert_alpha()

# adicionar "estados p/ o inimigo"

def draw():
    screen.clear()
    screen.fill('lightblue')
    
    rays = draw_walls(screen, player)
    draw_walls(screen, rays)
    player.draw()
    enemy.draw()

def update():
    player.update(keyboard)
    enemy.update(player)
    # testa movimento em Y
    if not (has_wall(player.sprite.x-dx, player_posy-dy) or has_wall(player.sprite.x+dx, player_posy-dy) or
    has_wall(player.sprite.x+dx, player_posy+dy) or has_wall(player.sprite.x-dx, player_posy+dy)):
        player.sprite.y = player_posy
    
    # movimento em X
    if not (has_wall(player_posx-dx, player.sprite.y-dy) or has_wall(player_posx+dx, player.sprite.y-dy) or
    has_wall(player_posx+dx, player.sprite.y+dy) or has_wall(player_posx-dx, player.sprite.y+dy)):
        player.sprite.x = player_posx

pgzrun.go()
