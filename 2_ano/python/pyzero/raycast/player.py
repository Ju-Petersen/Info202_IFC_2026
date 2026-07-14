from pgzero.actor import Actor
from main import random_pos

class Player:
    def __init__(self) :
        self.actor = Actor('circulo.png', anchor=('center', 'center'))
        self.pos = random_pos(x, y) # jeito de definir a posição (?)
        self.speed = 5.0
        self.angle = 0.0