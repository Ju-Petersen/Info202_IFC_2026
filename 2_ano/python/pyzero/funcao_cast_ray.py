from raycast import *

# função p/encontrar parede ('lançar' raio) - antigo
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

# acessar cada linha por coluna para rendenizar as paredes - antigo
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
