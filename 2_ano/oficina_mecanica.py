class Pessoa():
    def __init__(self, nome, telefone, data_nascimento):
        self.nome = nome
        self.telefone = telefone
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f'''
        '''

class Mecanico():
    def __init__(self, pessoa):
        self.pessoa =  pessoa

    def __str__(self):
        return f'''
        '''

class Cliente():
    def __init__(self, pessoa, email):
        self.pessoa = pessoa
        self.email = email

    def __str__(self):
        return f'''
        '''
        
class Servico():
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f'''
        '''
        
class Servico_realizado():
    def __init__(self, servico, mecanico):
        self.servico = servico
        self.mecanico = mecanico

    def __str__(self):
        return f'''
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
        '''
        
class Veiculo():
    def __init__(self, placa, cor):
        self.placa = placa
        self.cor = cor

    def __str__(self):
        return f'''
        '''
        
class Moto(Veiculo):
    def __init__(self, placa, cor):
        super().__init__(placa, cor)

    def __str__(self):
        return f'''
        {super().__str__()}
        '''

class VeiculoComPassageiro(Veiculo):
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor)
        self.lugares = lugares

    def __str__(self):
        return f'''
        {super().__str__()}
        '''
        
class Carro(VeiculoComPassageiro):
    def __init__(self, placa, cor, lugares, portas):
        super().__init__(placa, cor, lugares)
        self.portas = portas

    def __str__(self):
        return f'''
        {super().__str__()}
        '''

class Onibus(VeiculoComPassageiro):
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor, lugares)

    def __str__(self):
        return f'''
        {super().__str__()}
        '''
        
pess1 = Pessoa("João", "(47)123456", "28/01/2010")
pess2 = Pessoa("Mario", "(47)654321", "02/12/2009")
mec1 = Mecanico(pess2)
cli1 = Cliente(pess1, "joao.joao@gmail.com")
car1 = Carro("ythh-4534634", "cor", 5, 4)
mot1 = Moto("gfhfg-2353456435474356", "preto")
vei1 = Veiculo(mot1)
vei2 = Veiculo(car1)
ser1 = Servico("troca de pneu", "R$250")
serre1 = Servico_realizado(ser1, mec1)
ord_ser = Ordem_servico("25/04/2026", vei2, "26/04/2026", cli1, 20)

print(ord_ser)