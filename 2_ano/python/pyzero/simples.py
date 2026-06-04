# importar o módulo pgzrun para rodar o jogo
import pgzrun
import os

#janela:
os.environ['SDL_VIDEO_WINDOW_POS'] = "center" #ou os.environ['SDL_VIDEO_CENTERED'] = '1', ambas funcionam
# criar um "ator"
quad = Actor('quadrado.png')
# definir posição do ator (x, y)
quad.pos = 300, -50
quad.vel = 0.5

#ator2:
quad2 = Actor('quadrado2.png')
quad2.pos = 450, -50
quad2.vel = 1

# criar uma "base"
base = Actor('base.png')
# definir a posição da base
base.pos = 400, 700

# definir largura, altura e título da janela
TITLE = "ABCD"
WIDTH = 800
HEIGHT = 750

# método que vai desenhar os atores na tela
def draw():
    # limpar a tela
    screen.clear()
    screen.fill('lightblue')
    # desenhar os atores
    quad2.draw()
    quad.draw()
    base.draw()

# método que vai atualizar a posição dos atores
def update():  
    # se o ator NÃO colidiu com a base...
    if not quad.colliderect(base):
        # o ator continua "caindo"
        quad.top += 1
        #aumentando a velocidade:
        quad.y += quad.vel
    if not quad2.colliderect(base):
        quad2.top +=1
        quad2.y += quad2.vel

# executar o jogo
pgzrun.go()

''' EXERCÍCIOS:

a) aumentar a velocidade de queda do quadrado - FEITO (adicionar velocidade ao criar o ator e ao dar update)
b) mudar a posição inicial do quadrado (colocar o quadrado mais alto) - FEITO (mudar a posção na definição do ator)
c) mudar a posição da base (colocar a base mais para baixo) - FEITO (mudar a posção na definição do ator)
d) mudar as figuras da base e do quadrado - FEITO (apenas mudar a imagem colada no foldar images e atualizá-la no código)
e) colocar 2 quadrados caindo ao mesmo tempo - FEITO (adicionar outro ator)

Para fazer as atividades a seguir, você deverá buscar na Internet/IA
como realizá-las no pygame zero:

f) alterar a cor de fundo da janela - FEITO
===> "como alterar a cor de fundo da janela no pygame zero"
g) centralizar a janela na tela - FEITO
===> "como centralizar a janela no pygame zero"
h) colocar um título na janela - FEITO
===> "como colocar um título na janela no pygame zero"

'''