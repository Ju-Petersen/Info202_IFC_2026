# biblioteca adicional para o comando seguinte
import os

# comando para centralizar a janela
os.environ['SDL_VIDEO_CENTERED'] = '1'

# biblioteca pygamezero
import pgzrun
from pygame import Rect
from collections import deque
import random

# passo do jogador
PASSO = 3

# define o labirinto
maze = [
"########################################",
"#     #       #       #               G#",
"# ### # ##### # ##### # ####### #  #####",
"# #   #     # #     # # #     # #      #",
"# # ####### # ##### # # # ### # ###### #",
"# #       # #     # # # # # # #      # #",
"# ####### # ##### # # # # # # ###### # #",
"#       # #     # # # # # # #      # # #",
"####### # ##### # # # # # # ###### # # #",
"#       #     # # # # # # #      # # # #",
"# ########### # # # # # # ###### # # # #",
"#           # # # # # # #      # # # # #",
"########### # # # # # # ###### # # # # #",
"#         # # # # # # #      # # # # # #",
"# ####### # # # # # # ###### # # # # # #",
"# #     # # # # # # #      # # # # # # #",
"# # ### # # # # # # ###### # # # # # # #",
"# # # # # # # # # #      # # # # # # # #",
"# # # # # # # # # ###### # # # # # # # #",
"# # # # # # # # #      # # # # # # # # #",
"# # # # # # # # ###### # # # # # # # # #",
"# # # # # # # #      # # # # # # # # # #",
"# # # # # # # ###### # # # # # # # # # #",
"#                                     # #",
"########################################",
]

# granularidade do labirinto
# cada caracter do labirinto será desenhado VEZES o tamanho da ESCALA
ESCALA = 30

# largura da tela: largura do labirinto VEZES o tamanho da ESCALA
WIDTH = 500

# altura do labirinto: quantidade de elementos no vetor do labirinto (linhas)
# VEZES a ESCALA
HEIGHT = 500

#Para adicionar câmera no labirinto:
WORLD_WIDTH = len(maze[0]) * ESCALA
WORLD_HEIGHT = len(maze) * ESCALA

# jogador: retângulo que começa um pouco depois (5) da posição do labirinto
# o tamanho do jogador é 20 (largura) por 20
player = Rect((ESCALA + 5, ESCALA + 5), (20, 20))
# criar a câmera
camera_x = 0
camera_y = 0
# função que retorna se naquela posição existe ou não parede
def wall_at(x, y):
    # calcula em que posição da matriz o jogador está
    # divide a posição do jogador pela ESCALA,
    # pegando só a parte inteira da divisão
    col = x // ESCALA
    row = y // ESCALA

    # se naquele local houver PARECE, retorna verdadeiro
    # ("colisão": ali tem parede)
    if maze[row][col] == "#":
        return True

    # senão, retorna falso (não tem parede)
    return False

# função que tenta realizar o movimento
def try_move(dx, dy):

    # verifica se um dos quatro cantos está dentro de alguma parede
    '''
    (x1,y1)    (x2, y1)
    c1 ------ c4
    |          |
    |          |
    c2 ------ c3
    (x1,y2)    (x2,y2)

    '''

    # calcula as posições x1, x2, y1, y2
    x1 = player.x + dx
    x2 = player.x + dx + player.width
    y1 = player.y + dy
    y2 = player.y + dy + player.height
    
    # verifica se os pontos estão "dentro" da parede
    c1 = wall_at(x1, y1)
    c2 = wall_at(x2,y1)
    c3 = wall_at(x2,y2)
    c4 = wall_at(x1,y2)
    
    # se nenhum ponto estiver dentro da parede
    if not (c1 or c2 or c3 or c4):
        # movimenta o jogador
        player.x = x1
        player.y = y1

def goal_at(x, y):
    col = x // ESCALA
    row = y // ESCALA

    return maze[row][col] == "G"

def random_pos():
    free_space = []

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == " ":
                free_space.append((col, row))

    col, row = random.choice(free_space)

    x = col * ESCALA + 5
    y = row * ESCALA + 5

    return x, y
