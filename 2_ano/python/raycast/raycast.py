from world import world_map
from settings import  TILE, TILE_SIZE, ROWS, COLS, FOV, RES
# Implementação DDA:
# cast_ray para inimigo também

def cast_ray(player, world_map, angle):
    ray_y = math.sin(angle)
    ray_x = math.cos(angle)
    # a partir das coordenadas do raio, as coordenadas 
    # em pixel do player serão contadas a partir de TILE_SIZE
    y = player.sprite.y / TILE_SIZE
    x = player.sprite.x / TILE_SIZE # dividir por TILE_SIZE mostra em qual coluna o player está
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
    
    hit_y = player.sprite.y + ray_y * depth
    hit_x = player.sprite.x + ray_x * depth
        
    return depth, hit_x, hit_y, side

def draw_walls(screen, player):
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

def draw_enemy(self, screen, player, rays, enemy_img):
        screen.clear()
        screen.fill('lightblue')
        
        dx = self.sprite.x - player.sprite.x
        dy = self.sprite.y - player.sprite.y

        en_dist = math.hypot(dx, dy)
        angle = math.atan2(dy, dx)
        delta = angle - player.angle

        while delta > math.pi:
            delta -= 2*math.pi
        while delta < -math.pi:
            delta += 2*math.pi

        if abs(delta) > FOV/2:
            return
        
        en_dist *= math.cos(delta)
        if en_dist <= 1:
            en_dist = 1
        en_h = TILE_SIZE * DIST_PLANO / en_dist
        en_w = en_h
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
