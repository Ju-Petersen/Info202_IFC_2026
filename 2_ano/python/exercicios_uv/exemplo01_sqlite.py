# importações
from pony.orm import *
import os # comandos do sistema operacional
import random

# criando variável de acesso ao pony
db = Database()

# definição da classe: 
# é preciso herdar da classe Entity
class Pessoa(db.Entity):
    nome = Required(str)   # atributo string obrigatório
    email = Required(str, 100)  # atributo string obrigatório com máximo de 100 caracteres
    telefone = Optional(str, nullable=True) # atributo opcional
    #cpf = Required(str, 11, unique=True) # atributo obrigatório com tamanho fixo e único

# usando o banco de dados SQLite
db.bind(provider='sqlite', filename='pessoas.db', create_db=True)

# innformando que deve criar as tabelas, caso não existam
db.generate_mapping(create_tables=True)

# solicitando para mostrar os comandos SQL que vão sendo executados
set_sql_debug(True)

# iniciando uma sessão
with db_session:

    # criando uma pessoa
    jo = Pessoa(nome='João da Silva', email='josilva@gmail.com') # cpf='12345678901')
    ma = Pessoa(nome='Mário do Armário', email='marionarmario@gmail.com', telefone='(11) 91234-5678') # cpf='98765432109')

    #criando várias pessoas:
    nomes = [
   'João', 'Maria', 'Pedro', 'Ana', 'Lucas',
   'Juliana', 'Carlos', 'Fernanda', 'Rafael',
   'Camila', 'Gabriel', 'Beatriz', 'Mateus',
   'Larissa', 'Bruno', 'Mariana', 'Felipe',
   'Amanda', 'Gustavo', 'Letícia'
   ]
    sobrenomes = [
    'Silva', 'Santos', 'Oliveira', 'Souza', 'Costa',
    'Pereira', 'Rodrigues', 'Almeida', 'Nascimento',
    'Lima', 'Araújo', 'Fernandes', 'Carvalho',
    'Gomes', 'Martins', 'Ribeiro', 'Alves'
        ]
    
    for i in range(10000): # i entre 10 mil pessoas:
        novo = f'{random.choice(nomes)} {random.choice(sobrenomes)}'
        # seleciona uma nova pessoa com informações 
        # variáveis dentro da lista de nomes e sobrenomes
        pessoa = Pessoa(nome=novo, email=f'pessoa{i}@gmail.com') # cria a nova pessoa (de acordo com onde i está no loop)

    # salvando
    commit()

'''
Exercícios:

1) Confira os outros tipos de dados em:
https://docs.ponyorm.org/entities.html#attribute-data-types --> FEITO

2) Pergunte em alguma IA porque o comando "print(jo.id)" funciona neste código,
já que não existe o campo "id" declarado na classe --> FEITO

3) Descomente a linha 22 e execute novamente o programa, para ver
os códigos SQL que estão sendo executados --> FEITO

4) Abra o arquivo "pessoas.db" no DBeaver e visualize a tabela e os dados --> FEITO

- contar quantos registros existem na tabela - 
- verificar se existem nomes duplicados na tabela - 
- mostrar quantas vezes cada nome aparece na tabela - 
- mostrar os nomes em ordem alfabética - 
- descobrir qual é o nome que mais se repete na tabela - 
'''