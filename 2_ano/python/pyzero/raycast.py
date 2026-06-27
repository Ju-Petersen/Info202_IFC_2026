import os
#posição da janela:
os.environ['SDL_VIDEO_WINDOW_POS'] = "center"

import pygame
import pgzrun
import math

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
map = [
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

WIDTH = len(map[0]) * TILE_SIZE
HEIGHT = len(map) * TILE_SIZE

FOV = math.radians(60) # campo de visão, 60°
RES = 4 # resolução p/ rendenização
NUM_RAYS = WIDTH // RES # raios (vetores) que serão 'desenhados' a partir do movimento do player#0 são espaçoes vazios e 1 são as
DIST_PLANO = WIDTH / (2 * math.tan(FOV/2))

player = Actor('circulo.png', anchor=('center', 'center'))
player.vel = 1.5
player.angle = 0.0 #o centro de rotação é o ponto âncora e ângulo em rad

def has_wall(x, y):
    col = int(x // TILE_SIZE)
    row = int(y // TILE_SIZE)

    if row < 0 or row >= ROWS:
        return 1
    if col < 0 or col >= COLS:
        return 1

    return map[row][col]

player.pos = TILE_SIZE*2, TILE_SIZE*2
if has_wall(player.x, player.y):
    player.pos = (TILE_SIZE*2) - 2, (TILE_SIZE*2) - 2

# Implementação DDA:

def cast_ray(angle):
    ray_x = math.cos(angle)
    ray_y = math.sin(angle)
    # a partir das coordenadas do raio, as coordenadas 
    # em pixel do player serão contadas a partir de TILE_SIZE
    x = player.x / TILE_SIZE # dividir por TILE_SIZE mostra em qual coluna o player está
    y = player.y / TILE_SIZE
    '''A iteração da fução cast_ray antiga percorria cada pixel:

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
    +------+-------+------+'''
    # posição atual e futura:
    map_x = int(x)
    map_y = int(y)
    # calcular delta de "depth" para mostrar quanto o vetor precisa 
    # percorrer até chegar a próxima célula
    if ray_x == 0: # vai verificar o quanto precisa andar até chegar a próxima coluna
        delta_depth_x = 1e30 
        # considerar o delta da distância x e y por conta dos ângulos, 
        # ou seja, conforme um ângulo é mais reto ou diagonal leva mais 
        # tempo p/ o vetor atravessá-lo
    else:
        delta_depth_x  = abs(1/ray_x)
    if ray_y == 0:
        delta_depth_y = 1e30
    else:
        delta_depth_y  = abs(1/ray_y)
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
            +------+------+-------+'''
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
        if map[map_y][map_x]:
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
        
    hit_x = player.x + ray_x * depth
    hit_y = player.y + ray_y * depth
        
    return depth, hit_x, hit_y, side

def draw():
    screen.clear()
    screen.fill('lightblue')
    '''# acessar cada linha por coluna para rendenizar as paredes 
    for r in range(len(map)):
        for c in range(len(map[0])):
            # encontrar as coordenadas do tile
            tile_x = c * TILE_SIZE - 1 # loop colunas
            tile_y = r * TILE_SIZE - 1 # loop linhas
            # verificar se é True ou False:
            if map[r][c] == 1:
                TILE.topleft = tile_x, tile_y # lembrar de definir a posição!!!
                #screen.draw.filled_rect(TILE, BLUE) #desenhar o tile para teste
            elif map[r][c] == 0:
                TILE.topleft = tile_x, tile_y #tyle_y = r * TILE_SIZE - 1 e tyle_x = c * TILE_SIZE - 1
                #screen.draw.rect(TILE, WHITE) #desenhar o tile para teste
    '''
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
    screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT//2), (120,170,255))
    screen.draw.filled_rect(Rect(0, HEIGHT//2, WIDTH, HEIGHT//2), (80,80,80))
    
    for alt, depth in enumerate(rays):
        h = (TILE_SIZE * DIST_PLANO)/depth
        h = min(HEIGHT, h)
        x = alt*column_width
        y = HEIGHT/2 - h/2
        rect_screen = Rect(x, y, column_width+2, h)
        screen.draw.filled_rect(rect_screen, (120,120,255))

def update():
    cos_a = math.cos(player.angle)
    sin_a = math.sin(player.angle)
    dx = player.width / 2
    dy = player.height / 2
    
    player_posx = player.x # posição futura
    player_posy = player.y # posição futura

    if keyboard.w:
        player_posy += sin_a * player.vel #anda em x ou y de acordo com a direção que o player "olha"
        player_posx += cos_a * player.vel
    if keyboard.s:
        player_posy -= sin_a * player.vel
        player_posx -= cos_a * player.vel
    if keyboard.d:
        player_posx -= sin_a*player.vel
        player_posy += cos_a*player.vel
    if keyboard.a:
        player_posx += sin_a*player.vel
        player_posy -= cos_a*player.vel
    
    mouse_dx, mouse_dy = pygame.mouse.get_rel()
    player.angle += mouse_dx * 0.002
    player.angle -= mouse_dy * 0.002

    if not (has_wall(player_posx-dx, player.y-dy) or has_wall(player_posx+dx, player.y-dy) or
    has_wall(player_posx+dx, player.y+dy) or has_wall(player_posx-dx, player.y+dy)):
        player.x = player_posx
    # testa movimento em Y
    if not (has_wall(player.x-dx, player_posy-dy) or has_wall(player.x+dx, player_posy-dy) or
    has_wall(player.x+dx, player_posy+dy) or has_wall(player.x-dx, player_posy+dy)):
        player.y = player_posy

pgzrun.go()
