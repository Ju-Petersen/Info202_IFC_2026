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
    def __init__(self, dt: datetime, per: float, cli: Cliente, pr: list[Item_pedido]):
        self.data_pedido = dt
        self.percentual = per
        self.cliente = cli
        self.prato = pr
        self.valor_final = 0
    def calcular_valor(self):
        valor = 0
        for v in self.prato:
            #para cada valor diferente de um prato:
            valor += v.valor_prato
            #calcular o reajuste por cima do percentual p/ ter "valor_final"
        valor -= valor * (self.percentual/ 100)
        self.valor_final = valor

    def __str__(self):
        self.calcular_valor()
        pr = ""
        pr1 = ""
        for p in self.prato:
            pr += str(f"{p.prato.nome}, ")
            pr1 += str(f"{p.valor_prato}, ")
        return f'''
        Pedido feito em: {self.data_pedido}
        Desconto: {self.percentual}
        Cliente: {self.cliente}
        Pratos: {pr} Preço: {pr1}
        Total: {self.valor_final}'''

c = Cliente("a", datetime.datetime(1997, 3, 3), "01.123.456-78")
lst_ings = ["macarrão instantâneo", "tempero", "frango", "cebola", "ovo"]
p = Prato("Miojo", lst_ings, "Ferver água, enquanto ferve colocar o macarrão e o tempero em uma panela, colocar a água fervida por cima e esperar até ficar pronto.", 100.0)
p1 = Prato("Miojo1", lst_ings, "Ferver água, enquanto ferve colocar o macarrão, o tempero e o frango em uma panela, colocar a água fervida por cima e esperar até ficar pronto.", 200.0)
p2 = Prato("Miojo2", lst_ings, "Ferver água, enquanto ferve colocar o macarrão, o tempero, a cebola e o ovo em uma panela, colocar a água fervida por cima e esperar até ficar pronto.", 300.0)
item = Item_pedido(p, 100.0, 1)
item1 = Item_pedido(p1, 100.0, 1)
item2 = Item_pedido(p2, 100.0, 1)
lst_itens = [item, item1, item2]
ped = Pedido(datetime.date(2026, 6, 16), 50.0, c, lst_itens)

print(ped)
# A diferença entre os códigos 02 e 03 é basicamente o cálculo do valor de modo que 
# o reajuste fique "salvo", ou seja, caso ocorra o reajuste tanto o valor final será 
# calculado de acordo com este mas o preço unitário do "item_pedido" é salvo
