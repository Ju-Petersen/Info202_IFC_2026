import datetime

class Cliente:
    def __init__(self, nm: str, dt_nasc: datetime, cpf: StopIteration):
        self.nome = nm
        self.data_nascimento = dt_nasc
        self.cpf = cpf

    def __str__(self):
        return f'''
        Nome: {self.nome}
        Data de Nascimento: {self.data_nascimento}
        CPF: {self.cpf}'''

class Item_pedido:
    def __init__(self, pr: Prato, val_pr: float, qtd: int):
        self.prato = pr
        self.valor_prato = val_pr
        self.quantidade = qtd

    def __str__(self):
        return f'''
        Prato: {self.prato}
        Valor do prato: {self.valor_prato}
        Quantidade: {self.quantidade}'''
        
class Prato:
    def __init__(self, nm: str, ing: list[str], md_prep: str, pre: float):
        self.nome = nm
        self.ingredientes = ing
        self.modo_preparo = md_prep
        self.preco = pre

    def __str__(self):
        return f'''
        Nome: {self.nome}
        Ingredientes: 
        {self.ingredientes}
        Modo de Preparo: 
        {self.modo_preparo}

        Preço: {self.preco}'''

class Pedido:
    def __init__(self, dt: datetime, per: float, cli: Cliente, pr: list[Prato]):
        self.data_pedido = dt
        self.percentual = per
        self.cliente = cli
        self.prato = pr
        self.valor_final = 0
    def calcular_valor(self):
        valor = 0
        for v in self.pratos:
            #para cada valor diferente de um prato:
            valor += v.preco
        #calcular o reajuste por cima do percentual p/ ter "valor_final"
        self.valor_final = valor + (1 * self.percentual / 100)

    def __str__(self):
        return f'''
        {self.data_pedido}
        Desconto: {self.percentual}
        Cliente: {self.cliente}
        Prato: {self.prato}
        Total: {self.valor_final}'''


