class Player:
    def __init__(self):   
        self.sprite = Actor('circulo.png', anchor=('center', 'center'))
        self.angle = 0.0 #o centro de rotação é o ponto âncora e ângulo em rad
        self.speed = 1.5
    