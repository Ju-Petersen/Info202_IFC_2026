from b0_config_SQLite import *
from b1_modelo_SQLite import Pessoa

def retornar_pessoas_formato_tabela():
    
    # abrir a sessão do banco de dados
    with Session(engine) as session:

        # obtém as pessoas do banco de dados
        pessoas_interno = session.scalars(select(Pessoa)).all()

        # formata os dados para mostrar na camada de visão
        dados_no_formato = {
            "Nome": [p.nome for p in pessoas_interno],
            "Email": [p.email for p in pessoas_interno],
            "Telefone": [p.telefone for p in pessoas_interno]
        }
    
    # retorna os dados prontinhos para mostrar na visão
    return dados_no_formato

# esta função insere uma pessoa no banco de dados
def inserir_pessoa(nome : str, email : str, telefone : str):
    
    # cria uma pessoa
    nova = Pessoa(nome=nome, email=email, telefone=telefone)
    
    # abrir a sessão do banco de dados
    with Session(engine) as session:
        
        # insere o objeto na sessão e grava
        session.add(nova)
        session.commit()