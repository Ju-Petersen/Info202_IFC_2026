#classe 1
class Receita:
    def __init__(self, nm, tmp_pr, md_pr, ingr):
        self.nome = nm
        self.tempo_preparo = tmp_pr
        self.modo_preparo = md_pr
        self.ingredientes = ingr
    #definição p/ print de variável com str
    def __str__(self):
        ing = ""
        #"for ... in self.parametro" força o artributo dos ingredientes a ser str p/ o print
        for ings in self.ingredientes:
            ing += str(ings)

        return f'''
Receita: {self.nome}

Tempo de preparo: {self.tempo_preparo} min

Ingredientes: 
{ing}

Modo de preparo:
{self.modo_preparo}
                '''
#classe 2
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
i1 = Ingredientes("Cogumelo", 1, "unidade")
i2 = Ingredientes("Miojo", 1, "pacote")
#ingredientes da receita 2:
i3= Ingredientes("Milho", 1, "lata")
i4= Ingredientes("Leite", 1, "xícara")
i5= Ingredientes("Açúcar", 1, "xícara")
i6= Ingredientes("Ovos", 3, "unidades")
i7= Ingredientes("Óleo", 0.5, "xícara")
i8= Ingredientes("Fermento", 1, "colher chá")
i9= Ingredientes("Farinha", 2, "xícara")
#ingredientes da receita 3:
i10= Ingredientes("Óleo", 0.75, "xícara")
i11= Ingredientes("Açúcar", 2, "xícaras")
i12= Ingredientes("Sal", 2, "pitadas")
i13= Ingredientes("Cenoura", 3, "unidades")
i14= Ingredientes("Farinha", 2, "xícaras")
i15= Ingredientes("Ovos", 4, "unidades de")
i16= Ingredientes("Fermento", 1, "colher chá")
i17= Ingredientes("Leite", 0.5, "xícara")

r1_ing = [i1, i2]
r2_ing = [i3, i4, i5, i6, i7, i8, i9]
r3_ing = [i10, i11, i12, i13, i14, i15, i16, i17]

#variável = nome_da_classe(parâmetro1, parâmetro2, ...)
r1 = Receita("Mario", 50, '''
1-Pegue um cogumelo
2-Queime ele e grite tres vezes mario
3- coma um miojo da nitendo''', r1_ing)

r2 = Receita("Bolo de Milho", 60,
              '''
Bater tudo no liquidificador e colocar no forno''', r2_ing)

r3 = Receita("Bolo de Cenoura", 60, 
'''
    1 - Em um liquidificador bata o leite e cenoura;

    2 - Em seguida, adicione os ovos, açúcar, óleo e bata novamente;

    3 - Adicione a farinha aos poucos enquanto bate a massa até ficar homogênea;

    4 - Por fim adicione o sal e fermento, misture;

    5 - Em uma forma untada despeje a massa e leve ao forno pré-aquecido a 200°C por 40 minutos, ou até a massa dourar;

    6 - Desenforme (caso desejado) e sirva!''', r3_ing)
#prints separados para que cada receita seja visualizada em baixo da outra
print(r1)
print(r2)
print(r3)

#Implementar lista que mostra apenas os ingredientes necessários para as 3 receitas em uma tabela(dicionário):
rs = [r1, r2, r3]
tabela = {}

for rec in rs:
    for ing in rec.ingredientes:
        nm_ing = f"{ing.nome} {ing.unidade}"
        #Utilizar "nome" como chave
        if nm_ing in tabela:
            tabela[nm_ing] += ing.quantidade
        else:
            tabela[nm_ing] = ing.quantidade
            #Lembrete ao adicionar itens em dict: colocar o equivalente "nome_tabela[chave]"

'''
    Tentativa de uso de lst_ing para o print em forma de lista e não duplicar os ingredientes:(falha)

    lst_ing.append(ing)
        for a in lst_ing:
            print(f"{tabela[a].quantidade}")
'''
#Print em forma de lista:
for ingrs in tabela:
    print(f"{ingrs}: {tabela[ingrs]}")
#Print da tabela em si:
'''print(tabela)'''

Implementar soma de tempo:
for a in rs:
    tp = a.tempo_preparo
    #Se já estiv#er passado pela posição 0 [r1] somar o tempo de preparo salvo(r1) com o tempo de preparo da posição 1 [r2]
    if rs[0] != rs[0]:
        tempo_total += tp

        print(tempo_total)