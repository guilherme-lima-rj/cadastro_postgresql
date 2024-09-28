import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa as variáveis de ambiente
backend_url = os.getenv('BACKEND_URL')

def chamar_consultar():
    st.subheader("Consultar Cliente")

    response = requests.get(f"{backend_url}/customers/")
    
    if response.status_code != 200:
        st.error(f"Erro ao se conectar. Erro :{response.status_code}")
    else:
        customers = response.json()
        df = pd.DataFrame(customers)

        if df.empty:
            st.warning("Nenhum cliente cadastrado.")
            st.warning("Vá na opção 'inserir' no menu para cadastrar clientes.")    
        else:      
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

            # Convertendo a coluna 'created_at' para datetime
            df["created_at"] = pd.to_datetime(df["created_at"])

            # Formatando o campo 'created_at'
            df["created_at"] = df["created_at"].dt.strftime('%Y-%m-%d %H:%M:%S')

            with st.expander("Pesquisar Clientes"):
                options = ["Selecione uma opção:", "ID", "Nome", "Sobrenome", "Email", "Telefone"]
                selecione_busca = st.selectbox("Buscar por:", options=options)

                # Determina o estado do campo de entrada de texto
                input_desabilitado = selecione_busca == "Selecione uma opção:"

                # Determina a mensagem do text_input
                if input_desabilitado == True:
                    mensagem = "Selecione uma opção de pesquisa"
                else:
                    mensagem = f"Pesquisar cliente por {selecione_busca}:"

                # Entrada de texto para pesquisa
                buscar_nome = st.text_input(mensagem, disabled=input_desabilitado)

                consultar_cliente_bt = st.button("Consultar Cliente" , disabled=input_desabilitado)
            
                if consultar_cliente_bt:
                    # Filtrando o DataFrame com base na entrada do usuário
                    if buscar_nome.strip() == "":
                        st.warning("Digite uma valor para ser pesquisado!")
                    else:
                        df_filtrado= pd.DataFrame()
                        if not input_desabilitado and buscar_nome:
                            if selecione_busca == "Nome":
                                df_filtrado = df[df['name'].str.contains(buscar_nome, case=False, na=False)]
                            elif selecione_busca == "Sobrenome":
                                df_filtrado = df[df['surname'].str.contains(buscar_nome, case=False, na=False)]
                            elif selecione_busca == "Email":
                                df_filtrado = df[df['email'].str.contains(buscar_nome, case=False, na=False)]
                            elif selecione_busca == "Telefone":
                                df_filtrado = df[df['phone'].str.contains(buscar_nome, case=False, na=False)]
                            else:  # Assuming 'ID'
                                df_filtrado = df[df['id'].astype(str).str.contains(buscar_nome, case=False, na=False)]
                        
                    if not df_filtrado.empty:
                        df_filtrado.columns=["Id","Nome","Sobrenome","Email","Telefone","Criado em"]
                        st.dataframe(df_filtrado, hide_index=True, width=None)
                    else:
                        st.warning("Nenhum Cliente encontrado!")

            with st.expander("Buscar Todos os Clientes"):
                todos_clientes = st.button("Ver Todos os clientes")
                if todos_clientes:
                    # Exibe o DataFrame sem o índice
                    df.columns=["Id","Nome","Sobrenome","Email","Telefone","Criado em"]
                    st.dataframe(df, hide_index=True, width=None)                     
