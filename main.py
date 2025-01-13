import streamlit as st
from services.application_service import ApplicationService

# Inicializa o banco de dados (apenas na primeira execução)
from database.db_connection import initialize_db
initialize_db()

service = ApplicationService()

st.title("Gerenciador de Aplicações")

# Criar um expander para o formulário de adicionar aplicação
with st.expander("Adicionar Nova Aplicação"):
    # Formulário dentro do expander
    with st.form(key="add_app_form"):
        app_name = st.text_input("Nome da Aplicação")
        app_link = st.text_input("Link da Aplicação")
        icon_link = st.text_input("Link do Ícone")
        description = st.text_area("Descrição")
        submitted = st.form_submit_button("Adicionar")
        if submitted:
            service.add_application(app_name, app_link, icon_link, description)
            st.success("Aplicação adicionada com sucesso!")

# Inicializa o estado da busca se não estiver definido
if "search_term" not in st.session_state:
    st.session_state.search_term = ""

# Adicionar o campo de busca
search_term = st.text_input("Pesquisar Aplicações", value=st.session_state.search_term)

# Exibir um botão de reset para limpar a busca
reset_button = st.button("Resetar Busca")

# Resetar a busca quando o botão for pressionado
if reset_button:
    st.session_state.search_term = ""  # Limpar o termo de busca
    search_term = ""  # Atualizar a busca

# Atualizar o termo de busca no session_state
st.session_state.search_term = search_term

# Exibir aplicações lado a lado (5 por linha)
st.subheader("Lista de Aplicações")
applications = service.get_all_applications()

# Filtrar as aplicações com base no termo de pesquisa
if st.session_state.search_term:
    applications = [app for app in applications if st.session_state.search_term.lower() in app.app_name.lower() or st.session_state.search_term.lower() in app.description.lower()]

# Exibir as aplicações (5 por linha)
columns = st.columns(5)

for i, app in enumerate(applications):
    col = columns[i % 5]
    with col:
        # Centralizar nome e imagem, reduzir o tamanho da fonte e adicionar tooltip na descrição
        col.markdown(f"""
            <div style="text-align: center;">
                <p style="font-size: 16px; margin-bottom: 0;">
                    <a href="{app.app_link}" style="color: #00BFFF; text-decoration: none;" title="{app.description}">
                        {app.app_name}
                    </a>
                </p>
                <img src="{app.icon_link}" alt="{app.app_name}" width="50" />
            </div>
        """, unsafe_allow_html=True)
