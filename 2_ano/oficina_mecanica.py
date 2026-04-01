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
        Descrição do veículo: 
        {self.veiculo}
        Data que o veículo saiu: {self.data_saida}

        Dados do cliente:
        {self.cliente}
        Desconto aplicado: {self.desconto}
        '''
        
class Veiculo():
    def __init__(self, placa, cor):
        self.placa = placa
        self.cor = cor

    def __str__(self):
        return f'''{self.placa}
        cor: {self.cor}'''
        
class Moto(Veiculo):
    def __init__(self, placa, cor):
        super().__init__(placa, cor)

    def __str__(self):
        return f'''{super().__str__()}
        '''

class VeiculoComPassageiro(Veiculo):
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor)
        self.lugares = lugares

    def __str__(self):
        return f'''{super().__str__()}
        lugares do veículo: {self.lugares}'''
        
class Carro(VeiculoComPassageiro):
    def __init__(self, placa, lugares, cor, portas):
        super().__init__(placa, cor, lugares)
        self.portas = portas

    def __str__(self):
        return f'''placa: {super().__str__()}
        portas do veículo: {self.portas}'''

class Onibus(VeiculoComPassageiro):
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor, lugares)

    def __str__(self):
        return f'''placa: {super().__str__()}'''
        
pess = Pessoa("João", "(47)123456", "28/01/2010")
pess1 = Pessoa("Mario", "(47)654321", "02/12/2009")
mec = Mecanico(pess1)
cli = Cliente(pess, "joaoo@gmail.com")
vei = Carro("AAAAAAAA", 5, "azul", 4)
ser = Servico("troca de pneu", "R$250")
serre = Servico_realizado(ser, mec)
ord_ser = Ordem_servico("01/04/2026", vei, "26/04/2026", cli, 20)

print(ord_ser)