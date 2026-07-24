import os 
#posição da janela:
os.environ['SDL_VIDEO_WINDOW_POS'] = "center"

import pygame
import pgzrun

from enemy import Enemy
from player import Player
from raycast import draw_walls, draw_enemy

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

TITLE = "Tentando Raycasting"
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

player = Player()

# inimigo
enemy = Enemy()
enemy_img = pygame.image.load('2_ano/python/pyzero/images/fantasma.png').convert_alpha()

# adicionar "estados p/ o inimigo"

def draw():
    screen.clear()
    screen.fill('lightblue')
    
    rays = draw_walls(screen, player)
    draw_enemy(screen, player, enemy, rays)
    # player.draw()

def update():
    player.update(keyboard)
    
    mouse_dx, mouse_dy = pygame.mouse.get_rel()
    player.angle += mouse_dx * 0.002
    
    enemy.timer += 1
    if enemy.timer >= 15:
        if enemy.get_enemy_fov(player):
            enemy.can_see_player(player)
        
    enemy.move_enemy(player)
    
    if enemy.collision_with_player(player):
        quit()

pgzrun.go()
