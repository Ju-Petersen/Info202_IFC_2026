# alguns imports
from sqlalchemy import ForeignKey, create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional

# classe "base"
class Base(DeclarativeBase):
    pass

# classe pessoa, que herda da "base"
class Pessoa(Base):
    # nome da tabela a ser criada no banco de dados
    __tablename__ = "PESSOA_TABLE_JULIA"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)

    # atributo "lista reversa"
    celulares: Mapped[List["Celular"]] = relationship(back_populates="pessoa")

class Celular(Base):
    __tablename__ = "CELULAR_TABLE_JULIA"
    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[str] = mapped_column(String)
    marca: Mapped[str] = mapped_column(String)
    operadora: Mapped[str] = mapped_column(String)

    # chave estrangeira :-)
    pessoa_id: Mapped[int] = mapped_column(ForeignKey("PESSOA_TABLE_JULIA.id"))
    # atributo para acesso ao objeto inteiro :-)
    pessoa: Mapped["Pessoa"] = relationship(back_populates="celulares")

# definição do banco de dados
engine = create_engine("sqlite:///pessoas_e_celulares.db")

# configuração para criar o arquivo de banco de dados
Base.metadata.create_all(engine)

# abrir a sessão
with Session(engine) as session:

    # criar uma pessoa
    p = Pessoa(nome="João da Silva", 
               email="joao@email.com")
    p1 = Pessoa(nome="Maria Oliveira",
                email="maria@email.com")
    p2 = Pessoa(nome="Thiago Machado",
                email="thiago@email.com")

    # criar um celular
    c = Celular(numero="912345678", marca="Samsung", 
                 operadora="Vivo")
    c1=Celular(numero="987654321", marca="Apple",
                 operadora="Claro")

    # informar o DONO do celular
    c.pessoa = p
    c1.pessoa = p1

    # adicionar os objetos na sessão
    session.add(p)
    session.add(p1)
    session.add(p2)
    session.add(c)
    session.add(c1)
        
    # confirmar a inserção no banco de dados
    session.commit()

    print("Banco de dados criado (se não existia), tabela criada (se não havia) e dados inseridos no banco")

'''
- No código exemplo, crie mais uma pessoa e mais dois celulares, que vão pertencer a essa nova pessoa; - FEITO
    | execute o código e verifique no banco de dados se os registros foram inseridos corretamente - FEITO
- Modifique o programa para, em vez de acessar o SQLite, acessar o MySql. - FEITO
- Use o programa da aula anterior como referência, para acessar o MySql. - FEITO
- Levante uma instância de MySql no seu computador (use o XAMPP) - FEITO
'''
