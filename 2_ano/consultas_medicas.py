class Medico:
    def __init__(self, nm_m, esp):
        self.nome_medico = nm_m
        self.especialidade = esp
    def __str__(self):
        return f'''{self.nome_medico}, {self.especialidade}
'''

#O modo str deve dar print das informações necessária no teste
class Paciente:
    def __init__(self, nm, em, dt_nasc, med, ex):
        self.nome = nm
        self.email = em
        self.data_nascimento = dt_nasc
        self.medico = med
        self.exame = ex
    def __str__(self):
        return f'''
                Nome do Paciente: {self.nome}
                Email: {self.email}
                Data de nascimento: {self.data_nascimento}
                Médico que realixou o atendimento: {self.medico}
                Exame realizado: {self.exame}
'''
class Exame:
    def __init__(self, dt_rel, dthr_cons, rs, nm_ex):
        self.data_realizado = dt_rel
        self.resultado = rs
        self.datahora_consulta = dthr_cons
        self.nome_exame = nm_ex
    def __str__(self):
        return f'''{self.nome_exame}
                Data do Exame: {self.data_realizado}
                Informações da consulta: {self.datahora_consulta}
                Resultado: {self.resultado}
'''
#classes para armazenar informações da consulta, abaixo teste das classes

m1 = Medico("Pedro", "Radiologia")
e1 = Exame("03/03/2026", "04/03/2026", "fratura no punho", "Raio-x")
p1 = Paciente("Maria", "ma@gmail.com", "24/03/1999",m1, e1)

print(p1)