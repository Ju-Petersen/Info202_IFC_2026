#Definição das classes:
class Pessoa():
    def __init__(self, nm, telef, dt_nasc):
        self.nome = nm
        self.telefone = telef
        self.data_nascimento = dt_nasc

    def __str__(self):
        return f'''    nome: {self.nome}
            telefone: {self.telefone}
            data de nascimento: {self.data_nascimento}'''

class Mecanico():
    def __init__(self, pess):
        self.pessoa =  pess

    def __str__(self):
        return f'''{self.pessoa}'''

class Cliente():
    def __init__(self, pess, em):
        self.pessoa = pess
        self.email = em

    def __str__(self):
        return f'''{self.pessoa}
            e-mail cliente: {self.email}'''
        
class Servico():
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f'''
        Descrição do serviço: {self.descricao}
        Valor: {self.valor}
        '''
        
class Servico_realizado():
    def __init__(self, servico, mecanico):
        self.servico = servico
        self.mecanico = mecanico

    def __str__(self):
        return f'''
        {self.servico}
        Realizado por:
        {self.mecanico}
        '''
        
class Ordem_servico():
    def __init__(self, data_entrada, veiculo, data_saida, cliente, desconto):
        self.data_entrada = data_entrada
        self.veiculo = veiculo
        self.data_saida = data_saida
        self.cliente = cliente
        self.desconto = desconto

    def __str__(self):
        return f'''
        Data que o veículo entrou: {self.data_entrada}
        Data que o veículo saiu: {self.data_saida}
        Desconto aplicado: {self.desconto}

        Descrição do veículo: 
        {self.veiculo}
        Dados do cliente:
        {self.cliente}
        '''

class Veiculo():
    def __init__(self, placa, cor):
        self.placa = placa
        self.cor = cor

    def __str__(self):
        return f'''{self.placa}
            cor: {self.cor}'''
        
class Moto(Veiculo): #Sendo "Moto", filho de "Veiculo".
    def __init__(self, placa, cor):
        super().__init__(placa, cor) #Herda apenas placa e cor (no exercício não foi pedido que adicionasse a diferenciação por cilindradas).

    def __str__(self):
        return f'''{super().__str__()}
        '''
#Classes com herança:

class VeiculoComPassageiro(Veiculo): #Sendo "VeiculoComPassageiro", filho de "Veiculo".
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor) #Herda placa e cor, e por ter passageiros é adicionado "lugares".
        self.lugares = lugares

    def __str__(self):
        return f'''{super().__str__()}
            lugares do veículo: {self.lugares}'''
        
class Carro(VeiculoComPassageiro): #Sendo "Carro", filho de "VeiculoComPassageiro".
    def __init__(self, placa, lugares, cor, portas):
        super().__init__(placa, cor, lugares) #Herda placa, cor, e lugares.Por ter diferenciação de portas, "portas" é adicionado.
        self.portas = portas

    def __str__(self):
        return f'''placa: {super().__str__()}
            portas do veículo: {self.portas}'''

class Onibus(VeiculoComPassageiro): #Sendo "Carro", filho de "VeiculoComPassageiro".
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor, lugares) #Herda placa, cor, e lugares.

    def __str__(self):
        return f'''placa: {super().__str__()}'''

#teste de classes:
pess = Pessoa("João", "(47)123456", "28/01/2010")
pess1 = Pessoa("Mario", "(47)654321", "02/12/2009")
mec = Mecanico(pess1) #Mecânico é uma pessoa.
cli = Cliente(pess, "joaoo@gmail.com") #Cliente é uma pessoa + email desta.
vei = Carro("AAAAAAAA", 5, "azul", 4) #Lembrar que carro é um veículo, ou que "vei" é igual a "Carro(...)".
ser = Servico("troca de pneu", f"R${250}")
serre = Servico_realizado(ser, mec) #O serviço é realizado ao ter um mecânico designado e um "tipo" de serviço.
ord_ser = Ordem_servico("31/03/2026", vei, "01/04/2026", cli, f"{20}%")

print(f"{serre} {ord_ser}")

#Implementar soma de valores e dscontos (com tabela de registros?).