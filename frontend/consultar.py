import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()

backend_url = os.getenv('BACKEND_URL')

def chamar_consultar():
    st.subheader("Consultar Cliente")

    response = requests.get(f"{backend_url}/customers/")
    #response = requests.get("https://backend-cadastro-fj2o.onrender.com/customers/")
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
                        
            #        st.subheader("Clientes Encontrados")
                    if not df_filtrado.empty:
                        st.dataframe(df_filtrado, hide_index=True)
                    else:
                        st.warning("Nenhum Cliente encontrado!")

            with st.expander("Buscar Todos os Clientes"):
                todos_clientes = st.button("Ver Todos os clientes")
                if todos_clientes:
                    # Exibe o DataFrame sem o índice
                    st.dataframe(df, hide_index=True) 
                # else:
                #    show_response_message(response)
                    
        
    
    
    
    
    
    
    
    
    
    
#     clientes = buscar_todos_clientes()
#     df = pd.DataFrame(clientes, columns=["ID", "Nome", "Sobrenome", "Email", "Telefone"])
    
#     st.subheader("Consultar Clientes")
#     options = ["Selecione uma opção:", "ID", "Nome", "Sobrenome", "Email", "Telefone"]
#     selecione_busca = st.selectbox("Buscar por:", options=options)

#     # Determina o estado do campo de entrada de texto
#     input_desabilitado = selecione_busca == "Selecione uma opção:"

#     # Determina a mensagem do text_input
#     if input_desabilitado == True:
#         mensagem = "Selecione uma opção de pesquisa"
#     else:
#         mensagem = f"Pesquisar cliente por {selecione_busca}:"

#     # Entrada de texto para pesquisa
#     buscar_nome = st.text_input(mensagem, disabled=input_desabilitado)

#     # Filtrando o DataFrame com base na entrada do usuário
#     if not input_desabilitado and buscar_nome:
#         if selecione_busca == "Nome":
#             df_filtrado = df[df['Nome'].str.contains(buscar_nome, case=False, na=False)]
#         elif selecione_busca == "Sobrenome":
#             df_filtrado = df[df['Sobrenome'].str.contains(buscar_nome, case=False, na=False)]
#         elif selecione_busca == "Email":
#             df_filtrado = df[df['Email'].str.contains(buscar_nome, case=False, na=False)]
#         elif selecione_busca == "Telefone":
#             df_filtrado = df[df['Telefone'].str.contains(buscar_nome, case=False, na=False)]
#         else:  # Assuming 'ID'
#             df_filtrado = df[df['ID'].astype(str).str.contains(buscar_nome, case=False, na=False)]
        
#         st.subheader("Clientes Encontrados")
#         st.dataframe(df_filtrado, hide_index=True)

#         if not df_filtrado.empty:
#             pass

#         else:
#             st.write("Nenhum cliente encontrado com o critério fornecido.")
#     else:
#         st.subheader("Todos os Clientes")
#         st.dataframe(df,hide_index=True)

# elif choice == "Inserir":
#     st.subheader("Inserir Cliente")
#     nome = st.text_input("Nome")
#     sobrenome = st.text_input("Sobrenome")
#     email = st.text_input("Email")
#     telefone = st.text_input("Telefone")
#     if st.button("Inserir"):
#         inserir_cliente(nome, sobrenome, email, telefone)
#         st.success("Cliente inserido com sucesso!")

# elif choice == "Atualizar":
#     st.subheader("Atualizar Cliente")
#     busca_id = str(st.number_input("Digite o id do Cliente:",min_value=1, step=1))
#     # Botão para consultar cliente
#     if st.button("Buscar"):
#         cliente = buscar_cliente_id(busca_id)
#         if cliente:
#             st.session_state['cliente_upd'] = cliente
#             st.session_state['busca_id_upd'] = busca_id
#         else:
#             st.error("Nenhum cliente encontrado")

#     # Verifica se o cliente foi encontrado e exibe as informações
#     if 'cliente_upd' in st.session_state:
#         cliente = st.session_state['cliente_upd']
#         id, nome, sobrenome, email, telefone = cliente
        
#         # Exibindo campos editáveis
#         nome = st.text_input("Nome", value=nome)
#         sobrenome = st.text_input("Sobrenome", value=sobrenome)
#         email = st.text_input("Email", value=email)
#         telefone = st.text_input("Telefone", value=telefone)
    
#         if st.button("Atualizar"):
#             atualizar_cliente(st.session_state['busca_id_upd'], nome, sobrenome, email, telefone)
#             st.success("Cliente atualizado com sucesso!")
#             del st.session_state['cliente_upd']
#             del st.session_state['busca_id_upd']

# elif choice == "Deletar":
#     st.subheader("Deletar Cliente")
#     busca_id = str(st.number_input("Digite o id do Cliente:",min_value=1, step=1))

#     # Botão para consultar cliente
#     if st.button("Buscar"):
#         cliente = buscar_cliente_id(busca_id)
#         if cliente:
#             st.session_state['cliente_del'] = cliente
#             st.session_state['busca_id_del'] = busca_id
#         else:
#             st.error("Nenhum cliente encontrado")

#     # Verifica se o cliente foi encontrado e exibe as informações
#     if 'cliente_del' in st.session_state:
#         mostrar_cliente_del(st.session_state['cliente_del'])
#         if st.button("Deletar"):
#             deletar_cliente(st.session_state['busca_id_del'])
#             st.success("Cliente deletado com sucesso!")
#             del st.session_state['cliente_del']
#             del st.session_state['busca_id_del']