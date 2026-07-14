import os
#posição da janela:
os.environ['SDL_VIDEO_WINDOW_POS'] = "center"

import pygame
import pgzrun
from pgzero.rect import Rect

import math
from settings import FOV, NUM_RAYS, DIST_PLANO
from world import random_pos, WIDTH, HEIGHT, TILE_SIZE, has_wall
from enemy import Enemy
from player import Player

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

TITLE = "Tentando Raycasting"

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

PLAYER_SPEED = 1.5
player = Player()

player.pos = TILE_SIZE*2, TILE_SIZE*2
if has_wall(player.x, player.y):
    player.pos = (TILE_SIZE*2) - 2, (TILE_SIZE*2) - 2

# inimigo
enemy = Enemy()
x, y = random_pos(x, y)
enemy_img = pygame.image.load('2_ano/python/pyzero/images/fantasma.png').convert_alpha()
enemy_timer = 0

def draw():
    screen.clear()
    screen.fill('lightblue')
    # lançar os ângulos até que player.angle tenha FOV positivo:
    rays = []
    for ray in range(NUM_RAYS):
        angle = player.angle - FOV/2 + ray * (FOV / (NUM_RAYS-1)) # isolar NUM_RAYS - 1 !!
        # o ângulo do player quando aplicada a fórmula a partir do campo de visão (FOV) direciona para onde os vetores serão desenhados
        depth, hit_x, hit_y, side = cast_ray(angle) # onde o vetor colide com a parede
        rays.append(depth)
        #screen.draw.line(player.pos, (hit_x, hit_y), (0, 255, 0)) # desta maneira os vetores representam a h da parede na projeção.
    
    column_width = WIDTH / NUM_RAYS # a largura da coluna (um vaetor/raio/linha) baseada em NUM_RAYS, ou seja 200 raios.
    '''a divisão por WIDTH diz:
    se WIDTH = 1000 --> 1000 / 200 = 5, logo 
    raio 0 -> coluna 0
    raio 1 -> coluna 5
    raio 2 -> coluna 10'''
    screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT), (120,170,255))
    screen.draw.filled_rect(Rect(0, HEIGHT//2, WIDTH, HEIGHT//2), (80,80,80))
    
    for alt, depth in enumerate(rays):
        h = (TILE_SIZE * DIST_PLANO)/depth
        h = min(HEIGHT, h)
        x = alt*column_width
        y = HEIGHT/2 - h/2
        rect_screen = Rect(x, y, column_width+2, h)
        screen.draw.filled_rect(rect_screen, (120,120,255))

    dx = enemy.x - player.x
    dy = enemy.y - player.y

    en_dist = math.hypot(dx, dy)
    angle = math.atan2(dy, dx)
    delta = angle - player.angle

    while delta > math.pi:
        delta -= 2*math.pi
    while delta < -math.pi:
        delta += 2*math.pi

    if abs(delta) < FOV/2:
        return
    
    en_dist *= math.cos(delta)
    if en_dist <= 1:
        en_dist = 1
    en_h = TILE_SIZE * DIST_PLANO / en_dist
    en_w = h
    screen_x = WIDTH/2 + math.tan(delta) * DIST_PLANO
    screen_y = HEIGHT/2 - en_h/2
    left = int((screen_x - en_w/2) / column_width)
    right = int((screen_x + en_w/2) / column_width)
    
    ray = int(screen_x / column_width)
    sprite = pygame.transform.scale(enemy_img, (int(en_w), int(en_h)))
    for ray in range(left, right + 1):
            if 0 <= ray < NUM_RAYS:
                if en_dist < rays[ray]:
                    tex_x = int((ray-left) / (right-left+1) * sprite.get_width())
                    column = sprite.subsurface((tex_x, 0, 1, sprite.get_height()))
                    
                    x = ray * column_width
                    screen.surface.blit(column, (x, screen_y))

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
    
    enemy_timer += 1

    if enemy_timer >= 15:
        if get_enemy_fov(enemy, player):
            if can_see_player(enemy, player):
                move_enemy()

    enemy_timer = 0
    
    # testa movimento em Y
    if not (has_wall(player.x-dx, player_posy-dy) or has_wall(player.x+dx, player_posy-dy) or
    has_wall(player.x+dx, player_posy+dy) or has_wall(player.x-dx, player_posy+dy)):
        player.y = player_posy
    # movimento em X
    if not (has_wall(player_posx-dx, player.y-dy) or has_wall(player_posx+dx, player.y-dy) or
    has_wall(player_posx+dx, player.y+dy) or has_wall(player_posx-dx, player.y+dy)):
        player.x = player_posx

pgzrun.go()