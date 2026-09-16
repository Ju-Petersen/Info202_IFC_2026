from sqlalchemy import ForeignKey, String, Integer, create_engine, PrimaryKeyConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import List

# Armazenar world_map (listas) em uma database para que a 
# variável world_map acesse-a e outras funcionalidades 
# acessem apenas world_map

# classe "base"
class Base(DeclarativeBase):
    pass

class WorldMaps(Base): # classe para definir como os mapas são (a lista "world_map" no arquivo "world")
    __tablename__ = "world_maps"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    rows: Mapped[int] = mapped_column(Integer, nullable=False)
    cols: Mapped[int] = mapped_column(Integer, nullable=False)
    
    #Outra relação entre MapTiles e WorldMaps:
    tiles: Mapped[List["MapTiles"]] = relationship(back_populates="map", cascade="all, delete-orphan")
    #A lista "MapTiles" criada aqui significa que na tabela "world_maps" existe uma 
    # lista com todos os tiles do mapa x, y e/ou z, basicamente se o mapa citado no exemplo mais abaixo existe,
    # então essa lista irá conter todos os seus tiles

class MapTiles(Base):
    __tablename__ = "map_tiles"
    # Foregin Key:
    world_map_id: Mapped[int] = mapped_column(ForeignKey(WorldMaps.id), nullable=False)
    row: Mapped[int] = mapped_column(Integer, nullable=False)
    col: Mapped[int] = mapped_column(Integer, nullable=False)
    tile_type: Mapped[int] = mapped_column(Integer, nullable=False)
    # tile_type pode ser usado para defrinir se é parede (1) ou esoaço vazio (0) 
    # e futuramente algum outro tipo de parede/porta/armadilha p/ o mapa
    map: Mapped["WorldMaps"] = relationship(back_populates="tiles")
    
    #Chave primária composta!!!!
    __table_args__ = (PrimaryKeyConstraint("world_map_id", "row", "col"),)
    # os tiles são identificados pelo id do mapa + row + col, como se fossem coordenadas
    # assim, evita situações em que dois id's diferentes apontem para o mesmo tile
    
'''De acordo com as tabelas inseridas, a database manipula algo como:
world_map = [
 1 2 3               ...                        col14 --> tile_type = 1 (parede)
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], row 1 --> tile_type = 1 (parede)
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1], 
[1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1], 
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 
[1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1],  ...
[1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1], 
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 
[1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1], 
[1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1], 
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]] row 14

assim, se em col 3, row 2 o tile_type = 0, ele é vazio
bem como na col 1, row1 o tile_type = 1, ele é uma parede
esse mapa usado como exemplo pode se chamar "Mapa Principal" e ter id = 1
logo, todos os tiles com id = 1 pertencem ao "Mapa Principal"
'''

#Definir database:

engine = create_engine("sqlite:///world_models.db") #Teste inicial com sqlite p/ver o funcionamento das tbls

#Configuração para criar o arquivo de banco de dados
Base.metadata.create_all(engine)

#Abrir sessão:
with Session(engine) as session:

    world_map = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1],
[1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1],
[1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1],
[1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
    # criar o mapa
    first_map = WorldMaps(name="Mapa 1", rows=len(world_map), cols=len(world_map[0])) 
    #Utilizar diretamente as informações de world_map, ao invés de digitá-lo manualmente!!!

    # identificar o mapa, este é visto como uma matriz, assim se percorrem as rows e cols para adicioná-las em MapTiles:
    for row in range(len(world_map)): # acessar linhas em world_map
        # acessar colunas:
        for col in range(len(world_map[0])):
            # "criar um tile":
            tile = MapTiles(row=row, col=col,tile_type=world_map[row][col]) 
            # row é a linha acessada, col é a coluna acessada e tile_type identifica se está digitado como 0, 1 ou outros
            first_map.tiles.append(tile) # adicionar s "tiles" no mapa

    # adicionar os objetos na sessão
    session.add(first_map)
        
    # confirmar a inserção no banco de dados
    session.commit()

    print("Banco de dados criado (se não existia), tabela criada (se não havia) e dados inseridos no banco")
