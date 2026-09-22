from sqlalchemy import create_engine, String, Text, Integer, Float, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship # classes e outros módulos para criação das tabelas
from typing import Optional, List

class Base(DeclarativeBase):
    pass
#A classe abaixo é retirada do exercicio 3receitas_2classe.py, será modificado p/ o modelo sqlalchemy:
class Receita(Base):
    __tablename__ = "tbl_receitas_julia"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(200))
    tempo_preparo: Mapped[int] = mapped_column(Integer)
    modo_preparo: Mapped[str] = mapped_column(String(500))

    lst_ings: Mapped[List["Ingredientes"]] = relationship(back_populates="receitas")

class Ingredientes(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(150))

    receitas: Mapped["Receita"] = relationship(back_populates="lst_ings")

class IngredienteNaReceita(Base):
    receita_id: Mapped[int] = mapped_column(ForeignKey(Receita.id))
    ingrediente_id: Mapped[int] = mapped_column(ForeignKey(Ingredientes.id))
    unidade: Mapped[str] = mapped_column(String(150))
    quantidade: Mapped[int] = mapped_column(Float)

    ings_receita: Mapped[List["Ingredientes"]] = relationship(back_populates="receitas")

engine = create_engine("mysql+pymysql://root:root@localhost:3306/receitas_db_julia") # comentar com o professor pois a criação com mysql+pymysql está causando erro desconhecido!!!

Base.metadata.create_all(engine)

#Abrir sessão:
with Session(engine) as session:

    r1 = Receita(nome = "Bolo de milho", tempo_preparo = 50,

    modo_preparo = '''Bate no liquidificador a farinha, o milho,
    o leite, óleo e os ovos, até moer bem
    o milho. Acrescente o fermento e
    pulse o liquidificador 3 vezes.
    Despeje na forma e leve a forno
    por 50 minutos. Espere esfriar e sirva.''')

    lst_ings = [Ingredientes(nome = "milho"), 
                Ingredientes(nome = "leite"), 
                Ingredientes(nome = "açúcar"), 
                Ingredientes(nome = "ovos"), 
                Ingredientes(nome = "fermento"), 
                Ingredientes(nome = "óleo")]

    ings_rec = [IngredienteNaReceita(unidade = "lata", quantidade = 1),
                IngredienteNaReceita(unidade = "lata de milho", quantidade = 1),
                IngredienteNaReceita(unidade = "lata de milho", quantidade = 1),
                IngredienteNaReceita(unidade = "ovo", quantidade = 3),
                IngredienteNaReceita(unidade = "colher(es) de chá", quantidade = 1),
                IngredienteNaReceita(unidade = "lata de milho", quantidade = 0.5)]

    session.add(r1, lst_ings, ings_rec)
    session.commit()

    print("A tabela foi criada (se não existia) e os dados da receita foram inseridos.")
