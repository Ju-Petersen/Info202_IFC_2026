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
#Teste classes:

#Ingredientes r1:
i1 = Ingredientes("Ovos", "unidade(s)", 3)
i2 = Ingredientes("Leite", "xícara(s)", 0.5)
i3 = Ingredientes("Farinha de Trigo", "xícara(s)", 2)
i4 = Ingredientes("Cenoura", "unidade(s)", 2)
i5 = Ingredientes("Açúcar", "xícara(s)", 1)
i6 = Ingredientes("Fermento", "colher(es) (chá)", 1)
i7 = Ingredientes("Óleo de Soja", "colher(es) (sopa)", 2)
r1_ing = [i1, i2, i3, i4, i5, i6, i7]

#Ingredientes r2:
i8 = Ingredientes("Leite Condensado", "grama(s)", 250)
i9 = Ingredientes("Gelatina Incolor", "folha(s)", 8)
i10 = Ingredientes("Bolacha de Amido de Milho", "pacote(s)", 1)
i11 = Ingredientes("Doce de morango", "grama(s)", 500)
i12 = Ingredientes("Nata", "grama(s)", 200)
i13 = Ingredientes("Cream Cheese", "grama(s)", 200)
i14 = Ingredientes("Margarina (sem sal)", "colher(es) (sopa)", 6)
r2_ing = [i8, i9, i10, i11, i12, i13, i14]

#Ingredientes r3:
i15 = Ingredientes("Chocolate", "barra(s)", 1)
i16 = Ingredientes("Margarina (sem sal)", "colher(es) (sopa)", 2)
i17 = Ingredientes("Farinha de Trigo", "colher(es) (sopa)", 2)
i18 = Ingredientes("Gemas", "unidade(s)", 2)
i19 = Ingredientes("Ovos", "unidade(s)", 2)
r3_ing = [i15, i16, i17, i18, i19]

#Ingredientes r4:
i20 = Ingredientes("Bolacha de Amido de Milho", "pacote(s)", 3)
i21 = Ingredientes("Leite Condensado", "grama(s)", 250)
i22 = Ingredientes("Creme de Leite", "grama(s)", 200)
i23 = Ingredientes("Doce de Leite", "grama(s)", 500)
i24 = Ingredientes("Leite", "xícara(s)", 0.25)
i25 = Ingredientes("Chocolate Meio Amargo", "barra(s)", 2)
r4_ing = [i21, i22, i23, i24, i25]

#receita1
r1 = Receita("Bolo de Cenoura", 50, '''
        1 - Descasque a cenoura e corte-a em cubos;
        2 - Em um liquidificador, misture a cenoura com o leite e óleo;
        3 - Adicione os ovos e açúcar, misture  até a mistura se tornar homogênea;
        4 - Com o liquidificador em velocidade baixa adicione a farinha aos poucos;
        5 - Por fim misture o fermento;
        6 - Despeje a massa em uma forma de sua preferência untada com óleo e leve ao forno pré aquecido a 250°C por 40 minutos até a parte superior dourar;
''', r1_ing)

print(r1)

#receita2:
r2 = Receita("Cheesecake", 10, '''
        1 - Triture as bolachas e junte a margarina derretida, mexa bem e coloque no fundo de uma tarteira. Leve à geladeira enquanto prepara o creme.
        2 - Demolhe as folhas de gelatina e derreta em 100 ml de leite.
        3 - Bata as natas em chantilly e reserve.
        4 - Bata o queijo uns segundos com o leite condensado e junte as natas, adicione a gelatina derretida e deite sobre a base de bolacha.
        5 - Leve à geladeira para endurecer.
        6 - Retire e espalhe por cima o doce de morango, leve de novo ao frigorífico e sirva bem fresco.
''', r2_ing)

print(r2)

#receita3:
r3 = Receita("Petit Gateu", 30, '''
        1 - Derreta a manteiga e o chocolate em banho-maria.
        2 - Bata os ovos e as gemas com açúcar na batedeira, até ficar bem claro.
        3 - Junte o chocolate derretido e a farinha de trigo, misturando com uma espátula.
        4 - Depois, unte as forminhas de empadinha, passe farinha de trigo e coloque a massa.
        5 - Preaqueça o forno e leve para assar de 6 a 10 minutos (em fogo alto) até os bolinhos crescerem, mas o meio deve ficar molinho.
        6 - Deve-se desenformar ainda quente.
        7 - Sirva diretamente no prato, acompanhado com sorvete de creme.
''', r3_ing)

print(r3)

#receita4:
r4 = Receita("Torta de Bolacha", 30, '''
        1 - Em uma travessa, adicione o Doce de Leite, Leite Condensado, 100 gramas do Creme de Leite e misture-os (colher ou batedeira);
        2 - Caso a misture fique muito densa adicione um pouco do Leite;
        3 - Em uma travessa retângular ou oval pegue com uma concha parte da mistura e espalhe pelo fundo da travessa;
        4 - Em dois pratos reservados despeje o Leite e a Bolacha (separados);
        5 - Molhe as bolachas por inteiro no leite e faça uma camada destas;
        6 - Alterne entre uma camada da mistura e uma de bolachas até ter a quantidade desejada na travessa;
        7 - Dereta o chocolate no microondas;
        9 - Adicione 100 gramas de Creme de Leite ao chocolate e misture;
        10 - Despeje a ganache na última camada da torta e leve a geladeira (de preferência coberta com tampa ou plástico filme)  até a ganache firmar (se preferir deixe na geladeira de um diapara o outro);
''', r4_ing)

print(r4)

#Implementação Lista de Ingredientes:

rs = [r1, r2, r3, r4]
tab_ings = {}

#Encontrar x receita em lista de receitas:
for rec in rs:
    #Encontrar Ingredientes da x receita:
    for ingr in rec.ingredientes: #<<<<<<<<< OBJETO INGREDIENTE -> LISTA INGREDIENTES!!!
        #Variável que funciona como chave para nome e unidade do ingr:
        nm_ingr = f"{ingr.nome} {ingr.unidade}" #<<<<<<<< EXPRESSAR NOME E UNIDADE EM UMA VARIÁVEL QUE É CONCATENADA COM QUANTIDADE!!!
        #Se x ingrediente estiver na receita x e não na tabela:
        if nm_ingr in tab_ings:
            #Adicionar ingrediente na tabela.
            tab_ings[nm_ingr] += ingr.quantidade #<<<<<<<< NOME COMO CHAVE!!!
        else:
            #Somar a quantidade dos ingredientes iguais:
            tab_ings[nm_ingr] = ingr.quantidade #<<<<<<<< NOME COMO CHAVE!!!

#Em forma de lista:
print(f'''
Lista dos ingredientes para fazer todas as receitas:
      ''')
for a in tab_ings: #Para cada ingrediente:
    print(f" - {a}: {tab_ings[a]}") 
    #Print do nome do Ingrediente (a) e a quantidade somada e concatenada (tab_ings[a], sendo "a" para a quantidade daquele ingrediente em específico)