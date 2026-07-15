import os
#posição da janela:
os.environ['SDL_VIDEO_WINDOW_POS'] = "center"

import pygame
import pgzrun
import math

from settings import FOV, RES
from enemy import Enemy
from player import Player
from world import has_wall, TILE_SIZE

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

TITLE = "Tentando Raycasting"

player = Player()

if has_wall(player.sprite.x, player.sprite.y):
    player.sprite.pos = (TILE_SIZE*2) - 2, (TILE_SIZE*2) - 2

# inimigo
enemy = Enemy()
enemy_img = pygame.image.load('2_ano/python/pyzero/images/fantasma.png').convert_alpha()

# adicionar "estados p/ o inimigo"

def draw():
    player.draw()
    #enemy.draw()

def update():
    global enemy_timer
    mouse_dx, mouse_dy = pygame.mouse.get_rel()
    player.angle += mouse_dx * 0.002
    
    # enemy_timer += 1

    # if enemy_timer >= 15:
    #     if get_enemy_fov(player):
    #         if can_see_player(enemy, player):
    #             move_enemy()

    # enemy_timer = 0

pgzrun.go()
