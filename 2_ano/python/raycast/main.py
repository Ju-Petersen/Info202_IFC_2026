import os 
#posição da janela:
os.environ['SDL_VIDEO_WINDOW_POS'] = "center"

import pygame
import pgzrun
import math

from enemy import Enemy
from player import Player
from pathfind import bfs
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
    
    draw_walls(screen, player)
    player.draw()
    enemy.draw()

def update():
    global enemy_timer
    player.update(keyboard)
    
    mouse_dx, mouse_dy = pygame.mouse.get_rel()
    player.angle += mouse_dx * 0.002
    
    # enemy_timer += 1

    # if enemy_timer >= 15:
    #     if get_enemy_fov(enemy, player):
    #         if can_see_player(enemy, player):
    #             move_enemy()

    # enemy_timer = 0

pgzrun.go()
