class Pessoa():
    def __init__(self, nm, telef, dt_nasc):
        self.nome = nm
        self.telefone = telef
        self.data_nascimento = dt_nasc

    def __str__(self):
        return f'''
        Nome: {self.nome}
        Telefone: {self.nome}
        Data de Nascimento: {self.nome}
        '''

class Mecanico():
    def __init__(self, pess):
        self.pessoa =  pess

    def __str__(self):
        return f'''
        {self.pessoa}
        '''

class Cliente():
    def __init__(self, pess, em):
        self.pessoa = pess
        self.email = em

    def __str__(self):
        return f'''
        {self.pessoa}
        e-mail: {self.email}
        '''
        
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
        Descrição do veículo: {self.veiculo}
        Data que o veículo saiu: {self.data_saida}
        {self.cliente}
        Desconto aplicado: {self.desconto}
        '''
        
class Veiculo():
    def __init__(self, placa, cor):
        self.placa = placa
        self.cor = cor

    def __str__(self):
        return f'''
        Placa: {self.placa}
        Cor: {self.cor}
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
        Quantidade de lugares do veículo: {self.lugares}
        '''
        
class Carro(VeiculoComPassageiro):
    def __init__(self, placa, cor, lugares, portas):
        super().__init__(placa, cor, lugares)
        self.portas = portas

    def __str__(self):
        return f'''
        {super().__str__()}
        Quantidade de portas do veículo: {self.portas}
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
cli1 = Cliente(pess1, "joaoo@gmail.com")
car1 = Carro("ABCD-1234", "azul", 5, 4)
vei1 = Veiculo(car1)
ser1 = Servico("troca de pneu", "R$250")
serre1 = Servico_realizado(ser1, mec1)
ord_ser = Ordem_servico("25/04/2026", vei1, "26/04/2026", cli1, 20)

print(ord_ser)