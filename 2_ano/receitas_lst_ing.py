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
    def __init__(self, receita, ingrediente, quantidade, unidade):
        self.receita = receita
        self.ingrediente = ingrediente
        self.quantidade = quantidade
        self.unidade = unidade

# teste da classe
r1 = Receita("Bolo de Milho", 50,
              "Bater tudo no liquidificador e colocar no forno")

#i1= Ingrediente()
#Não é necessário deixar 
# os ingredientes separados (mais variáveis) 
# apenas mudar i1, i2 .... pelo nome do ingrediente

ir1 = Ingrediente(r1, "Milho", 1, "lata")
ir2 = Ingrediente(r1, "Leite", 1, "lata(milho)")
ir3 = Ingrediente(r1, "Açúcar", 1, "lata(milho)")
ir4 = Ingrediente(r1, "Ovos", 3, "unidade")
ir5 = Ingrediente(r1, "Óleo", 0.5, "lata")
ir6 = Ingrediente(r1, "Fermento", 1, "colher de chá")

r2 = Receita("Brownie", 40, 
'''
    1 - Misture os ovos e o açúcar.

    2 - Em seguida, agregue todos os outros ingredientes até formar um creme uniforme.

    3 - Despeje em uma assadeira, forrada com papel-manteiga e leve ao forno médio por 40 minutos.

    4 - O brownie estará pronto quando a parte de cima estiver levemente corada e, ao se espetar um palito, ele esteja levemente úmido (devido ao chocolate derretido).

    5 - Corte em quadrados ainda quente e sirva com uma bola de sorvete de creme, ou congele num saquinho para freezer.

    6 - Para descongelar, coloque o brownie num prato de sobremesa e aqueça no micro-ondas, potência alta, por 1 minuto''')

ir7 = Ingrediente(r2, "Margarina", 6, "colheres de sopa")
ir8 = Ingrediente(r2, "Chocolate em pó", 0.5, "xícara de")
ir9 = Ingrediente(r2, "Açúcar", 2, "xícaras de")
ir10 = Ingrediente(r2, "Sal", 2, "pitadas de")
ir11 = Ingrediente(r2, "Chocolate meio amargo", 1, "tablete")
ir12 = Ingrediente(r2, "Achocolatado", 0.75, "xícara de")
ir13 = Ingrediente(r2, "Farinha de trigo", 1.25, "xícaras de")
ir14 = Ingrediente(r2, "Ovos", 4, "unidades de")
ir15 = Ingrediente(r2, "Essência de baunilha", 1, "colher de chá")
ir16 = Ingrediente(r2, "Nozes picadas", 0.5, "xícara de")

ir1s = [ir1, ir2, ir3, ir4, ir5, ir6]
ir2s = [ir7, ir8, ir9, ir10, ir11, ir12, ir13, ir14, ir15, ir16]
print(r1)
# .nome, r1.tempo_preparo, r1.modo_preparo)
#print(ir1, ir2, ir3, ir4, ir5, ir6)

for ir in ir1s:
    print(ir.quantidade, ir.unidade, ir.ingrediente)

print(r2)

for i in ir2s:
    print(i.quantidade, i.unidade, i.ingrediente)

tabela = {}