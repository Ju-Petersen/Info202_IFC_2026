# Implementar FOV e raycast do inimigo (possibilita o inimigo "parar de ver" o player):
def see_player(angle):
    ray_y = math.sin(angle)
    ray_x = math.cos(angle)
     # a partir das coordenadas do raio, as coordenadas 
     # em pixel do player serão contadas a partir de TILE_SIZE
    y = player.y / TILE_SIZE
    x = player.x / TILE_SIZE # dividir por TILE_SIZE mostra em qual coluna o player está
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
