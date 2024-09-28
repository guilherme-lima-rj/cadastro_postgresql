import streamlit as st
from streamlit_option_menu import option_menu
from consultar import chamar_consultar
from inserir import chamar_inserir
from atualizar import chamar_atualizar
from deletar import chamar_deletar

st.set_page_config(
    page_title="Gerenciador de Clientes"
)

with st.sidebar:
    menu = option_menu(
        menu_title=None,
        options=["Home", "Consultar", "Inserir", "Atualizar", "Deletar"],
        styles={
            "container": {
                "padding": "0!important",
                "font-weight": "bold",
                "width": "250px",
            },
            "nav-link": {
                "font-size": "14px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#006498"},
        }
    )


if menu == "Home":
    st.header("Gerenciador de Clientes")

    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.title("Bem-vindo!")

if menu == "Consultar":
    chamar_consultar()
if menu == "Inserir":
    chamar_inserir()
if menu == "Atualizar":
    chamar_atualizar()
if menu == "Deletar":
    chamar_deletar()        