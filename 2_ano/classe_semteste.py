class Receita:
    def __init__(self, nm_rec, tp_prep, md_prep, ings):
        self.nome_receita = nm_rec
        self.tempo_preparo = tp_prep
        self.modo_preparo = md_prep
        self.ingredientes = ings

    #expressar em str
    def __str__(self):
        ing = ""
        for ings in self.ingredientes:
            ing += str(ings)

        return f'''
        {self.nome_receita}
        Tempo de Preparo: {self.tempo_preparo}
        Modo de Preparo: {self.modo_preparo}
        Ingredientes: {ing}'''
#O Ingredientes: {ing} deve retornar a classe Ingredientes forçando-a em string para o print

class Ingredientes:
    def __init__(self, nm, uni, quant):
        self.nome = nm
        self.unidade = uni
        self.quantidade = quant

    def __str__(self):
        return f'''
        - {self.quantidade} {self.unidade} de {self.nome}'''

r1 = Receita
r2 = Receita
r3 = Receita
r4 = Receita

rs = [r1, r2, r3, r4]
tab_ings = {}

for rec in rs:
    for ingr in rec.ingredientes: #<<<<<<<<< OBJETO INGREDIENTE -> LISTA INGREDIENTES!!!
        nm_ingr = f"{ingr.nome} {ingr.unidade}" #<<<<<<<< EXPRESSAR NOME E UNIDADE EM UMA VARIÁVEL QUE É CONCATENADA COM QUANTIDADE!!!
        if nm_ingr in tab_ings:
            tab_ings[nm_ingr] += ingr.quantidade #<<<<<<<< NOME COMO CHAVE!!!
        else:
            tab_ings[nm_ingr] = ingr.quantidade #<<<<<<<< NOME COMO CHAVE!!!

print(f'''
Lista dos ingredientes para fazer todas as receitas:
      ''')
for a in tab_ings: #Para cada ingrediente:
    print(f" - {a}: {tab_ings[a]}")