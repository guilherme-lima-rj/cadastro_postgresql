import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa as variáveis de ambiente
backend_url = os.getenv('BACKEND_URL')

def chamar_deletar():
    st.subheader("Deletar Cliente")
    id_cliente = str(st.number_input("Digite o id do Cliente:",min_value=1, format="%d"))

    # Botão para consultar cliente
    if st.button("Buscar"):
        df = pd.DataFrame()
        response = requests.get(f"{backend_url}/customer/{id_cliente}")
        if response.status_code == 200:
            customer = response.json()
            df = pd.DataFrame([customer])

            df = df[
                [
                    "id",
                    "name",
                    "surname",
                    "email",
                    "phone",
                    "created_at",
                ]
            ]

            # Concatenando Nome e Sobrenome
            df["full_name"] = df["name"] + " " + df["surname"]

            # Convertendo a coluna 'created_at' para datetime
            df["created_at"] = pd.to_datetime(df["created_at"])

            # Formatando o campo 'created_at'
            df["created_at"] = df["created_at"].dt.strftime('%Y-%m-%d %H:%M:%S')

        else:
            st.error("Cliente não encontrado!")

        if not df.empty:
            st.session_state['df_cliente_del'] = df
            st.session_state['id_cliente_del'] = id_cliente

    # Verifica se o cliente foi encontrado e exibe as informações
    if 'df_cliente_del' in st.session_state:    
        st.text_input("Nome:",value=st.session_state["df_cliente_del"].at[0,"full_name"], disabled=True, key="input_full_name")
        st.text_input("E-mail:",value=st.session_state["df_cliente_del"].at[0,"email"], disabled=True, key="input_email")
        st.text_input("Telefone:",value=st.session_state["df_cliente_del"].at[0,"phone"], disabled=True, key="input_phone")
        st.text_input("Criado em:",value=st.session_state["df_cliente_del"].at[0,"created_at"], disabled=True, key="input_created_at")      

        if st.button("Deletar Cliente"):
            response = requests.delete(f"{backend_url}/customer/{st.session_state['id_cliente_del']}")
            if response.status_code == 200:
                st.success("Cliente deletado com sucesso!")
                del st.session_state['df_cliente_del']
                del st.session_state['id_cliente_del']        
            else:
                st.error("Cliente não deletado!")