import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa as variáveis de ambiente
backend_url = os.getenv('BACKEND_URL')

def chamar_atualizar():
    st.subheader("Atualizar Cliente")
    id_cliente = str(st.number_input("Digite o id do Cliente:",min_value=1, format="%d"))

    # Botão para consultar cliente
    buscar_cliente_bt = st.button("Buscar")

    if buscar_cliente_bt:
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
            st.session_state['df_cliente_upd'] = df
            st.session_state['id_cliente_upd'] = id_cliente

    # Verifica se o cliente foi encontrado e exibe as informações
    if 'df_cliente_upd' in st.session_state: 
        with st.form("update_customer"):
            col1,col2=st.columns([2,3])
            with col1:
                new_name=st.text_input("Nome:",value=st.session_state["df_cliente_upd"].at[0,"name"], disabled=False, key="input_name")
                new_email=st.text_input("E-mail:",value=st.session_state["df_cliente_upd"].at[0,"email"], disabled=False, key="input_email")    
            with col2:
                new_surname=st.text_input("Sobrenome:",value=st.session_state["df_cliente_upd"].at[0,"surname"], disabled=False, key="input_surname")       
                new_phone=st.text_input("Telefone:",value=st.session_state["df_cliente_upd"].at[0,"phone"], disabled=False, key="input_phone")        

            atualizar_cliente_bt = st.form_submit_button("Atualizar Cliente")
            
            if atualizar_cliente_bt:
                cliente_atualizado = {}
                cliente_atualizado["name"] = new_name
                cliente_atualizado["surname"] = new_surname
                cliente_atualizado["email"] = new_email
                cliente_atualizado["phone"] = new_phone
            
                if cliente_atualizado:
                    response = requests.put(
                            f"{backend_url}/customer/{st.session_state['id_cliente_upd']}", json=cliente_atualizado
                        )            
                    
                    if response.status_code == 200:
                        st.success("Cliente atualizado com sucesso!")
                        del st.session_state['df_cliente_upd']
                        del st.session_state['id_cliente_upd'] 
                    else:
                        st.error("Erro ao atualizar cliente.")