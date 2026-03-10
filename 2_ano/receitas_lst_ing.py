class Receita:
    def __init__(self, nm, tmp_pr, md_pr, ingr):
        self.nome = nm
        self.tempo_preparo = tmp_pr
        self.modo_preparo = md_pr
        self.ingredientes = ingr
    def __str__(self):
        ing = ""
        for ings in self.ingredientes:
            ing = ing + str(ings)
        x= f'''
Receita: {self.nome}
Tempo de preparo: {self.tempo_preparo} min
ingredientes: {ing}
modo de preparo:
{self.modo_preparo}
                '''
        return x

class Ingredientes:
    def __init__(self, nm, quant, uni):
        self.nome = nm
        self.quantidade = quant
        self.unidade = uni
    
    def __str__(self):
        return f'''
{self.quantidade} {self.unidade} {self.nome}'''

ing1 = Ingredientes("Cogumelo", 1, "unidade de")
ing2 = Ingredientes("Miojo", 1, "pacote de")

r_ing = [ing1, ing2]

r1 = Receita("Mario", 50, ' 1-Pegue um cogumelo, 2-Queime ele e grite tres vezes mario, 3- coma um miojo da nitendo', r_ing)
print(r1)