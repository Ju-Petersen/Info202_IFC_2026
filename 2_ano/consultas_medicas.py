class Medico:
    def __init__(self, nm_m, esp):
        self.nome_medico = nm_m
        self.especialidade = esp
    def __str__(self):
        return f'''
                Médico: {self.nome_medico}
                Especialidade: {self.especialidade}
'''

#O modo str deve dar print das informações necessária no teste
class Paciente:
    def __init__(self, nm, em, dt_nasc):
        self.nome = nm
        self.email = em
        self.data_nascimento = dt_nasc
    def __str__(self):
        return f'''
                Nome do Paciente: {self.nome}
                Email: {self.email}
                Data de nascimento: {self.data_nascimento}
'''
class Exame:
    def __init__(self, dt_r, rs, dh_c):
        self.data_realizado = dt_r
        self.resultado = rs
        self.datahora_consulta = dh_c
    def __str__(self):
        return f'''
                Data do Exame: {self.data_realizado}
                Informações da consulta: {self.datahora_consulta}
                Resultado: {self.resultado}
'''
#classes para armazenar informações da consulta, abaixo teste das classes

m1 = Medico("Pedro", "Radiologista")
p1 = Paciente("Maria", "ma@gmail.com", "24/12/1977")
c1 = Exame("23/03/26", "fratura na costela", "24/03/26 as 13:30")

print(m1, p1, c1)