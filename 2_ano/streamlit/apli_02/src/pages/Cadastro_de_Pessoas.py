import streamlit as st
# import a2_servico_simples as s
import b2_servico_SQLite as s

# título da página (H1)
st.title("Cadastro de Pessoas")

# ----------------------
# formulário de cadastro 
# ----------------------

# agrupar em formulário
# após submeter, limpa os campos
with st.form("meu_formulario", clear_on_submit=True):
    
    # insere os campos na tela
    nome = st.text_input("Pessoa: ")
    email = st.text_input("Email: ")
    telefone = st.text_input("Telefone: ")

    # ao clicar no botão de Adicionar...
    if st.form_submit_button("Adicionar"):

        # se o nome não foi preenchido
        if nome == "":
            # mostre uma mensagem de advertência!
            st.warning("Preencha pelo menos o nome!!!")
        else:
            # adicionar a pessoa
            s.inserir_pessoa(nome, email, telefone)

# --------------------
# listagem das pessoas
# --------------------

# obter dados das pessoas em formato para tabela
dados = s.retornar_pessoas_formato_tabela()

# exibir!
st.dataframe(dados)