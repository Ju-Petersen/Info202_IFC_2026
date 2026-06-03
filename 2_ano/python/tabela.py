class Jogador():
    def __init__(self, pos: str, nm: str, clu: str):
        self.posicao = pos
        self.nome = nm
        self.clube = clu
    def __str__(self):
        return f'''
        Posição: {self.posicao}
        Nome: {self.nome}
        Clube: {self.clube}'''

class Selecao():
    def __init__(self, nm: str, jgdrs: list):
        self.nome = nm
        self.jogadores = jgdrs
    
    def __str__(self):
        return f'''
        Seleção: {self.nome}
        Jogadores para essa seleção: {self.jogadores}'''
    
j1 = Jogador("Goleiro", "Alisson", "Liverpool FC")
j2 = Jogador("Lateral", "Danilo", "CR Flamengo")
j3 = Jogador("Atacante", "Endrick", "Olympique Lyonnais")
j4 = Jogador("Meio-campo", "Bruno", "Newcastle United FC")
j5 = Jogador("Zagueiro", "Bremer", "Juventus FC")
lst_j1 = [j1, j2, j3, j4, j5]
s1 = Selecao("Sei lá", lst_j1)

print(f'''Seleção: {s1.nome}
Jogadores para a seleção:''')
for j in lst_j1:
            print(f"{j.posicao}  |  {j.nome}  |  {j.clube}")