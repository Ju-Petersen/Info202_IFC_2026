from a1_modelo_simples import Pessoa, pessoas_interno

# esta função retorna a lista de pessoas
# em um formato a ser exibido pela tabela do streamlit
# está armazenada na lista interna

def retornar_pessoas_formato_tabela():
    lst_nome = []
    lst_telefone = []
    lst_email = []
    # converte a lista de objetos para um formato
    # que o streamlit consegue mostrar
    dados_no_formato = {
        for p in pessoas_interno:
            lst_nome.append(p.nome)
            lst_nome.append(p.email)
            lst_nome.append(p.telefone)
    }

    # retorna os dados
    return dados_no_formato

# esta função insere uma pessoa
def inserir_pessoa(nome : str, email : str, telefone : str):
    
    # cria uma pessoa
    nova = Pessoa(nome, email, telefone)
    
    # adiciona no cadastro interno
    pessoas_interno.append(nova)    