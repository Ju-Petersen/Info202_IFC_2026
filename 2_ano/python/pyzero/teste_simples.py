import pgzrun
import os

#posição da janela:
os.environ['SDL_VIDEO_WINDOW_POS'] = "center" #ou os.environ['SDL_VIDEO_CENTERED'] = '1', ambas funcionam

#primeiro ator (procurar como simular primeira pessoa futuramente):
quad = Actor('quadrado.png')
# definir posição do ator (x, y)
quad.topright = 0, 10 #topright -> canto superior direito
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
HEIGHT = quad.height + 600 #altura da tela baseada na altura do ator

RED = 200, 0, 0
BOX = Rect((300, 400), (200, 100)) #definir forma com Rect((pos, pos), (largura, altura))

# método que vai desenhar os atores na tela
def draw():
    # limpar a tela
    screen.clear()
    screen.fill('lightblue')
    screen.draw.rect(BOX, RED)
    #screen.draw.circle((400, 300), 50, ('red')) !!lembrete de adicionar screen. antes de usar os objetos imbutidos!!
    # desenhar os ator e base
    quad.draw()
    quad2.draw()
    base.draw()

# método que vai atualizar a posição dos atores
def update():
    quad.left += 2
    if quad.left > WIDTH: #ator continua andando 2 px para a direita, o efeito de "loop" é pelo 'reset' que se dá quando o ato ultrapassa o tamanho da janela.
        quad.right = 0
    if not quad2.colliderect(base):
        quad2.top +=1
        quad2.y += quad2.vel
    if quad2.colliderect(BOX):
        sounds.vine.set_volume(0.2) #alterar volume do som
        sounds.vine.play() #tocar som da pasta sounds

# executar o jogo
pgzrun.go()

#função 'clock' e 'unique_schedule', a primeira para realizar uma mudança (sprite por exemplo) após um tempo 
#e a segunda, para evitar que a mudança seja acionada mais de uma vez (por exemplo repetindo muito cliques rápidos)