from b0_config_SQLite import *

# definição da classe
class Pessoa(Base):
    __tablename__ = 'pessoas'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    email: Mapped[str] = mapped_column(String(250))
    telefone: Mapped[str] = mapped_column(String(50))

# criando o banco de dados e as tabelas do SQLite,
# se ainda não existirem
Base.metadata.create_all(engine)