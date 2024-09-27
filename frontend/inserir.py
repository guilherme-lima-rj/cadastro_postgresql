import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()

backend_url = os.getenv('BACKEND_URL')

def chamar_inserir():
    st.subheader("Inserir Cliente")

    with st.form("new_customer"):
        name = st.text_input("Nome", key="name_input")
        surname = st.text_input("Sobrenome", key="surname_input")
        email = st.text_input("Email", key="email_input")
        phone = st.text_input("Telefone", key="phone_input")
        inserir_cliente_bt = st.form_submit_button("Inserir Cliente")

        if inserir_cliente_bt:
            if not name.strip() or not surname.strip() or not phone.strip():
                st.error("Os campos Nome, Sobrenome e Telefone, não podem estar vazios!")
            else:
                response = requests.post(
                    f"{backend_url}/customer/",
                    json={
                        "name": name,
                        "surname": surname,
                        "email": email,
                        "phone": phone,                    
                    },
                )
                if response.status_code == 200:
                    st.success("Cliente Inserido com sucesso!")
                else:
                    st.error("Erro ao tentar inserir cliente.")