import math
from world import TILE_SIZE, COLS, ROWS, world_map
from pgzero.actor import Actor
from player import Player
from main import random_pos
from collections import deque

player = Player()

class Enemy:
    def __init__(self) :
        self.actor = Actor('fantasma.png', anchor=('center', 'center'))
        self.pos = random_pos(x, y) # jeito de definir a posição (?)
        self.speed = 5.0
    # adicionar "estados p/ o inimigo"
    # Comentar bfs!!!!!!!!!!!!!!!!!!!!!!
    def bfs(start, goal):
        queue = deque([start]) # posições futuras do inimigo
        visited = {start} # posições passadas
        parent = {} # posições alcançadas

        while queue: # enquanto as posições futuras ainda não foram alcançadas (ainda há locais p/ "andar")
            current = queue.popleft() # retira a primeira posição da lista

            if current == goal: 
                # a posição a ser explorada é a mais antiga da lista, 
                # por isso a remoção do primeiro item:
                '''[(0, 0), (0,1), (1,0)]
                    current = (0,0)
                    nova lista:
                    [(0,1), (1,0)]'''
                path = []

                while current != start:
                    path.append(current)
                    current = parent[current] # como o caminho "acaba" quando se verifica o dicionário armazena onde o inimigo já procurou

                path.reverse() # o caminho fica de trás para frente, por isso o reverse
                return path

            row, col = current

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]: # explora a possibilidade das posições vizinhas
                nr = row + dr # e define as novas posições
                nc = col + dc

                if (0 <= nr < len(world_map) and 0 <= nc < len(world_map[0])
                    and world_map[nr][nc] != 1 and (nr, nc) not in visited):
                    # esse if verifica se aposição já foi passada e se é parede
                    visited.add((nr, nc))
                    parent[(nr, nc)] = current # chegou a posição (y, x) a partir da posição (y1, x1)
                    queue.append((nr, nc)) # se as condições forem prenchidas as novas posições são definidas

        return []
    # Implementar FOV e raycast do inimigo (possibilita o inimigo "parar de ver" o player):
    def can_see_player(self.actor, player):
        #colocar o DDA
        dx_enemy = player.actor.x - self.actor.x # encontrar o vetor entre inimigo e player
        dy_enemy = player.actor.y - self.actor.y
        dist_to_player = math.hypot(dy_enemy, dx_enemy) # direção do inimigo (onde ele "olha") -------------------
        en_angle = math.atan2(dy_enemy, dx_enemy)
        
        ray_y = math.sin(en_angle)
        ray_x = math.cos(en_angle)
        # a partir das coordenadas do raio, as coordenadas 
        # em pixel do player serão contadas a partir de TILE_SIZE
        y = self.actor.y / TILE_SIZE
        x = self.actor.x / TILE_SIZE # dividir por TILE_SIZE mostra em qual coluna o player está
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

    def get_enemy_fov(self.actor, player): # ângulo do inimigo
        dx_en = player.actor.x - self.actor.x
        dy_en = player.actor.y - self.actor.y

        angle_to_player = math.atan2(dy_en, dx_en) # direção do inimigo (onde ele "olha") -------------------

        delta_enemy = angle_to_player - self.actor.angle 
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

    def move_enemy():
        # encontrar inimigo:
        en_row = int(enemy.y // TILE_SIZE)
        en_col = int(enemy.x // TILE_SIZE)
        # e encontrar player:
        player_row = int(player.y // TILE_SIZE)
        player_col = int(player.x // TILE_SIZE)
        
        # traça o caminho entre inimigo e player
        path = bfs((en_row, en_col), (player_row, player_col)) # armazenar em lista para otimizar o cálculo do caminho

        if not path:
            return
        
        next_row, next_col = path[0] 
        # informa o caminho futuro, e divide a lista 
        # devolvendo apenas uma coordenada por frame ao inimigo

        target_x = next_col * TILE_SIZE + TILE_SIZE / 2 # e o "alvo" (player) nesse caminho futuro
        target_y = next_row * TILE_SIZE + TILE_SIZE / 2
        
        dy = target_y - enemy.y # coordenadas em pixels
        dx = target_x - enemy.x # e o quanto falta para chegar até o alvo

        dist = math.hypot(dy, dx)
        # calcula a distância real (acima)
        if dist > enemy.vel:
            enemy.y += dy / dist * enemy.vel # e move o inimigo de acordo com a velocidade e dist
            enemy.x += dx / dist * enemy.vel
        else: # caso falte menos que a velocidade p/ chegar ao alvo
            enemy.pos = (target_x, target_y) # evita teleportar o inimigo
