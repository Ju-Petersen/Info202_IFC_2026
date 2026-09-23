from sqlalchemy import create_engine, String, Text, Integer, Float, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship # classes e outros módulos para criação das tabelas
from typing import Optional, List

class Base(DeclarativeBase):
    pass
#A classe abaixo é retirada do exercicio 3receitas_2classe.py, será modificado p/ o modelo sqlalchemy:
class Receita(Base):
    __tablename__ = "tbl_receita"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(200))
    tempo_preparo: Mapped[int] = mapped_column(Integer)
    modo_preparo: Mapped[str] = mapped_column(String(500))
    
    medidas: Mapped[List["Medida"]] = relationship(back_populates="receita")
    # lista dos ingredientes já --> medidos (classe "Medida") <-- para cada receita (back_populates) !!!

class Ingredientes(Base):
    __tablename__ = "tbl_ingredientes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(150))
    
    receitas: Mapped[List["Medida"]] = relationship(back_populates="ingrediente")
    # lista do(s) ingrediente(s) --> medido (classe "Medida") <-- na receita (back_populates) !!!
    
class Medida(Base): # a classe medida é uma tabela associativa ligada com "Ingredientes" e "Receita"
    __tablename__ = "tbl_medida"
    receita_id: Mapped[int] = mapped_column(ForeignKey(Receita.id), primary_key=True)
    ingrediente_id: Mapped[int] = mapped_column(ForeignKey(Ingredientes.id), primary_key=True)
    unidade: Mapped[str] = mapped_column(String(150))
    quantidade: Mapped[int] = mapped_column(Float())

    ingrediente: Mapped[List["Ingredientes"]] = relationship(back_populates="receitas")
    # associação com receitas, de modo que cada MEDIDA (ingrediente + unidade + quatidade) está dentro da receita designada
    receita: Mapped[List["Receita"]] = relationship(back_populates="medidas")
    # associação com ingredientes, de modo que cada tipo de INGREDIENTE (nome) tenha sua MEDIDA designada

engine = create_engine("mysql+pymysql://root:root@localhost:3306/receitas_db_julia")
# comentar com o professor pois a criação com mysql+pymysql está causando erro desconhecido!!!

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

    i1 = Ingredientes(nome = "milho")
    i2 = Ingredientes(nome = "leite")
    i3 = Ingredientes(nome = "açúcar")
    i4 = Ingredientes(nome = "ovos")
    i5 = Ingredientes(nome = "fermento")
    i6 = Ingredientes(nome = "óleo")
    
    m1 = Medida(receita_id= r1, ingrediente_id= i1, unidade = "lata", quantidade = 1)
    m2 = Medida(receita_id= r1, ingrediente_id= i2, unidade = "lata de milho", quantidade = 1)
    m3 = Medida(receita_id= r1, ingrediente_id= i3, unidade = "lata de milho", quantidade = 1)
    m4 = Medida(receita_id= r1, ingrediente_id= i4, unidade = "ovo", quantidade = 3)
    m5 = Medida(receita_id= r1, ingrediente_id= i5, unidade = "colher(es) de chá", quantidade = 1)
    m6 = Medida(receita_id= r1, ingrediente_id= i6, unidade = "lata de milho", quantidade = 0.5)

    session.add(r1)
    session.commit()
    
    print("A tabela foi criada (se não existia) e os dados da receita foram inseridos.")
    print(f"A receita chamada {r1.nome} foi salva sob o número {r1.id}.")
    
    print("Ingredientes da receita:")
    for item in r1.medidas:
        print(item.ingrediente.nome, item.quantidade, item.unidade)

    