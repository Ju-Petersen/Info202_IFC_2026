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
    def __init__(self, desc, val):
        self.descricao = desc
        self.valor = val

    def __str__(self):
        return f'''
        Descrição do serviço: {self.descricao}
        Valor: {self.valor}
        '''
        
class Servico_realizado():
    def __init__(self, ser, mec, ord_ser):
        self.servico = ser
        self.mecanico = mec
        self.ordem_servico = ord_ser

    def __str__(self):
        return f'''
        {self.ordem_servico}
        {self.servico}
        Realizado por:
        {self.mecanico}
        '''
        
class Ordem_servico():
    def __init__(self, dt_ent, vei, dt_sai, cli, desc):
        self.data_entrada = dt_ent
        self.veiculo = vei
        self.data_saida = dt_sai
        self.cliente = cli
        self.desconto = desc

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
    def __init__(self, pl, cor):
        self.placa = pl
        self.cor = cor

    def __str__(self):
        return f'''{self.placa}
            cor: {self.cor}'''
        
class Moto(Veiculo): #Sendo "Moto", filho de "Veiculo".
    def __init__(self, pl, cor):
        super().__init__(pl, cor) #Herda apenas placa e cor (no exercício não foi pedido que adicionasse a diferenciação por cilindradas).

    def __str__(self):
        return f'''{super().__str__()}
        '''
#Classes com herança:

class VeiculoComPassageiro(Veiculo): #Sendo "VeiculoComPassageiro", filho de "Veiculo".
    def __init__(self, pl, cor, lug):
        super().__init__(pl, cor) #Herda placa e cor, e por ter passageiros é adicionado "lugares".
        self.lugares = lug

    def __str__(self):
        return f'''{super().__str__()}
            lugares do veículo: {self.lugares}'''
        
class Carro(VeiculoComPassageiro): #Sendo "Carro", filho de "VeiculoComPassageiro".
    def __init__(self, pl, lug, cor, por):
        super().__init__(pl, cor, lug) #Herda placa, cor, e lugares.Por ter diferenciação de portas, "portas" é adicionado.
        self.portas = por

    def __str__(self):
        return f'''placa: {super().__str__()}
            portas do veículo: {self.portas}'''

class Onibus(VeiculoComPassageiro): #Sendo "Carro", filho de "VeiculoComPassageiro".
    def __init__(self, pl, cor, lug):
        super().__init__(pl, cor, lug) #Herda placa, cor, e lugares.

    def __str__(self):
        return f'''placa: {super().__str__()}'''

#teste de classes (feito em test_oficina_mecanica):

pess = Pessoa("João", "(47)123456", "28/01/2010")
pess1 = Pessoa("Mario", "(47)654321", "02/12/2009")
mec = Mecanico(pess1) #Mecânico é uma pessoa!!
cli = Cliente(pess, "joaoo@gmail.com") #Cliente é uma pessoa + email desta.
vei = Carro("AAAAAAAA", 5, "azul", 4) #Lembrar que carro é um veículo, ou que "vei" é igual a "Carro(...)".
ser = Servico("troca de pneu", f"R${250}")
ord_ser1 = Ordem_servico("31/03/2026", vei, "01/04/2026", cli, f"{20}%")
serre = Servico_realizado(ser, mec, ord_ser1) #O serviço é realizado ao ter um mecânico designado e um "tipo" de serviço.

print(serre)

#Implementar soma de valores e dscontos (com tabela de registros?).

