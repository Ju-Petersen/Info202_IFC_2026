# Armazenar world_map (listas) em uma database para que a 
# variável world_map acesse-a e outras funcionalidades 
# acessem apenas world_map

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column # classes e outros módulos para criação das tabelas

# classe "base"
class Base(DeclarativeBase):
    pass

class WorldMaps(Base):
    __tablename__ = "world_maps"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    rows: Mapped[int] = mapped_column(Integer)
    cols: Mapped[int] = mapped_column(Integer)

class MapTiles(Base):
    __tablename__ = "map_tiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    row: Mapped[int] = mapped_column(Integer)
    col: Mapped[int] = mapped_column(Integer)
    tile_type: Mapped[int] = mapped_column(Integer)
    # tile_type pode ser usado para defrinir se é parede (1) ou esoaço vazio (0) 
    # e futuramente algum outro tipo de parede/porta/armadilha p/ o mapa

    # Foregin Key:
    world_map_id: Mapped[int] = mapped_column(ForeignKey(WorldMaps.id))
