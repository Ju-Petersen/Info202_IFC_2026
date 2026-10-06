from sqlalchemy import create_engine, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional

class Base(DeclarativeBase):
    pass

class Apartamento(Base): # v
    __tablename__ = "tbl_apartamento"

    id: Mapped[int] = mapped_column(primary_key=True)
    nro_apartamento: Mapped[int] = mapped_column(Integer)
    andar: Mapped[int] = mapped_column(Integer)

    moradores: Mapped[List["Morador"]] = relationship(back_populates="apartamento")

class Morador(Base):
    __tablename__ = "tbl_morador"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_apartamento: Mapped[int] = mapped_column(ForeignKey("tbl_apartamento"), primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    caracteristicas: Mapped[str] = mapped_column(String(500))
    honestidade: Mapped[str] = mapped_column(Boolean, default=True)

    sosias: Mapped[List["Sosia"]] = relationship(back_populates="morador")

class Sosia(Base):
    __tablename__ = "tbl_sosia"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_morador: Mapped[int] = mapped_column(ForeignKey("tbl_morador"), primary_key=True)
    caracteristicas: Mapped[str] = mapped_column(String(500))

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
