import streamlit as st
import sqlite3
import pandas as pd
from banco_dados import criar_banco

def buscar_cliente_id(id):
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute("SELECT * FROM clientes WHERE id = ?", (id))
    row = c.fetchone()
    conexao.close()
    return row

def mostrar_cliente_del(cliente):
    if cliente:
        st.text_input("ID Cliente: ", value=cliente[0], disabled=True)
        st.text_input("Nome", value=cliente[1], disabled=True)
        st.text_input("Sobrenome", value=cliente[2], disabled=True)
        st.text_input("Email", value=cliente[3], disabled=True)
        st.text_input("Telefone", value=cliente[4], disabled=True)
    else:
        st.error("Cliente não encontrado.")

def mostrar_cliente_upd(cliente):
    if cliente:
        st.text_input("ID Cliente: ", value=cliente[0], disabled=True)
        st.text_input("Nome", value=cliente[1], disabled=False)
        st.text_input("Sobrenome", value=cliente[2], disabled=False)
        st.text_input("Email", value=cliente[3], disabled=False)
        st.text_input("Telefone", value=cliente[4], disabled=False)
    else:
        st.error("Cliente não encontrado.")        

def buscar_todos_clientes():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute("SELECT * FROM clientes")
    rows = c.fetchall()
    conexao.close()
    return rows

def inserir_cliente(nome, sobrenome, email, telefone):
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute("INSERT INTO clientes (nome, sobrenome, email, telefone) VALUES (?, ?, ?, ?)",
              (nome, sobrenome, email, telefone))
    conexao.commit()
    conexao.close()

def atualizar_cliente(id, nome, sobrenome, email, telefone):
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute("UPDATE clientes SET nome = ?, sobrenome = ?, email = ?, telefone = ? WHERE id = ?",
              (nome, sobrenome, email, telefone, id))
    conexao.commit()
    conexao.close()

def deletar_cliente(id):
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

criar_banco()
st.set_page_config(
    page_title="Cadastro de Clientes"
)
st.subheader("SISTEMA DE CADASTRO DE CLIENTES")

# Estilizando o menu fixo à esquerda
st.markdown("""
    <style>
     .sidebar .sidebar-content h1 {
        font-size: 26px;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown("<h1>Menu</h1>", unsafe_allow_html=True)

menu = ["Consultar","Inserir","Atualizar","Deletar"]
choice = st.sidebar.radio("", menu)

if choice == "Consultar":
    clientes = buscar_todos_clientes()
    df = pd.DataFrame(clientes, columns=["ID", "Nome", "Sobrenome", "Email", "Telefone"])
    
    st.subheader("Consultar Clientes")
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
    bucar_nome = st.text_input(mensagem, disabled=input_desabilitado)

    # Filtrando o DataFrame com base na entrada do usuário
    if not input_desabilitado and bucar_nome:
        if selecione_busca == "Nome":
            df_filtrado = df[df['Nome'].str.contains(bucar_nome, case=False, na=False)]
        elif selecione_busca == "Sobrenome":
            df_filtrado = df[df['Sobrenome'].str.contains(bucar_nome, case=False, na=False)]
        elif selecione_busca == "Email":
            df_filtrado = df[df['Email'].str.contains(bucar_nome, case=False, na=False)]
        elif selecione_busca == "Telefone":
            df_filtrado = df[df['Telefone'].str.contains(bucar_nome, case=False, na=False)]
        else:  # Assuming 'ID'
            df_filtrado = df[df['ID'].astype(str).str.contains(bucar_nome, case=False, na=False)]
        
        st.subheader("Clientes Encontrados")
        st.dataframe(df_filtrado, hide_index=True)

        if not df_filtrado.empty:
            pass

        else:
            st.write("Nenhum cliente encontrado com o critério fornecido.")
    else:
        st.subheader("Todos os Clientes")
        st.dataframe(df,hide_index=True)

elif choice == "Inserir":
    st.subheader("Inserir Cliente")
    nome = st.text_input("Nome")
    sobrenome = st.text_input("Sobrenome")
    email = st.text_input("Email")
    telefone = st.text_input("Telefone")
    if st.button("Inserir"):
        inserir_cliente(nome, sobrenome, email, telefone)
        st.success("Cliente inserido com sucesso!")

elif choice == "Atualizar":
    st.subheader("Atualizar Cliente")
    busca_id = str(st.number_input("Digite o id do Cliente:",min_value=1, step=1))
    # Botão para consultar cliente
    if st.button("Buscar"):
        cliente = buscar_cliente_id(busca_id)
        if cliente:
            st.session_state['cliente_upd'] = cliente
            st.session_state['busca_id_upd'] = busca_id
        else:
            st.error("Nenhum cliente encontrado")

    # Verifica se o cliente foi encontrado e exibe as informações
    if 'cliente_upd' in st.session_state:
        cliente = st.session_state['cliente_upd']
        id, nome, sobrenome, email, telefone = cliente
        
        # Exibindo campos editáveis
        nome = st.text_input("Nome", value=nome)
        sobrenome = st.text_input("Sobrenome", value=sobrenome)
        email = st.text_input("Email", value=email)
        telefone = st.text_input("Telefone", value=telefone)
    
        if st.button("Atualizar"):
            atualizar_cliente(st.session_state['busca_id_upd'], nome, sobrenome, email, telefone)
            st.success("Cliente atualizado com sucesso!")
            del st.session_state['cliente_upd']
            del st.session_state['busca_id_upd']

elif choice == "Deletar":
    st.subheader("Deletar Cliente")
    busca_id = str(st.number_input("Digite o id do Cliente:",min_value=1, step=1))

    # Botão para consultar cliente
    if st.button("Buscar"):
        cliente = buscar_cliente_id(busca_id)
        if cliente:
            st.session_state['cliente_del'] = cliente
            st.session_state['busca_id_del'] = busca_id
        else:
            st.error("Nenhum cliente encontrado")

    # Verifica se o cliente foi encontrado e exibe as informações
    if 'cliente_del' in st.session_state:
        mostrar_cliente_del(st.session_state['cliente_del'])
        if st.button("Deletar"):
            deletar_cliente(st.session_state['busca_id_del'])
            st.success("Cliente deletado com sucesso!")
            del st.session_state['cliente_del']
            del st.session_state['busca_id_del']