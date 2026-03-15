class Pessoa:
    def __init__(self, nm, dt_nasc, cpf, em):
        self.nome = nm
        self.data_nascimento = dt_nasc
        self.cpf = cpf
        self.email = em

    def __str__(self):
        return f'''
                Nome: {self.nome}
                Data de Nascimento: {self.data_nascimento}
                CPF: {self.cpf}
                E-mail: {self.email}
'''
    
class Telefone:
    def __init__(self, nro, mc, op, ps):
        self.pessoa = ps
        self.numero = nro
        self.marca = mc
        self.operadora = op

    def __str__(self):
        return f'''
                Pessoa vinculada ao(s) celular(es): {self.pessoa}
                Número: {self.numero}
                Marca: {self.marca}
                Operadora: {self.operadora}
'''

p1 = Pessoa("Maria", "02/03/1999", 123.456-22, "ma@gmail.com")
p2 = Pessoa("João", "28/03/2000", 321.654-23, "jo@gmail.com")
c1 = Telefone("(47)1234-5678", "Motorola", "Vivo", "Maria")
c2 = Telefone("(47)4321-8765", "Xiaomi", "Claro", "Maria")
c3 = Telefone("(47)9987-3841", "Motorola", "Tim", "João")

print(p1, c1, c2)
print(p2, c3)