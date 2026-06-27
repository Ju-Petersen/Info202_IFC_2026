from raycast import *

'''A iteração da fução cast_ray atual percorre cada pixel:

    while True:
            x += math.cos(angle)*step
            y += math.sin(angle)*step
            depth += step

Com o DDA, o processo é localizado por células/tiles. 
Ou seja, os TILES desenhados ao invés de suas coordenadas por píxel:
+----+----+----+
|    |    |    |Irá identificar qual linha o vetor atinge,
| P  |    |    | se nesta há uma parede, gera colisão.
+----+----+----+Cada retângulo nesse exemplo é uma célula,
|    |    |    |se não há uma parede nesta, ele "pula" para a próxima.
|    |    |####|
+----+----+----+'''

def cast_ray(angle):
    ray_x = math.cos(angle)
    ray_y = math.sin(angle)
    # a partir das coordenadas do raio, as coordenadas 
    # em pixel do player serão contadas a partir de TILE_SIZE
    x = player.x / TILE_SIZE # dividir por TILE_SIZE mostra em qual coluna o player está
    y = player.y / TILE_SIZE
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
        '''
            +------+-------+------+ Por exemplo, se para se mover "para frente", "delta_depth = 1",
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
        
    return depth, hit_x, hit_y

''' 
# função p/encontrar parede ('lançar' raio):
def cast_ray(angle):
    # modificando para usar a iteração por TILE, ao invés de pixels
    x = player.x
    y = player.y
    step = 1
    depth = 0

    while True:
        x += math.cos(angle)*step
        y += math.sin(angle)*step
        depth += step
        
        if has_wall(x, y):
            hit_x = x-math.cos(angle)
            hit_y = y-math.sin(angle)
            
            tile_x = int(hit_x // TILE_SIZE)
            tile_y = int(hit_y // TILE_SIZE)
            offset_x = hit_x % TILE_SIZE
            offset_y = hit_y % TILE_SIZE
            depth = math.hypot(hit_x - player.x, hit_y - player.y)
            # o retorno de depth significa que o vetor/linha
            # que estiver a A pixels de disância deve parecer
            # maior que o a B pixels de distância (considerando A < B)
            # essa profundiade é feita pelo desenho da altura inversamente proporcional
            return (hit_x, hit_y, depth, tile_x, tile_y, offset_x, offset_y)
'''
