class Veiculo():
    def __init__(self, pl: str, ano: int):
        self.placa = pl
        self.ano = ano

    def __str__(self):
        return f'''
        {self.placa}
        ano: {self.ano}'''
    
class Moto(Veiculo): #Sendo "Moto", filho de "Veiculo".
    def __init__(self, pl: str, ano: int):
        super().__init__(pl, ano) #Herda apenas placa e cor (no exercício não foi pedido que adicionasse a diferenciação por cilindradas).

    def __str__(self):
        return f'''{super().__str__()}'''
    
class Caminhao(Veiculo): #Sendo "Moto", filho de "Veiculo".
    def __init__(self, pl: str, ano: int, ps_kg: int):
        super().__init__(pl, ano) #Herda apenas placa e cor (no exercício não foi pedido que adicionasse a diferenciação por cilindradas).
        self.peso_kg = ps_kg

    def __str__(self):
        return f'''{super().__str__()}
        Peso do veículo: {self.peso_kg} kg'''
    
v1 = Moto("BBBBBBBB", 2010)
v2 = Caminhao("CCCCCCCC", 2005, 10)

print(f'''
{v1}
{v2}''')
