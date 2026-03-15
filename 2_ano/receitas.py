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
            ing = str(ings)

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
    
#teste classes:

#Ingredientes:

i1 = Ingredientes("Ovos", "unidade(s)", 3)
i2 = Ingredientes("Leite", "xícara(s)", 0.5)
i3 = Ingredientes("Farinha de Trigo", "xícara(s)", 2)
i4 = Ingredientes("Cenoura", "unidade(s)", 2)
i5 = Ingredientes("Açúcar", "xícara(s)", 1)
i6 = Ingredientes("Fermento", "colher(es) (chá)", 1)
i7 = Ingredientes("Óleo de Soja", "colher(es) (sopa)", 2)
r1_ing = [i1, i2, i3, i4, i5, i6, i7]

#receita1
r1 = Receita("Bolo de Cenoura", 50, '''
1 - Descasque a cenoura e corte-a em cubos;
2 - Em um liquidificador, misture a cenoura com o leite e óleo;
3 - Adicione os ovos e açúcar, misture  até a mistura se tornar homogênea;
4 - Com o liquidificador em velocidade baixa adicione a farinha aos poucos;
5 - Por fim misture o fermento;
6 - Despeje a massa em uma forma de sua preferência untada com óleo e leve ao forno pré aquecido a 250°C por 40 minutos até a parte superior dourar;
''', r1_ing)