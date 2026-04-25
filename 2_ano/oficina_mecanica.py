from oficinamecanica_classes import *

pess = Pessoa("João", "(47)123456", "28/01/2010")
pess1 = Pessoa("Mario", "(47)654321", "02/12/2009")
pess2 = Pessoa("Maria", "(47)987654", "15/05/2011")
pess3 = Pessoa("Sofia", "(47)456789", "20/08/2012")
pess4 = Pessoa("Osvaldo", "(47)321654", "10/11/2008")

mec = Mecanico(pess1) #Mecânico é uma pessoa!!!
mec2 = Mecanico(pess4)

cli = Cliente(pess, "joaoo@gmail.com") #Cliente é uma pessoa + email desta.
cli1 = Cliente(pess2, "ma@gmail.com")
cli2 = Cliente(pess3, "so@gmail.com")

vei = Carro("AAAAAAAA", 5, "azul", 4) #Lembrar que carro é um veículo, ou que "vei" é igual a "Carro(...)".
vei2 = Moto("BBBBBBBB", "preta")
vei3 = Onibus("CCCCCCCC", "vermelho", 50)

ser = Servico("troca de pneu", 250)
ser1 = Servico("troca de óleo", 150)
ser2 = Servico("troca de bateria", 300)

ord_ser = Ordem_servico("31/03/2026", vei, "01/04/2026", cli, 20)
ord_ser1 = Ordem_servico("30/03/2026", vei2, "01/04/2026", cli1, 10)
ord_ser2 = Ordem_servico("29/03/2026", vei3, "01/04/2026", cli2, 15)

serre = Servico_realizado(ser, mec, ord_ser) #O serviço é realizado ao ter um mecânico designado e um "tipo" de serviço.
serre1 = Servico_realizado(ser1, mec2, ord_ser1)
serre2 = Servico_realizado(ser2, mec, ord_ser2)

print(serre)
print(serre1)
print(serre2)