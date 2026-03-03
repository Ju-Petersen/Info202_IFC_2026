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

r1 = Receita("Brownie", 40, 
'''
1 - Misture os ovos e o açúcar.

2 - Em seguida, agregue todos os outros ingredientes até formar um creme uniforme.

3 - Despeje em uma assadeira, forrada com papel-manteiga e leve ao forno médio por 40 minutos.

4 - O brownie estará pronto quando a parte de cima estiver levemente corada e, ao se espetar um palito, ele esteja levemente úmido (devido ao chocolate derretido).

5 - Corte em quadrados ainda quente e sirva com uma bola de sorvete de creme, ou congele num saquinho para freezer.

6 - Para descongelar, coloque o brownie num prato de sobremesa e aqueça no micro-ondas, potência alta, por 1 minuto''')

i1= Ingrediente("margarina")
i2= Ingrediente("mhocolate em pó")
i3= Ingrediente("açúcar")
i4= Ingrediente("sal")
i5= Ingrediente("chocolate meio amargo")
i6= Ingrediente("achocolatado")
i7= Ingrediente("farinha de trigo")
i8= Ingrediente("ovos")
i9= Ingrediente("essência de baunilha")
i10= Ingrediente("nozes picadas")

ir1 = IngredienteDaReceita(r1, i1, 6, "colheres de sopa")
ir2 = IngredienteDaReceita(r1, i2, 0.5, "xícara de")
ir3 = IngredienteDaReceita(r1, i3, 2, "xícaras de")
ir4 = IngredienteDaReceita(r1, i4, 2, "pitadas de")
ir5 = IngredienteDaReceita(r1, i5, 1, "tablete")
ir6 = IngredienteDaReceita(r1, i6, 0.75, "xícara de")
ir7 = IngredienteDaReceita(r1, i7, 1.25, "xícaras de")
ir8 = IngredienteDaReceita(r1, i8, 4, "unidades de")
ir9 = IngredienteDaReceita(r1, i9, 1, "colher de chá")
ir10 = IngredienteDaReceita(r1, i10, 0.5, "xícara de")

irs = [ir1, ir2, ir3, ir4, ir5, ir6]
print(r1)
# .nome, r1.tempo_preparo, r1.modo_preparo)
#print(ir1, ir2, ir3, ir4, ir5, ir6)

for ir in irs:
    print(ir.quantidade, ir.unidade, ir.ingrediente.nome)

