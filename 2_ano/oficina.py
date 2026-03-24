#Registrar as ordens de serviço que ocorrem em uma oficina mecânica

class Cliente: #classe que registra o cliente
    def __init__(self, nm, em, telef, vei):
        self.nome = nm
        self.email = em
        self.telefone = telef
        self.veiculo = vei

    def __str__(self): #expressar em string
        return f'''
{self.nome}
{self.email}
{self.telefone}
{self.veiculo}
'''

class Servico: #classe que registra os dados do serviço
    def __init__(self, vei, tp_ser, val, nm_mec):
        self.veiculo = vei
        self.tipo_servico = tp_ser
        self.valor = val
        self.mecanico = nm_mec

    def __str__(self): #expressar em string
        return f'''
{self.veiculo}
{self.tipo_servico}
{self.valor}
{self.mecanico}
'''

class Ordem_Servico: #classe que registra qual cliente e veiculo foi atendido
    def __init__(self, cli, vei, dt_ent, dt_sai, desc):
        self.cliente = cli
        self.veiculo = vei
        self.data_entrada = dt_ent
        self.data_saida = dt_sai
        self.desconto = desc

    def __str__(self): #expressar em string
        return f'''
{self.cliente}
{self.veiculo}
{self.data_entrada}
{self.data_saida}
{self.desconto}
'''

class Veiculo: #classe que registra veículos
    def __init__(self, tp, pl, cor):
        self.tipo = tp #Se for carro, identificar portas. Se for ônibus identificar lugares (usar 'for' e 'if'?)
        self.placa = pl
        self.cor = cor

'''
v = "vnjfdnvb"
v2 = "abcdefgh"
c1 = Cliente("A", "A@email", "123456789", v)
c2 = Cliente("B", "B@email", "987654321", v2)
servico1 = Servico(v2, "Limpeza", f"R${50.00}", "Ronaldão")
ordem_servico1 = Ordem_Servico(c2, v2, "00/00/00", "00/00/00", "fazer somatoria de desconto")'''

print("temporario")