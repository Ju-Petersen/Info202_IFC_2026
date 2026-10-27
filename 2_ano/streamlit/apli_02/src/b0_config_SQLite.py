# configurações necessárias ao banco de dados

from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import Session, mapped_column, declarative_base, Mapped

# configuração do SQLAlchemy
engine = create_engine('sqlite:///pessoas.db')

# nomeando a classe Base
Base = declarative_base()
