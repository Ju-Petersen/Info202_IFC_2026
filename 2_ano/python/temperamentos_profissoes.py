class Desafio():
    def __init__(self, desc: str):
        self.descricao = desc
    def __str__(self):
        return f'''
    {self.descricao}
    '''

class Ponto_forte():
    def __init__(self, desc: str):
        self.descricao = desc
    def __str__(self):
        return f'''
    {self.descricao}
    '''

class Personalidade():
    def __init__(self, nm: str):
        self.nome = nm
    def __str__(self):
        return f'''
    {self.nome}
    '''

class Profissao():
    def __init__(self, nm: str):
        self.nome = nm
    def __str__(self):
        return f'''{self.nome}'''

class Area_ideal():
    def __init__(self, nm: str, prof: list[Profissao]):
        self.nome = nm
        self.profissoes = prof
    def __str__(self):
        return f'''{self.nome}, {self.profissoes}'''
        
class Temperamento():
    def __init__(self, id: int, nm: str, el: str, fc_prof: str, pf: list[Ponto_forte], des: list[Desafio], ps: list[Personalidade], ars: list[Area_ideal]):
        self.id = id
        self.nome = nm
        self.elemento = el
        self.foco_profissional = fc_prof
        self.pontos_fortes = pf
        self.desafios = des
        self.personalidades = ps
        self.areas = ars
    
    def __str__(self):
        return f'''
    Personalidade: {self.nome} | Elemento: {self.elemento}
    Foco: {self.foco_profissional} | Areas Ideais: {self.areas}
    '''
    
pf1 = Ponto_forte("Extrovertido")
pf2 = Ponto_forte("Comunicativo")
pf3 = Ponto_forte("Espontâneo")
lst_pf1 = [pf1, pf2, pf3]
des1 = Desafio("Impulsivo")
des2 = Desafio("Indisciplinado")
des3 = Desafio("Superficial")
lst_des1 = [des1, des2, des3]
ps1 = Personalidade("Bill Clinton")
ps2 = Personalidade("Will Smith")
ps3 = Personalidade("Anna (Frozen)")
lst_ps1 = [ps1, ps2, ps3]
pfs1 = Profissao("Jornalista")
pfs2 = Profissao("Vendedor")
pfs3 = Profissao("Ator")
pfs4 = Profissao("a")
pfs5 = Profissao("b")
pfs6 = Profissao("c")
pfs7 = Profissao("d")
pfs8 = Profissao("e")
pfs9 = Profissao("f")
lst_pfs1 = [pfs1, pfs2, pfs3]
lst_pfs2 = [pfs4, pfs5, pfs6]
lst_pfs3 = [pfs7, pfs8, pfs9]
ar1 = Area_ideal("Comunicação", lst_pfs1)
ar2 = Area_ideal("Vendas", lst_pfs2)
ar3 = Area_ideal("Entretenimento", lst_pfs3)
lst_ars1 = [ar1, ar2, ar3]
tbl1 = Temperamento(1, "Sanguineo", "ar", "Pessoas e Dinamismo", lst_pf1, lst_des1, lst_ps1, lst_ars1)

#for para acessar as informações em lista.
