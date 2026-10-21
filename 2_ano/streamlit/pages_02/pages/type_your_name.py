import streamlit as st
from home import dados

st.title("User Interaction Page")
st.write("This is the second subpage.")

name = st.text_input("Type in your name:")
age = st.number_input("Type in your age:", step=1)

# se clicar no botão "Enviar"
if st.button("Send"):
    # se foi preenchido o nome e a idade
    if age and name:
        st.success(f"Hello, {name}! Your age is {age}.")
        st.dataframe(dados['Name'].append(name)) # os dados são exibidos em um "dataframe"
        st.dataframe(dados['Age'].append(age))
    else:
        st.warning("Please, type in your name and age.")

# se clicar no botão de "Voltar"...
if st.button("Back to Home"):
    # "vai" para a página inicial
    st.switch_page("Home.py")
