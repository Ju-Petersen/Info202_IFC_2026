from sqlalchemy import create_engine, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional

class Base(DeclarativeBase):
    pass

class Apartamento(Base):
    __tablename__ = "tbl_apartamento"
    
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    nro_apartamento: Mapped[int] = mapped_column(Integer)
    andar: Mapped[int] = mapped_column(Integer)
        
    moradores: Mapped[List["Morador"]] = relationship(back_populates="apartamento")
    
class Morador(Base):
    __tablename__ = "tbl_morador"
    
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    id_apartamento: Mapped[int] = mapped_column(ForeignKey("tbl_apartamento.id"), primary_key=True)
    nome: Mapped[int] = mapped_column(String(250))
    caracteristicas: Mapped[str] = mapped_column(String(500))
    honestidade: Mapped[str] = mapped_column(Boolean, default=True)
        
    apartamento: Mapped[List["Apartamento"]] = relationship(back_populates="moradores")
    
engine = create_engine("sqlite:///apartamentos_db")

Base.metadata.create_all(engine) # Solicitar a criação das tabelas (classes) informadas acima

with Session(engine) as session: # Iniciar sessão
    # Os objetos criados contém as informacoes que 
    # equivalem ao que aparecera preenchendo as tabelas 
    # (classes) criadas para a database:
    ap1 = Apartamento(nro_apartamento=101, andar=1)
    m1 = Morador(nome="A", caracteristicas="Alto, moreno, nariz fino, ...", honestidade=True)

    session.add(ap1) # Adicionar o objeto criado
    session.add(m1)
    session.commit() # Salvar as alterações que foram feitas na database

print("A database foi criada com sucesso!") # Teste para confirmação da criação da db

'''
Escolha 2 classes relacionadas de forma 1 para N e implemente-as usando o SQLAlchemy
    - Cada classe deve ter pelo menos 4 atributos
    - Escolha classes diferentes de outras pessoas! Uma classe pode ser igual, mas a outra precisa ser diferente
!!! Faça um programa de terminal que interaja com o usuário, permitindo realizar as 3 operações: --> --> inserir, listar e excluir dados <-- <--
        - Devem ser manipulados dados das 2 classes
        - O programa deve ter opção para o usuário se conectar a um banco de dados SQLite ou a um banco de dados MySql
        - O usuário escolhe em qual banco de dados deseja se conectar
        - Durante a operação do programa ele pode alterar a conexão (SQLite ou MySql)
'''
