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
        # selecionar um morador aleatório entre todos os moradores da tabela (com o id aleatorio *selecionado*):
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
        # selecionar uma sosia aleatória entre todas as sosias da tabela (com o id aleatorio *selecionado*):
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

def listar_informacoes(session): # listar os moradores verdadeiros e suas características
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

# def selecionar_db():
#     print("temporario")

# ler o arquivo .env
# load_dotenv()

# buscando as variáveis de ambiente
# MYSQL_USER = os.getenv("MYSQL_USER")
# MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
# MYSQL_HOST = os.getenv("MYSQL_HOST")
# MYSQL_PORT = os.getenv("MYSQL_PORT")
# MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# engine = create_engine("mysql+pymysql://root@localhost:3306/apartamentos_db")

def main(session):
    while True:
        print('''
            +-------------------------+
            | 1 - Iniciar             |
            | 2 - Lista de  moradores |
            | 3 - Personalizar        |
            | 4 - Encerrar            |
            +-------------------------+''')
        
        opcao = input("Escolha uma opção: ")

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

engine = create_engine("sqlite:///apartamentos_db")
Base.metadata.create_all(engine)

if __name__ == "__main__":
    with Session(engine) as session:
        main(session)

'''
Escolha 2 classes relacionadas de forma 1 para N e implemente-as usando o SQLAlchemy - FEITO
    - Cada classe deve ter pelo menos 4 atributos - FEITO
    - Escolha classes diferentes de outras pessoas! Uma classe pode ser igual, mas a outra precisa ser diferente - FEITO
!!! Faça um programa de terminal que interaja com o usuário, 
    permitindo realizar as 3 operações: --> --> inserir, listar e excluir dados <-- <-- - FEITO
        - Devem ser manipulados dados das 2 classes - FEITO
        - O programa deve ter opção para o usuário se conectar a um banco de dados SQLite ou a um banco de dados MySql - ??
        - O usuário escolhe em qual banco de dados deseja se conectar - ??
        - Durante a operação do programa ele pode alterar a conexão (SQLite ou MySql) - ??
'''
