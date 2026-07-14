import math

TITLE = "Tentando Raycasting"
TILE_SIZE = 55
TILE = Rect(0, 0, TILE_SIZE, TILE_SIZE) #definir o tamanho do tile (quadrado) para rendenização

ROWS = 14
COLS = 25

FOV = math.radians(60) # campo de visão, 60°
RES = 4 # resolução p/ rendenização

PLAYER_SPEED = 1.5
