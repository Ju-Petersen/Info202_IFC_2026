import math
from pgzero.actor import Actor
from world import has_wall
from settings import TILE_SIZE

class Player:
    def __init__(self):   
        self.sprite = Actor('circulo.png', anchor=('center', 'center'))
        self.angle = 0.0 #o centro de rotação é o ponto âncora e ângulo em rad
        self.speed = 1.5
        self.sprite.pos = TILE_SIZE*2, TILE_SIZE*2
        if has_wall(self.sprite.x, self.sprite.y):
            self.sprite.pos = (TILE_SIZE*2) - 2, (TILE_SIZE*2) - 2
    
    def draw(self):
        self.sprite.draw()
        
    def update(self, keyboard):
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)
        dx = self.sprite.width / 2
        dy = self.sprite.height / 2
        
        player_posx = self.sprite.x # posição futura
        player_posy = self.sprite.y # posição futura
        
        if keyboard.lshift:
            self.speed = 3
        else:
            self.speed = 1.5
        if keyboard.w:
            player_posy += sin_a * self.speed #anda em x ou y de acordo com a direção que o player "olha"
            player_posx += cos_a * self.speed
        if keyboard.s:
            player_posy -= sin_a * self.speed
            player_posx -= cos_a * self.speed
        if keyboard.d:
            player_posx -= sin_a * self.speed
            player_posy += cos_a * self.speed
        if keyboard.a:
            player_posx += sin_a * self.speed
            player_posy -= cos_a * self.speed

        # testa movimento em Y
        if not (has_wall(self.sprite.x-dx, player_posy-dy) or has_wall(self.sprite.x+dx, player_posy-dy) or
        has_wall(self.sprite.x+dx, player_posy+dy) or has_wall(self.sprite.x-dx, player_posy+dy)):
            self.sprite.y = player_posy
        
        # movimento em X
        if not (has_wall(player_posx-dx, self.sprite.y-dy) or has_wall(player_posx+dx, self.sprite.y-dy) or
        has_wall(player_posx+dx, self.sprite.y+dy) or has_wall(player_posx-dx, self.sprite.y+dy)):
            self.sprite.x = player_posx
