import os

#posição da janela:
os.environ['SDL_VIDEO_WINDOW_POS'] = "center" #ou os.environ['SDL_VIDEO_CENTERED'] = '1', ambas funcionam

import pgzrun

quad = Actor('quadrado.png')
quad.pos = 300, 200

base = Actor('base.png')
base.pos = 400, 400

# definir largura, altura e título da janela
TITLE = "ABCD"
WIDTH = 800
HEIGHT = 600 #altura da tela baseada na altura do ator

RED = 200, 0, 0
BOX = Rect((300, 400), (200, 100)) #definir forma com Rect((pos, pos), (largura, altura))

# método que vai desenhar os atores na tela
def draw():
    screen.clear()
    quad.draw()
    base.draw()

def update():
    if not quad.colliderect(base):
        quad.top += 4
    else:
        quad.left += 3
    if quad.top > HEIGHT:
        quit()
# executar o jogo
pgzrun.go()
