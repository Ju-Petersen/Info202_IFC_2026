import pygame
import math
from pathfind import bfs
from world import random_pos
from settings import TILE_SIZE, TILE_SIZE, COLS, ROWS
from pgzero.actor import Actor
from collections import deque

class Enemy:
    def __init__(self):
        self.sprite = Actor('fantasma.png', anchor=('center', 'center'))
        self.speed = 5.0
        self.angle = 0
        self.timer = 0
        self.sprite.pos = random_pos()

    # Implementar FOV e raycast do inimigo (possibilita o inimigo "parar de ver" o player):
    def can_see_player(self, player):
        #colocar o DDA
        dx_enemy = player.sprite.x - self.sprite.x # encontrar o vetor entre inimigo e player
        dy_enemy = player.sprite.y - self.sprite.y
        dist_to_player = math.hypot(dy_enemy, dx_enemy) # direção do inimigo (onde ele "olha") -------------------
        en_angle = math.atan2(dy_enemy, dx_enemy)
        
        ray_y = math.sin(en_angle)
        ray_x = math.cos(en_angle)
        # a partir das coordenadas do raio, as coordenadas 
        # em pixel do player serão contadas a partir de TILE_SIZE
        y = self.sprite.y / TILE_SIZE
        x = self.sprite.x / TILE_SIZE # dividir por TILE_SIZE mostra em qual coluna o player está
        # posição atual e futura:
        map_y = int(y)
        map_x = int(x)
        # calcular delta de "depth" para mostrar quanto o vetor precisa 
        # percorrer até chegar a próxima célula
        if ray_y == 0:
            delta_depth_y = 1e30
        else:
            delta_depth_y  = abs(1/ray_y)
        if ray_x == 0: # vai verificar o quanto precisa andar até chegar a próxima coluna
            delta_depth_x = 1e30 
            # considerar o delta da distância x e y por conta dos ângulos, 
            # ou seja, conforme um ângulo é mais reto ou diagonal leva mais 
            # tempo p/ o vetor atravessá-lo
        else:
            delta_depth_x  = abs(1/ray_x)
        # sentido do vetor:
        if ray_x < 0:
            step_x = -1
            # a distância inicial em "delta_depth" é fixa, porém a direção entre cada linha é variável:
            side_depth_x = (x - map_x)*delta_depth_x 
        else:
            step_x = 1
            side_depth_x = (map_x + 1-x)*delta_depth_x
        if ray_y < 0:
            step_y = -1
            side_depth_y = (y - map_y)*delta_depth_y
        else:
            step_y = 1
            side_depth_y = (map_y + 1-y)*delta_depth_y
        
        while True:
            if side_depth_x < side_depth_y:
                wall_depth = side_depth_x
                side_depth_x += delta_depth_x
                map_x += step_x
            else:
                wall_depth = side_depth_y
                side_depth_y += delta_depth_y
                map_y += step_y
            
            if not (0 <= map_x < COLS and 0 <= map_y < ROWS):
                return False
            if world_map[map_y][map_x]:
                return False
            
            en_depth = wall_depth * TILE_SIZE
            if en_depth >= dist_to_player:
                return True

    def get_enemy_fov(self, player): # ângulo do inimigo
        dx_en = player.sprite.x - self.sprite.x
        dy_en = player.sprite.y - self.sprite.y

        angle_to_player = math.atan2(dy_en, dx_en) # direção do inimigo (onde ele "olha") -------------------

        delta_enemy = angle_to_player - self.angle 
        # calcular delta entre o ângulo do inimigo e seu ângulo em relação ao player, 
        # para mostrar quanto o vetor precisa
        # percorrer até chegar a próxima célula

        while delta_enemy > math.pi: 
            # usando o ângulo qual o inimigo olha, e o quanto ele tem que "girar" 
            # para que o player estja em seu fov. Então se os ângulos resultam em 0°, o player está no fov do inimigo
            delta_enemy -= 2 * math.pi

        while delta_enemy < -math.pi:
            delta_enemy += 2 * math.pi

        return abs(delta_enemy) < math.radians(45)

    def move_enemy(self, player):
        # encontrar inimigo:
        en_row = int(self.sprite.y // TILE_SIZE)
        en_col = int(self.sprite.x // TILE_SIZE)
        # e encontrar player:
        player_row = int(player.sprite.y // TILE_SIZE)
        player_col = int(player.sprite.x // TILE_SIZE)
        
        # traça o caminho entre inimigo e player
        path = bfs((en_row, en_col), (player_row, player_col)) # armazenar em lista para otimizar o cálculo do caminho

        if not path:
            return
        
        next_row, next_col = path[0] 
        # informa o caminho futuro, e divide a lista 
        # devolvendo apenas uma coordenada por frame ao inimigo

        target_x = next_col * TILE_SIZE + TILE_SIZE / 2 # e o "alvo" (player) nesse caminho futuro
        target_y = next_row * TILE_SIZE + TILE_SIZE / 2
        
        dy = target_y - self.sprite.y # coordenadas em pixels
        dx = target_x - self.sprite.x # e o quanto falta para chegar até o alvo
        self.angle = math.atan2(dy, dx)

        dist = math.hypot(dy, dx)
        # calcula a distância real (acima)
        if dist > self.sprite.speed:
            self.sprite.y += dy / dist * self.sprite.speed # e move o inimigo de acordo com a velocidade e dist
            self.sprite.x += dx / dist * self.sprite.speed
        else: # caso falte menos que a velocidade p/ chegar ao alvo
            self.sprite.pos = (target_x, target_y) # evita teleportar o inimigo
