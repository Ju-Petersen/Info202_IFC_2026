class Veiculo():
    def __init__(self, pl, cor, tq, odo, rend, des):
        self.placa = pl
        self.cor = cor
        self.tanque = tq
        self.odometro = odo
        self.rendimento = rend
        self.desenho = des

    def __str__(self):
        return f'''
            placa: {self.placa}
            cor: {self.cor}
            tanque: {self.tanque}
            odometro: {self.odometro}
            rendimento: {self.rendimento}
            {self.desenho}'''
    # Gasta 1 litro por x km (rendimento)
    # Atualiza odometro por cada km rodado
    def andar(self):
        self.tanque -= 1
        self.odometro += self.rendimento

class Pista():
    def __init__(self, ext):
        self.extensao = ext
        self.veiculos = []