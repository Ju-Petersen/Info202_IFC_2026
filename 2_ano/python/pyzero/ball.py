# biblioteca adicional para o comando seguinte
import os
# comando para centralizar a janela
os.environ['SDL_VIDEO_CENTERED'] = '1'

# biblioteca pygamezero e componente Actor
import pgzrun
from pgzero.actor import Actor

''' 
-------------------------
Segue um trecho de código para ignorar warning sballre o screen.
Um "warning" é um sublinhado em amarelo que aparece no código.
Quem gera o warning é o Pylance, uma extensão do VSCode 
que analisa o código em python realizando verificações.


* No caso de "screen", ele é criado pelo pygame zero quando o
programa é executado, mas o Pylance não sabe disso, por isso
aponta o warning.
* No caso de "Actor", a classe não está declarada, então
o Pylance aponta warning.

Para "resolver" esses warnings, usamos a variável TYPE_CHECKING.
TYPE_CHECKING é Falso quando o programa está executando.
Quando estamos editando o código no VSCode, ele é Verdadeiro.
Então, durante a edição, informamos a origem de "screen"
e de "Actor", para que o Pylance não gere um "warning".
--------------------------
'''

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import pygame
    screen: pygame.Surface

from random import randint

# largura e altura da janela
WIDTH = 800
HEIGHT = 600

# fator de gravidade
GRAVITY = 0.5

# perda de velocidade Y quando a bola bate no chão
# no caso, está igual a 85%
BOUNCE = 0.95

# altura do piso
FLOOR_Y = HEIGHT - 100
FLOOR_X = WIDTH

# piso / "chão"
floor = Actor('floor.png')
floor.left = 0
floor.top = FLOOR_Y
floor.right = FLOOR_X

# bola
ball = Actor('ballstaculo2.png')
# posição inicial da bola
ball.x = WIDTH // 2
ball.y = 100

ball_lst = []

for b in range(2):
        # cria um alvo ali em uma posição aleatória
        ball = ball
        ball.x = randint(0, WIDTH) + b * 100
        ball.y = randint(0, HEIGHT) + b * 100
         # velocidades próprias de cada bola
        ball.vx = 6 + b
        ball.vy = 5
        # ângulo inicial
        ball.angle = 0
        # adiciona o alvo na lista de alvos
        ball_lst.append(ball)

# velocidades iniciais da bola
vx = 2
vy = 0

def update():
    global ball, vx, vy, ball_lst

    for ball in ball_lst:
        # aumenta a velocidade da bola em Y, conforme a gravidade
        # (a bola está caindo!)
        vy += GRAVITY

        # move a bola em X e Y
        ball.x += vx
        ball.y += vy

        # se a bola encostar no chão...
        if ball.bottom >= floor.top:

            # bota a bola no chão
            ball.bottom = floor.top
            
            # inverte a velocidade Y, 
            # provocando uma PERDA quando bate no chão
            vy = -vy * BOUNCE 
            # alterar BOUNCE faz com que a bola 
            # retorne mais alto ou mais baixo

            # fricção da bola no chão: reduz a velocidade X
            vx = vx * 0.85 # a bola quica por mais tempo com a redução de fricção

            # se a velocidade X ficar muito pequena
            if abs(vx) < 0.1: # aumentar faz com que a bola fique quicando no mesmo lugar por mais tempo
                # pode parar em X
                vx = 0

            # se a velocidade Y for bem pequena
            if abs(vy) < 5: # aumentar ou diminuir faz com que a bola pareça mais pesada ou leve
                # pode parar!
                vy = 0

        # se a bola passar da parede esquerda
        if ball.left <= 0:
            # volta pro começo da parede
            # repare que a bola é posicionada "em seu lado esquerdo"
            ball.left = 0
            # inverte a velocidade X
            vx = -vx

        # se passar da parede direita
        if ball.right >= WIDTH:
            # volta pra parede direita
            # repare que a bola é posicionada em relação "a seu lado direito"
            # ela "encosta o lado direito na parede"
            ball.right = WIDTH
            # inverte a velocidade X
            vx = -vx

def draw():
    global ball_lst
    # desenha fundo azul
    screen.fill("skyblue")

    # desenha o piso
    floor.draw()

    # desenha a bola
    for ball in ball_lst:
        ball.draw()

pgzrun.go()

'''
EXERCÍCIOS:
a) alterar a velocidade inicial de queda da bola - FEITO(?)
b) alterar a gravidade do cenário - FEITO
c) alterar o fator de perda do impacto da bola no chão 
(ao quicar, ela pode perder mais ou menos velocidade) - FEITO (?)

Você pode também alterar a cor de fundo, 
a imagem do piso e a imagem da bola. - FEITO

Algumas coisas para se pensar sballre como poderia fazer...

d) tentar criar mais bolas? Em vez de criar variáveis com o 
nome "2", "3", poderia fazer uma "lista" :-)
e) aumentar o tamanho da janela?
f) tentar "girar" a bola? Procure assim no google: 
"pygamezero girar actor".
O giro seria diferente se a bola estiver quicando 
para a direita ou para a esquerda.

'''