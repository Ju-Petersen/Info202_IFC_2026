import os
#posição da janela:
os.environ['SDL_VIDEO_WINDOW_POS'] = "center"

import pygame
import pgzrun
from pgzero.actor import Actor
from pgzero.rect import Rect

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import pygame
    screen: pygame.Surface

import math
import random
from collections import deque

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

TITLE = "Tentando Raycasting"
TILE_SIZE = 55
TILE = Rect(0, 0, TILE_SIZE, TILE_SIZE) #definir o tamanho do tile (quadrado) para rendenização

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

ROWS = 14
COLS = 25

# no "for" abaixo, o "c" dá um loop pelas colunas, e "r" por cada linha
world_map = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1],
[1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1],
[1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1],
[1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

WIDTH = len(world_map[0]) * TILE_SIZE
HEIGHT = len(world_map) * TILE_SIZE

FOV = math.radians(60) # campo de visão, 60°
RES = 4 # resolução p/ rendenização
NUM_RAYS = WIDTH // RES # raios (vetores) que serão 'desenhados' a partir do movimento do player#0 são espaçoes vazios e 1 são as
DIST_PLANO = WIDTH / (2 * math.tan(FOV/2))

PLAYER_SPEED = 1.5
player = Actor('circulo.png', anchor=('center', 'center'))
player.angle = 0.0 #o centro de rotação é o ponto âncora e ângulo em rad

def has_wall(x, y):
    col = int(x // TILE_SIZE)
    row = int(y // TILE_SIZE)

    if row < 0 or row >= ROWS:
        return 1
    if col < 0 or col >= COLS:
        return 1

    return world_map[row][col]

player.pos = TILE_SIZE*2, TILE_SIZE*2
if has_wall(player.x, player.y):
    player.pos = (TILE_SIZE*2) - 2, (TILE_SIZE*2) - 2

def random_pos():
    # os espaços livres são uma lista que retorna uma posição de spawn p/ o inimigo
    free_space = []

    # acessa as posições na grid do mapa:
    for row in range(len(world_map)):
        for col in range(len(world_map[row])): # verifica se a linha tem um tile 0:
            if world_map[row][col] == 0: # 0 são os espaços livres (que não tem parede)
                free_space.append((col, row))
    
    if not free_space:
        return None
    row, col = random.choice(free_space) # escolhe um espaço 0 para spawnar o inimigo
    
    y = row * TILE_SIZE + TILE_SIZE / 2
    x = col * TILE_SIZE + TILE_SIZE / 2

    return y, x # retorna a posição aleatória

# inimigo
y, x = random_pos()
enemy = Actor('fantasma.png', anchor=('center', 'center'))
enemy.pos = random_pos()
enemy_img = pygame.image.load('2_ano/python/pyzero/images/fantasma.png').convert_alpha()
enemy.vel = 5.0
enemy_timer = 0

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

# Entender melhor move_enemy !!!!!!!!!!!!!!!!!!!!!!!!!
def move_enemy():
    # encontrar inimigo:
    en_row = int(enemy.y // TILE_SIZE)
    en_col = int(enemy.x // TILE_SIZE)
    # e encontrar player:
    player_row = int(player.y // TILE_SIZE)
    player_col = int(player.x // TILE_SIZE)
    
    # traça o caminho entre inimigo e player
    path = bfs((en_row, en_col), (player_row, player_col))

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
        enemy.pos = (target_y, target_x) # evita teleportar o inimigo

# Implementação DDA:

def cast_ray(angle):
    ray_y = math.sin(angle)
    ray_x = math.cos(angle)
    # a partir das coordenadas do raio, as coordenadas 
    # em pixel do player serão contadas a partir de TILE_SIZE
    y = player.y / TILE_SIZE
    x = player.x / TILE_SIZE # dividir por TILE_SIZE mostra em qual coluna o player está
    '''
    A iteração da fução cast_ray antiga percorria cada pixel:

        while True:
                x += math.cos(angle)*step --> step = 1 (a cada movimento, adicionava um passo)
                y += math.sin(angle)*step
                depth += step

    Com o DDA, o processo é localizado por células/tiles. 
    Ou seja, os TILES desenhados ao invés de suas coordenadas por píxel:
    +------+-------+------+
    |  /    |      |      | Irá identificar qual linha o vetor atinge,
    | P --> |      |      | se nesta há uma parede, gera colisão.
    +--\----+------+------+ Cada retângulo nesse exemplo é uma célula,
    |   \   |      |      | se não há uma parede nesta, ele "pula" para a próxima.
    |       |      | #####|
    +------+-------+------+
    '''
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
        # desta maneira, quando se atravessa uma célula adiciona "delta_depth" 
        # como uma PA, qual a razão é determinada pelo ângulo da direção "apontada" pelo player:
        ''' +------+-------+------+ Por exemplo, se para se mover "para frente", "delta_depth = 1",
            |  /    |      |      | então para chegar até a última coluna: "side_depth = 1"
            | P --> |      |      | e após o passo: "side_depth = side_depth + delta_depth",
            +--\----+------+------+ sendo que "side_depth" sempre aumenta até o player chegar a última coluna.
            |   \   |      |      | Ou simplesmente aos limites do mapa.
            |       |      | #####| Logo, uma PA de razão "delta_depyh".
            +------+------+-------+
            '''
    else:
        step_x = 1
        side_depth_x = (map_x + 1-x)*delta_depth_x
    if ray_y < 0:
        step_y = -1
        side_depth_y = (y - map_y)*delta_depth_y
    else:
        step_y = 1
        side_depth_y = (map_y + 1-y)*delta_depth_y
    
    hit = False
    
    while not hit:
        if side_depth_x < side_depth_y:
            side_depth_x += delta_depth_x
            map_x += step_x # qual coluna está percorrendo
            side = 0 # se for no eixo x, lado = True
        else:
            side_depth_y += delta_depth_y
            map_y += step_y
            side = 1 # se for no eixo y, lado = False (afinal, é vertical)
        if not (0 <= map_x < COLS and 0 <= map_y < ROWS):
            break
        if world_map[map_y][map_x]:
            hit = True
    
    # profundidade e ponto de colisão:
    if side == 0:
        wall_depth = (map_x - x + (1-step_x) / 2)/ray_x
        # se lado = True e há uma parede ...
    else:
        wall_depth = (map_y - y + (1-step_y) / 2)/ray_y
    # a profundidade é "desenhada", ou melhor, convertida em pixels
    depth = wall_depth * TILE_SIZE
    depth *= math.cos(angle-player.angle)
    
    hit_y = player.y + ray_y * depth
    hit_x = player.x + ray_x * depth
        
    return depth, hit_x, hit_y, side

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
        
    dx_enemy = enemy.x - player.x # encontrar o vetor entre inimigo e player
    dy_enemy = enemy.y - player.y
    en_angle = math.atan2(dy_enemy, dx_enemy) # direção do inimigo (onde ele "olha")
    delta_enemy = en_angle - player.angle # variação do en_angle
    
    while delta_enemy > math.pi: # limitação dos ângulos
         delta_enemy -= 2*math.pi

    while delta_enemy < -math.pi: # limitação dos ângulos
        delta_enemy += 2*math.pi
    
    en_depth = math.hypot(dy_enemy, dx_enemy) # distância entre ambos
    en_dist = en_depth * math.cos(delta_enemy)
    
    if abs(delta_enemy) < FOV/2:
        en_height = (TILE_SIZE * DIST_PLANO) / en_dist
        en_width = en_height
        screen_x = (delta_enemy / FOV + 0.5) * WIDTH
        screen_y = HEIGHT/2 - en_height/2
        
        ray = int(screen_x / column_width)

        if 0 <= ray < len(rays):
            if en_dist < rays[ray]:
                en_screen = pygame.transform.scale(enemy_img, (int(en_width), int(en_height)))
                screen.surface.blit(en_screen, (screen_x - en_width/2, screen_y))

    # Implementar a lógica do inimigo parecida com o cast_ray das paredes,
    # podendo mostrá-lo quando o FOV do player "enquadra" o inimigo.

def update():
    global enemy_timer
    
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
        move_enemy()
        enemy_timer = 0
    if enemy.colliderect(player):
        quit()
    
    # testa movimento em Y
    if not (has_wall(player.x-dx, player_posy-dy) or has_wall(player.x+dx, player_posy-dy) or
    has_wall(player.x+dx, player_posy+dy) or has_wall(player.x-dx, player_posy+dy)):
        player.y = player_posy
    # movimento em X
    if not (has_wall(player_posx-dx, player.y-dy) or has_wall(player_posx+dx, player.y-dy) or
    has_wall(player_posx+dx, player.y+dy) or has_wall(player_posx-dx, player.y+dy)):
        player.x = player_posx

pgzrun.go()
