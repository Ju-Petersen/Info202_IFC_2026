class Receita:
    def __init__(self, nm, tmp_pr, md_pr, ingr):
        self.nome = nm
        self.tempo_preparo = tmp_pr
        self.modo_preparo = md_pr
        self.ingredientes = ingr
    #definição p/ print de variável com str
    def __str__(self):
        ing = ""
        #"for ... in self.parametro" percorre os objetos da classe colocada como artributo de outra classe
        for ings in self.ingredientes:
            ing = ing + str(ings)
        #"x" é a variável que guarda o print para retornar os dados em str
        x= f'''
Receita: {self.nome}

Tempo de preparo: {self.tempo_preparo} min

Ingredientes: 
{ing}

Modo de preparo:
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

#teste classe ----------------------------------------------------------------------------------------

#ingredientes da receita1:
i1 = Ingredientes("Cogumelo", 1, "unidade de")
i2 = Ingredientes("Miojo", 1, "pacote de")
#ingredientes da receita 2:
i3= Ingredientes("Milho", 1, "lata (milho)")
i4= Ingredientes("Leite", 1, "lata (milho)")
i5= Ingredientes("Açúcar", 1, "lata (milho)")
i6= Ingredientes("Ovos", 3, "unidade")
i7= Ingredientes("Óleo", 0.5, "lata (milho)")
i8= Ingredientes("Fermento", 1, "colher de chá")
#ingredientes da receita 3:
i9= Ingredientes("Margarina", 6, "colheres de sopa")
i10= Ingredientes("Chocolate em pó", 0.5, "xícara de")
i11= Ingredientes("Açúcar", 2, "xícaras de")
i12= Ingredientes("Sal", 2, "pitadas de")
i13= Ingredientes("Chocolate meio amargo", 1, "tablete")
i14= Ingredientes("Achocolatado", 0.75, "xícara de")
i15= Ingredientes("Farinha de trigo", 1.25, "xícaras de")
i16= Ingredientes("Ovos", 4, "unidades de")
i17= Ingredientes("Essência de baunilha", 1, "colher de chá")
i18= Ingredientes("Nozes picadas", 0.5, "xícara de")

r1_ing = [i1, i2]
r2_ing = [i3, i4, i5, i6, i7, i8]
r3_ing = [i9, i10, i11, i12, i13, i14, i15, i16, i17, i18]

#variável = nome_da_classe(parâmetro1, parâmetro2, ...)
r1 = Receita("Mario", 50, '''
1-Pegue um cogumelo
2-Queime ele e grite tres vezes mario
3- coma um miojo da nitendo''', r1_ing)
r2 = Receita("Bolo de Milho", 50,
              '''
Bater tudo no liquidificador e colocar no forno''', r2_ing)
r3 = Receita("Brownie", 40, 
'''
    1 - Misture os ovos e o açúcar.

    2 - Em seguida, agregue todos os outros ingredientes até formar um creme uniforme.

    3 - Despeje em uma assadeira, forrada com papel-manteiga e leve ao forno médio por 40 minutos.

    4 - O brownie estará pronto quando a parte de cima estiver levemente corada e, ao se espetar um palito, ele esteja levemente úmido (devido ao chocolate derretido).

    5 - Corte em quadrados ainda quente e sirva com uma bola de sorvete de creme, ou congele num saquinho para freezer.

    6 - Para descongelar, coloque o brownie num prato de sobremesa e aqueça no micro-ondas, potência alta, por 1 minuto''', r3_ing)
#prints separados para que cada receita seja visualizada em baixo da outra
#print(r1)
#print(r2)
#print(r3)

#Implementar lista que mostra apenas os ingredientes necessários para as 3 receitas em uma tabela(dicionário):
rs = [r1, r2, r3]
tabela = {}

for r in rs:
    for ing in r.ingredientes:
        if ing in tabela:
            ing = f"{ing.nome}, {ing.quantidade}"
            tabela[ing] += ing.quantidade
            #Lembrete ao adicionar itens em dict: colocar o equivalente ("nome_tabela[variável/dado]")
        else:
            ing = f"{ing.nome}, {ing.quantidade}"
            tabela[ing] += ing

    print(tabela[ing])