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
        Modo de Preparo: 
        {self.modo_preparo}
        Ingredientes:
        {ing}
'''
#O Ingredientes: {ing} deve retornar a classe Ingredientes forçando-a em string para o print

class Ingredientes:
    def __init__(self, nm, uni, quant):
        self.nome = nm
        self.unidade = uni
        self.quantidade = quant

    def __str__(self):
        return f'''
        {self.quantidade} {self.unidade} de {self.nome}
'''
#Teste classes:

r1 = Receita()
r2 = Receita()
r3 = Receita()
r4 = Receita()

#Implementação Lista de Ingredientes:

rs = [r1, r2, r3, r4]
tab_ings = {}