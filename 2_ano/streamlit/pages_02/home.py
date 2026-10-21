import streamlit as st

# configuração da página inicial:
# título e layout
st.set_page_config(page_title="Meu Aplicativo")

# título da página (H1)
st.title("Home")
# texto mostrado na página
st.write("Welcome to my Streamlit app!")

# texto usando markdown
# st.markdown("""
# Este é um exemplo de aplicação com três páginas.

# Utilize o menu lateral para navegar entre elas:
# - Página 1: apresentação de dados.
# - Página 2: interação com o usuário.
# """)

# usando o selectbox:
info = st.selectbox(
    "Select onde of the following: ", 
    ("Page 1: data listing", "Page 2: user interaction"), # opcoes que aparecem no dropdown
    index=None, placeholder="Select wich page you'd like to check"
    # enquanto a selecao for None o texto que aparece na caixa de selecao e "Utilize o menu lateral..."
)

# verificar a seleção:
st.write("You selected: ", info)

# texto de informação
st.info("Select one of the pages on sidebar menu to start.")

# dicionário contendo dados
dados = {
    "Name": ["Ana", "Bruno", "Carlos"],
    "Age": [25, 30, 28]
}
