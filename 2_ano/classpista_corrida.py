import time

class Veiculo():
    def __init__(self, pl, cor, tq, rend, des):
        self.placa = pl
        self.cor = cor
        self.tanque = tq
        self.odometro = 0
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
         # Implementar definições para mostrar e andar na pista.
    def esperar(self):
        # verificar se ainda tem pista, e se tiver, andar.
        for vei in self.veiculos:
            if vei.odometro <= self.extensao: # "vei" age como CONTADOR!! =! de "self"
                vei.andar()

    def grafico_pista(self):
        for vei in self.veiculos:
            pista = "__" * int(vei.odometro/10) # Print da pista usando a quantidade que indica no odômetro ajustada para aparecer no print
            print(vei.placa, vei.odometro, pista, vei.desenho)

vei1 = Veiculo("ABCD-1234", "azul", 30, 5, "O--O")
vei2 = Veiculo("DCBA-4321", "preto", 60, 10, "C---C")
relampago_marquinhos = Pista(250)
relampago_marquinhos.veiculos.append(vei1)
relampago_marquinhos.veiculos.append(vei2)

while True:
    relampago_marquinhos.esperar()
    relampago_marquinhos.grafico_pista()
    time.sleep(1)
    if relampago_marquinhos.veiculos[0].odometro >= 250 and relampago_marquinhos.veiculos[1].odometro >= 250:
        break
