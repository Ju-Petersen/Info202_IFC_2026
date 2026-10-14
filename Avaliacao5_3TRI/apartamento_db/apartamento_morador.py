from sqlalchemy import create_engine, String, Integer, Boolean, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional
from dotenv import load_dotenv
import os
import random

class Base(DeclarativeBase):
    pass

class Apartamento(Base):
    __tablename__ = "tbl_apartamento"

    id: Mapped[int] = mapped_column(primary_key=True)
    nro_apartamento: Mapped[int] = mapped_column(Integer)
    andar: Mapped[int] = mapped_column(Integer)

    apartamento: Mapped[List["Morador"]] = relationship(back_populates="moradores")

class Morador(Base):
    __tablename__ = "tbl_morador"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_apartamento: Mapped[int] = mapped_column(ForeignKey("tbl_apartamento.id"))
    nome: Mapped[str] = mapped_column(String(100))
    caracteristicas: Mapped[str] = mapped_column(String(500))
    honestidade: Mapped[str] = mapped_column(Boolean, default=True)

    moradores: Mapped[List["Apartamento"]] = relationship(back_populates="apartamento")

class Sosia(Base):
    __tablename__ = "tbl_sosia"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_morador: Mapped[int] = mapped_column(ForeignKey("tbl_morador.id"))
    nome: Mapped[str] = mapped_column(String(100))
    caracteristicas: Mapped[str] = mapped_column(String(500))

def mostrar_individuo(session):
    # consultar a tabela de moradores e sosias:
    id_moradores = session.execute(select(Morador.id)).all() # -->executar<-- um select nos ids, e "recolhe-los"
    id_sosias = session.execute(select(Sosia.id)).all()
    
    tipo = random.choice(["morador", "sosia"])
    # se for um morador:
    if tipo == "morador":
        # selecionar um morador aleatorio entre todos os moradores da tabela (com o id aleatorio *selecionado*):
        id_morador = random.choice(id_moradores)
        morador = session.get(Morador, id_morador)
        apt = session.get(Apartamento, morador.id_apartamento)
        # listar o(s) objeto(s) presente(s) na tabela:
        print(f'''
            nome: {morador.nome}
            apartamento: {apt.nro_apartamento}
            andar: {apt.andar}
            caracteristicas: {morador.caracteristicas}''')
        
        return("morador", morador)
    # se for uma sosia:    
    elif tipo == "sosia":
        # selecionar uma sosia aleatoria entre todas as sosias da tabela (com o id aleatorio *selecionado*):
        id_sosia = random.choice(id_sosias)
        sosia = session.get(Sosia, id_sosia)
        mor_sosia = session.get(Morador, sosia.id_morador)
        apt_sosia = session.get(Apartamento, mor_sosia.id_apartamento)
        # listar o(s) objeto(s) presente(s) na tabela:
        print(f'''
            nome: {sosia.nome}
            apartamento: {apt_sosia.nro_apartamento}
            andar: {apt_sosia.andar}
            caracteristicas: {sosia.caracteristicas}''')

        return("sosia", sosia)

def listar_informacoes(session): # listar os moradores verdadeiros e suas caracteristicas
    # consultar a tabela de moradores e sosias:
    moradores = session.execute(select(Morador)).all() # -->executar<-- um select nos ids, e "recolhe-los"
    # listar o(s) objeto(s) presente(s) na tabela:
    for m in moradores:
        morador = m[0]
        
        apt = session.get(Apartamento, morador.id_apartamento)
        
        print(f'''
            nome: {morador.nome}
            apartamento: {apt.nro_apartamento}
            andar: {apt.andar}
            caracteristicas: {morador.caracteristicas}
            ''')

def denunciar_sosia(session, sosia): # excluir
    # deletar a sosia do banco de dados:
    session.delete(sosia)
    session.commit()
    
    print("Anomalia removida.")

def personalizar_individuos(session): # inserir
    escolha = input(f'''
        +-------------------+
        | 1 - Criar Morador |
        | 2 - Criar Sósia   |
        +-------------------+
        
        : ''')
    if escolha == "1":
        # pedir artributos:
        nome = input(f'''Dê um nome a seu morador: ''')
        caracteristicas = input(f'''Digite suas características (ou cole uma ascii art :D): ''')
        apt = int(input(f'''Identificação do apartamento (1, 2, 3, 4, ... até 16): '''))
        
        morador_personalizado = Morador(nome=nome, caracteristicas=caracteristicas, id_apartamento=apt, honestidade=True)
        session.add(morador_personalizado)
        session.commit()
        print("Morador adicionado :)")
    
    elif escolha == "2":
        qtd_moradores = len(session.execute(select(Morador.id)).all()) # -->executar<-- um select nos ids, e "recolhe-los"
        # pedir artributos:
        nome = input(f'''Dê um nome a sua sósia: ''')
        caracteristicas = input(f'''Digite suas características (ou cole uma ascii art :D): ''')
        morador_copiado = int(input(f'''Qual a identificação do morador que ela copia? (1, 2, 3, 4, ... até {qtd_moradores}): '''))
        
        sosia_personalizado = Sosia(nome=nome, caracteristicas=caracteristicas, id_morador=morador_copiado)
        session.add(sosia_personalizado)
        session.commit()
        print("Sósia adicionada :)")

