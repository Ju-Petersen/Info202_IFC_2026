class Receita:
    def __init__(self, nome, tempo_preparo, modo_preparo):
        self.nome = nome
        self.tempo_preparo = tempo_preparo
        self.modo_preparo = modo_preparo
    # como expressar uma receita em formato textual (modo __str__)
    def __str__(self):
        return f'''
        Receita: {self.nome}
        Tempo de preparo: {self.tempo_preparo} minutos
        Modo de preparo: {self.modo_preparo}
        '''

class Ingrediente:
    def __init__(self,nome):
        self.nome=nome

class IngredienteDaReceita:
    def __init__(self, receita, ingrediente, quantidade, unidade):
        self.receita = receita
        self.ingrediente = ingrediente
        self.quantidade = quantidade
        self.unidade = unidade

# teste da classe
r1 = Receita("Bolo de Milho", 50,
              "Bater tudo no liquidificador e colocar no forno")    

i1= Ingrediente("Milho")
i2= Ingrediente("Leite")
i3= Ingrediente("Açúcar")
i4= Ingrediente("Ovos")
i5= Ingrediente("Óleo")
i6= Ingrediente("Fermento")

ir1 = IngredienteDaReceita(r1, i1, 1, "lata")
ir2 = IngredienteDaReceita(r1, i2, 1, "lata")
ir3 = IngredienteDaReceita(r1, i3, 1, "lata")
ir4 = IngredienteDaReceita(r1, i4, 3, "unidade")
ir5 = IngredienteDaReceita(r1, i5, 0.5, "lata")
ir6 = IngredienteDaReceita(r1, i6, 1, "colher de chá")

r2 = Receita("Brownie", 40, 
'''
    1 - Misture os ovos e o açúcar.

    2 - Em seguida, agregue todos os outros ingredientes até formar um creme uniforme.

    3 - Despeje em uma assadeira, forrada com papel-manteiga e leve ao forno médio por 40 minutos.

    4 - O brownie estará pronto quando a parte de cima estiver levemente corada e, ao se espetar um palito, ele esteja levemente úmido (devido ao chocolate derretido).

    5 - Corte em quadrados ainda quente e sirva com uma bola de sorvete de creme, ou congele num saquinho para freezer.

    6 - Para descongelar, coloque o brownie num prato de sobremesa e aqueça no micro-ondas, potência alta, por 1 minuto''')

i7= Ingrediente("margarina")
i8= Ingrediente("mhocolate em pó")
i9= Ingrediente("açúcar")
i10= Ingrediente("sal")
i11= Ingrediente("chocolate meio amargo")
i12= Ingrediente("achocolatado")
i13= Ingrediente("farinha de trigo")
i14= Ingrediente("ovos")
i15= Ingrediente("essência de baunilha")
i16= Ingrediente("nozes picadas")

ir7 = IngredienteDaReceita(r2, i7, 6, "colheres de sopa")
ir8 = IngredienteDaReceita(r2, i8, 0.5, "xícara de")
ir9 = IngredienteDaReceita(r2, i8, 2, "xícaras de")
ir10 = IngredienteDaReceita(r2, i9, 2, "pitadas de")
ir11 = IngredienteDaReceita(r2, i10, 1, "tablete")
ir12 = IngredienteDaReceita(r2, i11, 0.75, "xícara de")
ir13 = IngredienteDaReceita(r2, i12, 1.25, "xícaras de")
ir14 = IngredienteDaReceita(r2, i13, 4, "unidades de")
ir15 = IngredienteDaReceita(r2, i14, 1, "colher de chá")
ir16 = IngredienteDaReceita(r2, i15, 0.5, "xícara de")

ir1s = [ir1, ir2, ir3, ir4, ir5, ir6]
ir2s = [ir7, ir8, ir9, ir10, ir11, ir12, ir13, ir14, ir15, ir16]
print(r1)
# .nome, r1.tempo_preparo, r1.modo_preparo)
#print(ir1, ir2, ir3, ir4, ir5, ir6)

for ir in ir1s:
    print(ir.quantidade, ir.unidade, ir.ingrediente.nome)

print(r2)

for i in ir2s:
    print(i.quantidade, i.unidade, i.ingrediente.nome)