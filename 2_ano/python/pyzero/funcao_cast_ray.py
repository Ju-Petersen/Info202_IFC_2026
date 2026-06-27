from raycast import *

# função p/encontrar parede ('lançar' raio) antiga: (iteração por pixel)
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