def main():

    while True:
        print('''
                        +---------------+
                        | 1 - MySQL     |
                        | 2 - SQLite    |
                        | 3 - Encerrar  |
                        +---------------+''')
        escolha_db = input(f"Escolha qual database você deseja utilizar: ")

        if escolha_db == "1":
            # ler o arquivo .env
            load_dotenv()
            # buscando as variaveis de ambiente
            MYSQL_USER = os.getenv("MYSQL_USER")
            MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
            MYSQL_HOST = os.getenv("MYSQL_HOST")
            MYSQL_PORT = os.getenv("MYSQL_PORT")
            MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
            engine = create_engine("mysql+pymysql://root@localhost:3306/apartamentos_db")
            Base.metadata.create_all(engine)
            
            with Session(engine) as session:
                    ap1 = Apartamento(nro_apartamento=101, andar=1)
                    ap2 = Apartamento(nro_apartamento=102, andar=1)
                    ap3 = Apartamento(nro_apartamento=103, andar=1)
                    ap4 = Apartamento(nro_apartamento=104, andar=1)
                    ap5 = Apartamento(nro_apartamento=201, andar=2)
                    ap6 = Apartamento(nro_apartamento=202, andar=2)
                    ap7 = Apartamento(nro_apartamento=203, andar=2)
                    ap8 = Apartamento(nro_apartamento=204, andar=2)
                    ap9 = Apartamento(nro_apartamento=301, andar=3)
                    ap10 = Apartamento(nro_apartamento=302, andar=3)
                    ap11 = Apartamento(nro_apartamento=303, andar=3)
                    ap12 = Apartamento(nro_apartamento=304, andar=3)
                    ap13 = Apartamento(nro_apartamento=401, andar=4)
                    ap14 = Apartamento(nro_apartamento=402, andar=4)
                    ap15 = Apartamento(nro_apartamento=403, andar=4)
                    ap16 = Apartamento(nro_apartamento=404, andar=4)
                    m1 = Morador(id_apartamento=1, nome="Felipe",caracteristicas="Alto", honestidade=True)
                    m2 = Morador(id_apartamento=1, nome="Pedro",caracteristicas="Baixo", honestidade=True)
                    m3 = Morador(id_apartamento=2, nome="Igor",caracteristicas="Velho", honestidade=True)
                    m4 = Morador(id_apartamento=3, nome="Arthur",caracteristicas="Nerd", honestidade=True)
                    m5 = Morador(id_apartamento=3, nome="Daniel",caracteristicas="Música", honestidade=True)
                    m6 = Morador(id_apartamento=3, nome="Julia",caracteristicas="AAAAAAAAAA", honestidade=True)
                    m7 = Morador(id_apartamento=4, nome="Victor",caracteristicas="BBBBBBBBBB", honestidade=True)
                    m8 = Morador(id_apartamento=5, nome="Matheus", caracteristicas="Dream", honestidade=True)
                    m9 = Morador(id_apartamento=5, nome="Lara", caracteristicas="Emo", honestidade=True)
                    m10 = Morador(id_apartamento=6, nome="Santiago",caracteristicas="Cabelo", honestidade=True)
                    m11 = Morador(id_apartamento=7, nome="Vitorio",caracteristicas="Sardas", honestidade=True)
                    m12 = Morador(id_apartamento=8, nome="Hilda",caracteristicas="Olhos", honestidade=True)
                    m13 = Morador(id_apartamento=9, nome="Henrique",caracteristicas="Limão", honestidade=True)
                    m14 = Morador(id_apartamento=10, nome="Radija",caracteristicas="Roxo", honestidade=True)
                    m15 = Morador(id_apartamento=11, nome="Mariana",caracteristicas="Óculos", honestidade=True)
                    m16 = Morador(id_apartamento=12, nome="Oliver", caracteristicas="Curto", honestidade=True)
                    m17 = Morador(id_apartamento=13, nome="Ryan",caracteristicas="Moreno", honestidade=True)
                    m18 = Morador(id_apartamento=14, nome="Natalia",caracteristicas="Inteligente", honestidade=True)
                    m19 = Morador(id_apartamento=15, nome="Melina",caracteristicas="Desenhos", honestidade=True)
                    m20 = Morador(id_apartamento=16, nome="Luana",caracteristicas="Vestidos", honestidade=True)
                    s1 = Sosia(id_morador=1, nome="Felipe", caracteristicas="Baixo")
                    s2 = Sosia(id_morador=2, nome="Pedro", caracteristicas="Alto")
                    s3 = Sosia(id_morador=3, nome="Igor", caracteristicas="Novo")
                    s4 = Sosia(id_morador=4, nome="Arthur", caracteristicas="Leigo")
                    s5 = Sosia(id_morador=5, nome="Daniel", caracteristicas="Surdo")
                    s6 = Sosia(id_morador=6, nome="Julia", caracteristicas="BBBBBBBBBB")
                    s7 = Sosia(id_morador=7, nome="Victor", caracteristicas="AAAAAAAAAA")
                    s8 = Sosia(id_morador=8, nome="Matheus", caracteristicas="Nightmare")
                    s9 = Sosia(id_morador=9, nome="Lara", caracteristicas="Scene")
                    s10 = Sosia(id_morador=10, nome="Santiago", caracteristicas="Verde")
                    s11 = Sosia(id_morador=11, nome="Vitorio", caracteristicas="Sem sardas")
                    s12 = Sosia(id_morador=12, nome="Hilda", caracteristicas="Cega")
                    s13 = Sosia(id_morador=13, nome="Henrique", caracteristicas="Maca")
                    s14 = Sosia(id_morador=14, nome="Radija", caracteristicas="Amarelo")
                    s15 = Sosia(id_morador=15, nome="Mariana", caracteristicas="Sem oculos")
                    s16 = Sosia(id_morador=16, nome="Oliver", caracteristicas="Longo")
                    s17 = Sosia(id_morador=17, nome="Ryan", caracteristicas="Louro")
                    s18 = Sosia(id_morador=18, nome="Natalia", caracteristicas="Burro")
                    s19 = Sosia(id_morador=19, nome="Melina", caracteristicas="IA")
                    s20 = Sosia(id_morador=20, nome="Luana", caracteristicas="Calças")
    
                    session.add(ap1)
                    session.add(ap2)
                    session.add(ap3)
                    session.add(ap4)
                    session.add(ap5)
                    session.add(ap6)
                    session.add(ap7)
                    session.add(ap8)
                    session.add(ap9)
                    session.add(ap10)
                    session.add(ap11)
                    session.add(ap12)
                    session.add(ap13)
                    session.add(ap14)
                    session.add(ap15)
                    session.add(ap16)
                    session.add(m1)
                    session.add(m2)
                    session.add(m3)
                    session.add(m4)
                    session.add(m5)
                    session.add(m6)
                    session.add(m7)
                    session.add(m8)
                    session.add(m9)
                    session.add(m10)
                    session.add(m11)
                    session.add(m12)
                    session.add(m13)
                    session.add(m14)
                    session.add(m15)
                    session.add(m16)
                    session.add(m17)
                    session.add(m18)
                    session.add(m19)
                    session.add(m20)
                    session.add(s1)
                    session.add(s2)
                    session.add(s3)
                    session.add(s4)
                    session.add(s5)
                    session.add(s6)
                    session.add(s7)
                    session.add(s8)
                    session.add(s9)
                    session.add(s10)
                    session.add(s11)
                    session.add(s12)
                    session.add(s13)
                    session.add(s14)
                    session.add(s15)
                    session.add(s16)
                    session.add(s17)
                    session.add(s18)
                    session.add(s19)
                    session.add(s20)
                    session.commit()

            print(f"Database MySQL iniciada (acesse o servidor com DBeaver para visualizar as informações).")
            
        elif escolha_db == "2":
            engine = create_engine("sqlite:///apartamentos_db")
            Base.metadata.create_all(engine)

            with Session(engine) as session:
                ap1 = Apartamento(nro_apartamento=101, andar=1)
                ap2 = Apartamento(nro_apartamento=102, andar=1)
                ap3 = Apartamento(nro_apartamento=103, andar=1)
                ap4 = Apartamento(nro_apartamento=104, andar=1)
                ap5 = Apartamento(nro_apartamento=201, andar=2)
                ap6 = Apartamento(nro_apartamento=202, andar=2)
                ap7 = Apartamento(nro_apartamento=203, andar=2)
                ap8 = Apartamento(nro_apartamento=204, andar=2)
                ap9 = Apartamento(nro_apartamento=301, andar=3)
                ap10 = Apartamento(nro_apartamento=302, andar=3)
                ap11 = Apartamento(nro_apartamento=303, andar=3)
                ap12 = Apartamento(nro_apartamento=304, andar=3)
                ap13 = Apartamento(nro_apartamento=401, andar=4)
                ap14 = Apartamento(nro_apartamento=402, andar=4)
                ap15 = Apartamento(nro_apartamento=403, andar=4)
                ap16 = Apartamento(nro_apartamento=404, andar=4)
                m1 = Morador(id_apartamento=1, nome="Felipe",caracteristicas="Alto", honestidade=True)
                m2 = Morador(id_apartamento=1, nome="Pedro",caracteristicas="Baixo", honestidade=True)
                m3 = Morador(id_apartamento=2, nome="Igor",caracteristicas="Velho", honestidade=True)
                m4 = Morador(id_apartamento=3, nome="Arthur",caracteristicas="Nerd", honestidade=True)
                m5 = Morador(id_apartamento=3, nome="Daniel",caracteristicas="Música", honestidade=True)
                m6 = Morador(id_apartamento=3, nome="Julia",caracteristicas="AAAAAAAAAA", honestidade=True)
                m7 = Morador(id_apartamento=4, nome="Victor",caracteristicas="BBBBBBBBBB", honestidade=True)
                m8 = Morador(id_apartamento=5, nome="Matheus", caracteristicas="Dream", honestidade=True)
                m9 = Morador(id_apartamento=5, nome="Lara", caracteristicas="Emo", honestidade=True)
                m10 = Morador(id_apartamento=6, nome="Santiago",caracteristicas="Cabelo", honestidade=True)
                m11 = Morador(id_apartamento=7, nome="Vitorio",caracteristicas="Sardas", honestidade=True)
                m12 = Morador(id_apartamento=8, nome="Hilda",caracteristicas="Olhos", honestidade=True)
                m13 = Morador(id_apartamento=9, nome="Henrique",caracteristicas="Limão", honestidade=True)
                m14 = Morador(id_apartamento=10, nome="Radija",caracteristicas="Roxo", honestidade=True)
                m15 = Morador(id_apartamento=11, nome="Mariana",caracteristicas="Óculos", honestidade=True)
                m16 = Morador(id_apartamento=12, nome="Oliver", caracteristicas="Curto", honestidade=True)
                m17 = Morador(id_apartamento=13, nome="Ryan",caracteristicas="Moreno", honestidade=True)
                m18 = Morador(id_apartamento=14, nome="Natalia",caracteristicas="Inteligente", honestidade=True)
                m19 = Morador(id_apartamento=15, nome="Melina",caracteristicas="Desenhos", honestidade=True)
                m20 = Morador(id_apartamento=16, nome="Luana",caracteristicas="Vestidos", honestidade=True)
                s1 = Sosia(id_morador=1, nome="Felipe", caracteristicas="Baixo")
                s2 = Sosia(id_morador=2, nome="Pedro", caracteristicas="Alto")
                s3 = Sosia(id_morador=3, nome="Igor", caracteristicas="Novo")
                s4 = Sosia(id_morador=4, nome="Arthur", caracteristicas="Leigo")
                s5 = Sosia(id_morador=5, nome="Daniel", caracteristicas="Surdo")
                s6 = Sosia(id_morador=6, nome="Julia", caracteristicas="BBBBBBBBBB")
                s7 = Sosia(id_morador=7, nome="Victor", caracteristicas="AAAAAAAAAA")
                s8 = Sosia(id_morador=8, nome="Matheus", caracteristicas="Nightmare")
                s9 = Sosia(id_morador=9, nome="Lara", caracteristicas="Scene")
                s10 = Sosia(id_morador=10, nome="Santiago", caracteristicas="Verde")
                s11 = Sosia(id_morador=11, nome="Vitorio", caracteristicas="Sem sardas")
                s12 = Sosia(id_morador=12, nome="Hilda", caracteristicas="Cega")
                s13 = Sosia(id_morador=13, nome="Henrique", caracteristicas="Maca")
                s14 = Sosia(id_morador=14, nome="Radija", caracteristicas="Amarelo")
                s15 = Sosia(id_morador=15, nome="Mariana", caracteristicas="Sem oculos")
                s16 = Sosia(id_morador=16, nome="Oliver", caracteristicas="Longo")
                s17 = Sosia(id_morador=17, nome="Ryan", caracteristicas="Louro")
                s18 = Sosia(id_morador=18, nome="Natalia", caracteristicas="Burro")
                s19 = Sosia(id_morador=19, nome="Melina", caracteristicas="IA")
                s20 = Sosia(id_morador=20, nome="Luana", caracteristicas="Calças")

                session.add(ap1)
                session.add(ap2)
                session.add(ap3)
                session.add(ap4)
                session.add(ap5)
                session.add(ap6)
                session.add(ap7)
                session.add(ap8)
                session.add(ap9)
                session.add(ap10)
                session.add(ap11)
                session.add(ap12)
                session.add(ap13)
                session.add(ap14)
                session.add(ap15)
                session.add(ap16)
                session.add(m1)
                session.add(m2)
                session.add(m3)
                session.add(m4)
                session.add(m5)
                session.add(m6)
                session.add(m7)
                session.add(m8)
                session.add(m9)
                session.add(m10)
                session.add(m11)
                session.add(m12)
                session.add(m13)
                session.add(m14)
                session.add(m15)
                session.add(m16)
                session.add(m17)
                session.add(m18)
                session.add(m19)
                session.add(m20)
                session.add(s1)
                session.add(s2)
                session.add(s3)
                session.add(s4)
                session.add(s5)
                session.add(s6)
                session.add(s7)
                session.add(s8)
                session.add(s9)
                session.add(s10)
                session.add(s11)
                session.add(s12)
                session.add(s13)
                session.add(s14)
                session.add(s15)
                session.add(s16)
                session.add(s17)
                session.add(s18)
                session.add(s19)
                session.add(s20)
                session.commit()

            print(f"Database SQLite iniciada (acesse o arquivo apartamentos_db com a extensão do SQLite Viewer para visualizar as informações).")
        
        elif escolha_db == "3":
            print(f"Encerrando o programa...")
            break
        else:
            print(f"Opção inválida. Tente novamente.")

        while True:  
            
            print('''
                +-------------------------+
                | 1 - Iniciar             |
                | 2 - Lista de  moradores |
                | 3 - Personalizar        |
                | 4 - Encerrar            |
                +-------------------------+''')
            
            opcao = input(f"Escolha uma opção: ")

            if opcao == "1":
                # mostrar um individuo (escolhido aleatoriamente):
                resultado = mostrar_individuo(session)
                
                tipo, individuo = resultado # retorna se e sosia/"sosia" ou morador/"morador"
                
                print('''
                +-------------------------+
                | 1 - Decunciar           |
                | 2 - Não Denunciar       |
                | 3 - Ver lista novamente |
                +-------------------------+''')
                
                executar = input("Denunciar? (Digite 1 ou 2): ") # o usuario decide se tal individuo e ou nao uma sosia/anomalia
                # se for denunciar:
                if executar == "1" and tipo == "sosia": # e o individuo e uma sosia:
                        denunciar_sosia(session, individuo)
                        print("V")
                # se for denunciar:
                elif executar == "1" and tipo == "morador":
                    denunciar_sosia(session, individuo) # e o individuo nao e uma sosia:
                    print("X")
                # se nao for denunciar:
                if executar == "2" and tipo == "morador": # e o individuo e morador:
                        print("V")
                # se nao for denunciar:
                elif executar == "2" and tipo == "sosia": # e o individuo nao e morador:
                        print("X")
                
                if opcao == "3":
                    print("Estes são todos os moradores não anômalos e suas características: ")
                    listar_informacoes(session)
            
            elif opcao == "2":
                print("Estes são todos os moradores não anômalos e suas características: ")
                listar_informacoes(session)

            elif opcao == "3":
                personalizar_individuos(session)

            elif opcao == "4":
                print("Encerrando o programa...")
                break

            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

'''
Escolha 2 classes relacionadas de forma 1 para N e implemente-as usando o SQLAlchemy - FEITO
    - Cada classe deve ter pelo menos 4 atributos - FEITO
    - Escolha classes diferentes de outras pessoas! Uma classe pode ser igual, mas a outra precisa ser diferente - FEITO
!!! Faca um programa de terminal que interaja com o usuario, 
    permitindo realizar as 3 operacoes: --> --> inserir, listar e excluir dados <-- <-- - FEITO
        - Devem ser manipulados dados das 2 classes - FEITO
        - O programa deve ter opcao para o usuario se conectar a um banco de dados SQLite ou a um banco de dados MySql - ??
        - O usuario escolhe em qual banco de dados deseja se conectar - ??
        - Durante a operacao do programa ele pode alterar a conexao (SQLite ou MySql) - ??
'''