# inimigo
x, y = random_pos()
enemy = Rect((x, y), (20, 20))
enmy_timer = 0

def bfs(start, goal):
    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []

            while current != start:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path

        row, col = current

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr = row + dr
            nc = col + dc

            if (
                0 <= nr < len(maze)
                and 0 <= nc < len(maze[0])
                and maze[nr][nc] != "#"
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                parent[(nr, nc)] = current
                queue.append((nr, nc))

    return []

def move_enemy():
    enemy_cell = (
        enemy.y // ESCALA,
        enemy.x // ESCALA
    )

    player_cell = (
        player.y // ESCALA,
        player.x // ESCALA
    )

    path = bfs(enemy_cell, player_cell)

    if path:
        next_row, next_col = path[0]

        enemy.x = next_col * ESCALA + 5
        enemy.y = next_row * ESCALA + 5

def update():
    global camera_x, camera_y, enmy_timer
    # se foi apertada a seta esquerda
    if keyboard.left:
        # tenta ir para a esquerda
        try_move(-PASSO, 0)

    if keyboard.right:
        try_move(PASSO, 0)
    if keyboard.up:
        try_move(0, -PASSO)
    if keyboard.down:
        try_move(0, PASSO)

    camera_x = player.centerx - WIDTH // 2
    camera_y = player.centery - HEIGHT // 2
    #---------------------------------------------------------
    camera_x = max(0, min(camera_x, WORLD_WIDTH - WIDTH))
    camera_y = max(0, min(camera_y, WORLD_WIDTH - HEIGHT))
    
    enmy_timer += 1

    if enmy_timer >= 15:
        move_enemy()
        enmy_timer = 0
    if enemy.colliderect(player):
        quit()
    
def draw():
    # limpa a tela
    screen.clear()

    # percorrer as linhas do labirinto
    for row in range(len(maze)):

        # percorrer as colunas do labirinto
        for col in range(len(maze[row])):

            # se for parede...
            if maze[row][col] == "#":
                # desenha parede :-)
                wall = Rect(
                    (col * ESCALA - camera_x, #desenhando as paredes conforme a câmera
                     row * ESCALA - camera_y),
                    (ESCALA, ESCALA)
                )
                screen.draw.filled_rect(
                    wall,
                    (100, 100, 100)
                )
            # Se for a "chegada"
            if maze[row][col] == "G":
                # desenha chegada :-)
                wall = Rect(
                    (col * ESCALA - camera_x, #desenhando as paredes conforme a câmera
                     row * ESCALA - camera_y),
                    (ESCALA, ESCALA)
                )
                screen.draw.filled_rect(
                    wall,
                    (0, 100, 0)
                )

    # desenha o jogador
    player_screen = Rect(
        (player.x - camera_x, player.y - camera_y), 
        (player.width, player.height)
    )
    screen.draw.filled_rect(player_screen, "green")
    enemy_screen = Rect(
        (enemy.x - camera_x, enemy.y - camera_y), 
        (enemy.width, enemy.height)
    )
    screen.draw.filled_rect(enemy_screen, "red")

    if goal_at(player.x, player.y):
        screen.clear()
        screen.fill((0, 0, 255))
        screen.draw.text("Você Venceu!!", center=(WIDTH // 2, HEIGHT // 2), color=(255, 0, 0))

# executa o pygme zero
pgzrun.go()

'''
EXERCÍCIOS:
a) mudar a escala do labirinto (valor da variável ESCALA) - FEITO
b) modificar o labirinto (variável maze) - FEITO
c) fornecer o labirinto para uma IA e pedir para gerar um labirinto maior - 

outras melhorias:
https://chatgpt.com/share/6a36f25d-4e18-83e9-a918-1d87a2da7811

Extras:
- Câmera que se movimenta com o player; - FEITO
- Consertar o aviso de "você venceu"; - FEITO
- Adicionar perseguição; - FEITO (explicar)
- Mais níveis (talvez);
'''
