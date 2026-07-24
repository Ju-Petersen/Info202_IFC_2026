import random
from pgzero.rect import Rect

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

TILE_SIZE = 55
TILE = Rect(0, 0, TILE_SIZE, TILE_SIZE) #definir o tamanho do tile (quadrado) para rendenização

ROWS = 14
COLS = 25

def has_wall(x, y):
    col = int(x // TILE_SIZE)
    row = int(y // TILE_SIZE)

    if row < 0 or row >= ROWS:
        return 1
    if col < 0 or col >= COLS:
        return 1

    return world_map[row][col]

def random_pos():
    # os espaços livres são uma lista que retorna uma posição de spawn p/ o inimigo
    free_space = []

    # acessa as posições na grid do mapa:
    for row in range(len(world_map)):
        for col in range(len(world_map[row])): # verifica se a linha tem um tile 0:
            if world_map[row][col] == 0: # 0 são os espaços livres (que não tem parede)
                free_space.append((row, col))
    
    if not free_space:
        return None
    row, col = random.choice(free_space) # escolhe um espaço 0 para spawnar o inimigo
    
    y = row * TILE_SIZE + TILE_SIZE / 2
    x = col * TILE_SIZE + TILE_SIZE / 2

    return x, y # retorna a posição aleatória