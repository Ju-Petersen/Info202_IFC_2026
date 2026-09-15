from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column # classes e outros módulos para criação das tabelas

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
