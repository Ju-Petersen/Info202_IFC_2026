import streamlit as st
from home import dados

# título da página (H1)
st.title("Data Listing Page")
st.write("First subpage created in the system.")

# título de menor nível (H2)
st.subheader("Examples:")

st.dataframe(dados)

# se clicar em um botão chamado "Voltar ao início"...
if st.button("Back to Home"):
    # retorna à página inicial
    st.switch_page("Home.py")
