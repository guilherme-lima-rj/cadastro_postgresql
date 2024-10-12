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
    # Adicionando CSS para centralizar os textos
    st.markdown(
        """
        <style>
        .centered-header {
            text-align: center;
        }
        .centered-title {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Aplicando as classes CSS aos elementos
    st.markdown('<h2 class="centered-header">Gerenciador de Clientes</h2>', unsafe_allow_html=True)
    st.markdown('<h1 class="centered-title">Bem-vindo!</h1>', unsafe_allow_html=True)

if menu == "Consultar":
    chamar_consultar()
if menu == "Inserir":
    chamar_inserir()
if menu == "Atualizar":
    chamar_atualizar()
if menu == "Deletar":
    chamar_deletar()        