import math
from world import WIDTH

FOV = math.radians(60) # campo de visão, 60°
RES = 4 # resolução p/ rendenização
NUM_RAYS = WIDTH // RES # raios (vetores) que serão 'desenhados' a partir do movimento do player#0 são espaçoes vazios e 1 são as
DIST_PLANO = WIDTH / (2 * math.tan(FOV/2))