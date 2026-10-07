from sqlalchemy import create_engine, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional
import os
from dotenv import load_dotenv

class Base(DeclarativeBase):
    pass

class Apartamento(Base):
    __tablename__ = "tbl_apartamento"

    id: Mapped[int] = mapped_column(primary_key=True)
    nro_apartamento: Mapped[int] = mapped_column(Integer)
    andar: Mapped[int] = mapped_column(Integer)

    moradores: Mapped[List["Morador"]] = relationship(back_populates="apartamento")

class Morador(Base):
    __tablename__ = "tbl_morador"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_apartamento: Mapped[int] = mapped_column(ForeignKey("tbl_apartamento.id"))
    nome: Mapped[str] = mapped_column(String(100))
    caracteristicas: Mapped[str] = mapped_column(String(500))
    honestidade: Mapped[str] = mapped_column(Boolean, default=True)

    sosias: Mapped[List["Sosia"]] = relationship(back_populates="morador")

class Sosia(Base):
    __tablename__ = "tbl_sosia"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_morador: Mapped[int] = mapped_column(ForeignKey("tbl_morador.id"))
    caracteristicas: Mapped[str] = mapped_column(String(500))

    morador: Mapped[List["Morador"]] = relationship(back_populates="sosia")

# ler o arquivo .env
load_dotenv()

# buscando as variáveis de ambiente
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


engine = create_engine("mysql+pymysql://root@localhost:3306/apartamentos_db")

Base.metadata.create_all(engine)

with Session(engine) as session:

    ap1 = Apartamento(nro_apartamento=101, andar=1)
    m1 = Morador(id_apartamento=1, nome="Pedro",caracteristicas="lorem ipsum somebullcrap", honestidade=True)
    s1 = Sosia(id_morador=1, caracteristicas="lorem ipsum not some somebullcrap")

    session.add(ap1)
    session.add(m1)
    session.add(s1)
    session.commit()

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
