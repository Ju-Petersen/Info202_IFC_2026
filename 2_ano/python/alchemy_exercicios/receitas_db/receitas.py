from sqlalchemy import create_engine, String, Text, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session # classes e outros módulos para criação das tabelas
from typing import Optional

class Base(DeclarativeBase):
    pass

#A classe abaixo é retirada do exercicio 3receitas_2classe.py, será modificado p/ o modelo sqlalchemy:
class Receita(Base):
    __tablename__ = "tbl_receitas_julia"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(200))
    tempo_preparo: Mapped[int] = mapped_column(Integer)
    modo_preparo: Mapped[str] = mapped_column(String(500))
    ingredientes: Mapped[list] = mapped_column(String(500))

engine = create_engine("mysql+pymysql://root:root@localhost:3306/receitas_db_julia") # comentar com o professor pois a criação com mysql+pymysql está causando erro desconhecido!!!

Base.metadata.create_all(engine)

#Abrir sessão:
with Session(engine) as session:
    r1 = Receita(nome = "Bolo de milho", tempo_preparo = 50,

    modo_preparo = "Bate no liquidificador a farinha, o milho, "+\
    "o leite, óleo e os ovos, até moer bem "+\
    "o milho. Acrescente o fermento e "+\
    "pulse o liquidificador 3 vezes. "+\
    "Despeje na forma e leve a forno"+\
    " por 50 minutos. Espere esfriar e sirva.",

    ingredientes = "1 lata de milho,  leite (medida da lata), " +\
    "açúcar (medida da lata), 3 ovos, 1 colher de fermento," +\
    "1/2 lata de óleo")
    # adicionar o objeto ao db
    session.add(r1)
    session.commit() # atualizar as adições

    print("A tabela foi criada (se não existia) e os dados da receita foram inseridos.")
    print(f"A receita chamada {r1.nome} foi salva sob o número {r1.id}.")
