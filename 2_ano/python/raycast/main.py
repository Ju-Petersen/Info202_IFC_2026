import os
#posição da janela:
os.environ['SDL_VIDEO_WINDOW_POS'] = "center"

import pygame
import pgzrun
import path

from enemy import Enemy
from player import Player
import settings
import raycaster
import world

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

WIDTH = len(world_map[0]) * TILE_SIZE
HEIGHT = len(world_map) * TILE_SIZE

NUM_RAYS = WIDTH // RES # raios (vetores) que serão 'desenhados' a partir do movimento do player#0 são espaçoes vazios e 1 são as
DIST_PLANO = WIDTH / (2 * math.tan(FOV/2))

player.pos = TILE_SIZE*2, TILE_SIZE*2
if has_wall(player.x, player.y):
    player.pos = (TILE_SIZE*2) - 2, (TILE_SIZE*2) - 2

# inimigo
x, y = random_pos()
enemy = Enemy()
enemy_img = pygame.image.load('2_ano/python/pyzero/images/fantasma.png').convert_alpha()

# adicionar "estados p/ o inimigo"

def draw():
    player.draw()
    enemy.draw()

def update():
    global enemy_timer, PLAYER_SPEED

    if keyboard.lshift:
        PLAYER_SPEED = 3
    else:
        PLAYER_SPEED = 1.5
    
    cos_a = math.cos(player.angle)
    sin_a = math.sin(player.angle)
    dx = player.width / 2
    dy = player.height / 2
    
    player_posx = player.x # posição futura
    player_posy = player.y # posição futura
        
    if keyboard.w:
        player_posy += sin_a * PLAYER_SPEED #anda em x ou y de acordo com a direção que o player "olha"
        player_posx += cos_a * PLAYER_SPEED
    if keyboard.s:
        player_posy -= sin_a * PLAYER_SPEED
        player_posx -= cos_a * PLAYER_SPEED
    if keyboard.d:
        player_posx -= sin_a * PLAYER_SPEED
        player_posy += cos_a * PLAYER_SPEED
    if keyboard.a:
        player_posx += sin_a * PLAYER_SPEED
        player_posy -= cos_a * PLAYER_SPEED
    
    mouse_dx, mouse_dy = pygame.mouse.get_rel()
    player.angle += mouse_dx * 0.002
    
    # enemy_timer += 1

    # if enemy_timer >= 15:
    #     if get_enemy_fov(enemy, player):
    #         if can_see_player(enemy, player):
    #             move_enemy()

    # enemy_timer = 0
    
    # testa movimento em Y
    if not (has_wall(player.x-dx, player_posy-dy) or has_wall(player.x+dx, player_posy-dy) or
    has_wall(player.x+dx, player_posy+dy) or has_wall(player.x-dx, player_posy+dy)):
        player.y = player_posy
    
    # movimento em X
    if not (has_wall(player_posx-dx, player.y-dy) or has_wall(player_posx+dx, player.y-dy) or
    has_wall(player_posx+dx, player.y+dy) or has_wall(player_posx-dx, player.y+dy)):
        player.x = player_posx

pgzrun.go()
