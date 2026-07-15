import random
from settings import TILE, TILE_SIZE, ROWS, COLS

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
                free_space.append((col, row))
    
    if not free_space:
        return None
    row, col = random.choice(free_space) # escolhe um espaço 0 para spawnar o inimigo
    
    y = row * TILE_SIZE + TILE_SIZE / 2
    x = col * TILE_SIZE + TILE_SIZE / 2

    return x, y # retorna a posição aleatória

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
