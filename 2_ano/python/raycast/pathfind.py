from collections import deque# Comentar bfs!!!!!!!!!!!!!!!!!!!!!!
from world import world_map

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
