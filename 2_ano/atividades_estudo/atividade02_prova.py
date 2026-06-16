import datetime

class Cliente:
    def __init__(self, nm: str, dt_nasc: datetime, cpf: str):
        self.nome = nm
        self.data_nascimento = dt_nasc
        self.cpf = cpf

    def __str__(self):
        return f'''{self.nome} de {self.data_nascimento} cpf {self.cpf}'''

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
    def __init__(self, dt: datetime, per: float, val_fn: float, cli: Cliente, pr: list[Prato]):
        self.data_pedido = dt
        self.percentual = per
        self.cliente = cli
        self.prato = pr
        self.valor_final = val_fn

    def __str__(self):
        pr = ""
        pr1 = ""
        for p in self.prato:
            pr += str(f"{p.nome}, ")
            pr1 += str(f"{p.preco}, ")
        return f'''
        {self.data_pedido}
        Desconto: {self.percentual}
        Cliente: {self.cliente}
        Prato: {pr} Preço: {pr1}
        Total: {self.valor_final}'''

c = Cliente("a", datetime.datetime(1997, 3, 3), "01.123.456-78")
lst_ings = ["macarrão instantâneo", "tempero", "frango", "cebola", "ovo"]
p = Prato("Miojo", lst_ings, "Ferver água, enquanto ferve colocar o macarrão e o tempero em uma panela, colocar a água fervida por cima e esperar até ficar pronto.", 100.0)
p1 = Prato("Miojo1", lst_ings, "Ferver água, enquanto ferve colocar o macarrão, o tempero e o frango em uma panela, colocar a água fervida por cima e esperar até ficar pronto.", 200.0)
p2 = Prato("Miojo2", lst_ings, "Ferver água, enquanto ferve colocar o macarrão, o tempero, a cebola e o ovo em uma panela, colocar a água fervida por cima e esperar até ficar pronto.", 300.0)
lst_pratos = [p, p1, p2]
ped = Pedido(datetime.date(2026, 6, 16), 50.0, 50.0, c, lst_pratos)

print(ped)
