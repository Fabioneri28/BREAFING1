import streamlit as st
import pandas as pd
import os

# --- Configurações Iniciais ---
st.set_page_config(layout="wide", page_title="Briefing de Clientes")

# Inicializa o estado da sessão para controlar as etapas e os dados
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1
if 'briefing_data' not in st.session_state:
    st.session_state.briefing_data = {}

st.title("Programa de Briefing de Clientes 📝")

# --- Funções para Navegação e Salvamento ---

def next_step():
    st.session_state.current_step += 1

def previous_step():
    st.session_state.current_step -= 1

def save_briefing_to_csv(data):
    # Define o nome do arquivo CSV
    csv_file = "briefings_clientes.csv"

    # Converte os dados para um DataFrame
    df = pd.DataFrame([data])

    # Se o arquivo já existir, lê e anexa, senão cria um novo
    if os.path.exists(csv_file):
        existing_df = pd.read_csv(csv_file)
        df = pd.concat([existing_df, df], ignore_index=True)

    df.to_csv(csv_file, index=False)
    st.success(f"Briefing salvo com sucesso em '{csv_file}'!")

# --- Etapa 1: Cadastro do Cliente ---
if st.session_state.current_step == 1:
    st.header("Etapa 1: Cadastro do Cliente")
    with st.form("cadastro_cliente_form"):
        st.session_state.briefing_data['nome'] = st.text_input("Nome Completo", value=st.session_state.briefing_data.get('nome', ''))
        st.session_state.briefing_data['endereco'] = st.text_input("Endereço (Rua, Número, Complemento)", value=st.session_state.briefing_data.get('endereco', ''))
        st.session_state.briefing_data['cidade'] = st.text_input("Cidade", value=st.session_state.briefing_data.get('cidade', ''))
        st.session_state.briefing_data['bairro'] = st.text_input("Bairro", value=st.session_state.briefing_data.get('bairro', ''))
        st.session_state.briefing_data['cep'] = st.text_input("CEP", value=st.session_state.briefing_data.get('cep', ''))
        st.session_state.briefing_data['telefone'] = st.text_input("Telefone", value=st.session_state.briefing_data.get('telefone', ''))
        st.session_state.briefing_data['email'] = st.text_input("E-mail", value=st.session_state.briefing_data.get('email', ''))

        submitted1 = st.form_submit_button("Avançar para Etapa 2")
        if submitted1:
            # Validação simples para campos obrigatórios
            if not all([st.session_state.briefing_data['nome'], st.session_state.briefing_data['telefone']]):
                st.error("Nome e Telefone são obrigatórios.")
            else:
                next_step()
                st.rerun() # Atualiza a página para mostrar a próxima etapa

# --- Etapa 2: Briefing do Imóvel e Ambiente ---
elif st.session_state.current_step == 2:
    st.header("Etapa 2: Briefing do Imóvel e Ambiente")
    with st.form("briefing_imovel_form"):
        st.session_state.briefing_data['tipo_imovel'] = st.radio(
            "Tipo de Imóvel",
            options=["Casa", "Apartamento"],
            index=0 if st.session_state.briefing_data.get('tipo_imovel') == "Casa" else 1 if st.session_state.briefing_data.get('tipo_imovel') == "Apartamento" else 0
        )
        st.session_state.briefing_data['situacao_imovel'] = st.radio(
            "Situação do Imóvel",
            options=["Própria", "Alugada"],
            index=0 if st.session_state.briefing_data.get('situacao_imovel') == "Própria" else 1 if st.session_state.briefing_data.get('situacao_imovel') == "Alugada" else 0
        )
        st.session_state.briefing_data['ambientes'] = st.multiselect(
            "Ambientes a Serem Projetados",
            options=["Cozinha", "Sala de Estar/Jantar", "Banheiro", "Dormitório", "Lavabo", "Área de Serviço", "Escritório", "Outros"],
            default=st.session_state.briefing_data.get('ambientes', [])
        )
        if "Outros" in st.session_state.briefing_data['ambientes']:
            st.session_state.briefing_data['outros_ambientes_desc'] = st.text_input("Especifique outros ambientes", value=st.session_state.briefing_data.get('outros_ambientes_desc', ''))
        else:
            st.session_state.briefing_data['outros_ambientes_desc'] = ""

        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("Voltar para Etapa 1"):
                previous_step()
                st.rerun()
        with col2:
            submitted2 = st.form_submit_button("Avançar para Etapa 3")
            if submitted2:
                next_step()
                st.rerun()

# --- Etapa 3: Preferências e Estilo ---
elif st.session_state.current_step == 3:
    st.header("Etapa 3: Preferências e Estilo")
    with st.form("preferencias_estilo_form"):
        st.session_state.briefing_data['cor_predominante'] = st.text_input(
            "Cor Predominante/Paleta de Cores",
            value=st.session_state.briefing_data.get('cor_predominante', '')
        )
        st.session_state.briefing_data['estilo'] = st.selectbox(
            "Estilo",
            options=["Moderno", "Clássico", "Minimalista", "Industrial", "Rústico", "Contemporâneo", "Outro"],
            index=["Moderno", "Clássico", "Minimalista", "Industrial", "Rústico", "Contemporâneo", "Outro"].index(st.session_state.briefing_data.get('estilo', "Moderno"))
        )
        if st.session_state.briefing_data['estilo'] == "Outro":
            st.session_state.briefing_data['outro_estilo_desc'] = st.text_input("Especifique outro estilo", value=st.session_state.briefing_data.get('outro_estilo_desc', ''))
        else:
            st.session_state.briefing_data['outro_estilo_desc'] = ""

        st.session_state.briefing_data['perfil_cliente'] = st.text_area(
            "Perfil do Cliente/Usuário (Ex: Família com crianças, pessoa solteira, gosta de cozinhar)",
            value=st.session_state.briefing_data.get('perfil_cliente', '')
        )
        st.session_state.briefing_data['material_pedra'] = st.selectbox(
            "Material de Pedra (se aplicável)",
            options=["Nenhum", "Granito", "Mármore", "Quartzo", "Porcelanato", "Outro"],
            index=["Nenhum", "Granito", "Mármore", "Quartzo", "Porcelanato", "Outro"].index(st.session_state.briefing_data.get('material_pedra', "Nenhum"))
        )
        if st.session_state.briefing_data['material_pedra'] == "Outro":
            st.session_state.briefing_data['outro_material_pedra_desc'] = st.text_input("Especifique outro material de pedra", value=st.session_state.briefing_data.get('outro_material_pedra_desc', ''))
        else:
            st.session_state.briefing_data['outro_material_pedra_desc'] = ""

        st.session_state.briefing_data['tipo_iluminacao'] = st.multiselect(
            "Tipo de Iluminação Preferida",
            options=["Luz Quente", "Luz Fria", "Luz Neutra", "Iluminação Ambiente", "Iluminação Funcional", "Iluminação Decorativa"],
            default=st.session_state.briefing_data.get('tipo_iluminacao', [])
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("Voltar para Etapa 2"):
                previous_step()
                st.rerun()
        with col2:
            submitted3 = st.form_submit_button("Avançar para Etapa 4")
            if submitted3:
                next_step()
                st.rerun()

# --- Etapa 4: Detalhamento dos Componentes dos Móveis ---
elif st.session_state.current_step == 4:
    st.header("Etapa 4: Detalhamento dos Componentes dos Móveis")
    with st.form("detalhamento_moveis_form"):
        st.session_state.briefing_data['tipo_corredicas'] = st.selectbox(
            "Tipo de Corrediças",
            options=["Telescópica", "Invisível (Oculta)", "Roller", "Não se aplica/Não sabe"],
            index=["Telescópica", "Invisível (Oculta)", "Roller", "Não se aplica/Não sabe"].index(st.session_state.briefing_data.get('tipo_corredicas', "Telescópica"))
        )
        st.session_state.briefing_data['tipo_dobradicas'] = st.selectbox(
            "Tipo de Dobradiças",
            options=["Com Amortecimento (Slow Motion)", "Sem Amortecimento", "Outro/Não sabe"],
            index=["Com Amortecimento (Slow Motion)", "Sem Amortecimento", "Outro/Não sabe"].index(st.session_state.briefing_data.get('tipo_dobradicas', "Com Amortecimento (Slow Motion)"))
        )
        if st.session_state.briefing_data['tipo_dobradicas'] == "Outro/Não sabe":
            st.session_state.briefing_data['outro_dobradica_desc'] = st.text_input("Especifique outro tipo de dobradiça", value=st.session_state.briefing_data.get('outro_dobradica_desc', ''))
        else:
            st.session_state.briefing_data['outro_dobradica_desc'] = ""

        st.session_state.briefing_data['tipo_articulador'] = st.selectbox(
            "Tipo de Articulador (para portas basculantes)",
            options=["Pistão a Gás", "Articulador Tipo Compasso", "Hettich", "Blum", "Outro/Não se aplica"],
            index=["Pistão a Gás", "Articulador Tipo Compasso", "Hettich", "Blum", "Outro/Não se aplica"].index(st.session_state.briefing_data.get('tipo_articulador', "Pistão a Gás"))
        )
        if st.session_state.briefing_data['tipo_articulador'] == "Outro/Não se aplica":
            st.session_state.briefing_data['outro_articulador_desc'] = st.text_input("Especifique outro tipo de articulador", value=st.session_state.briefing_data.get('outro_articulador_desc', ''))
        else:
            st.session_state.briefing_data['outro_articulador_desc'] = ""

        st.session_state.briefing_data['perfil_puxadores'] = st.multiselect(
            "Perfil de Puxadores",
            options=["Embutido (Cava)", "Externo (Aparente)", "Perfil Gola", "Sem puxador (fecho toque)", "Outro"],
            default=st.session_state.briefing_data.get('perfil_puxadores', [])
        )
        if "Outro" in st.session_state.briefing_data['perfil_puxadores']:
            st.session_state.briefing_data['outro_puxador_desc'] = st.text_input("Especifique outro perfil de puxador", value=st.session_state.briefing_data.get('outro_puxador_desc', ''))
        else:
            st.session_state.briefing_data['outro_puxador_desc'] = ""

        st.session_state.briefing_data['detalhe_cava'] = st.selectbox(
            "Detalhe da Cava (se aplicável)",
            options=["Cava Reta", "Cava 45 Graus", "Cava Usinada", "Não se aplica"],
            index=["Cava Reta", "Cava 45 Graus", "Cava Usinada", "Não se aplica"].index(st.session_state.briefing_data.get('detalhe_cava', "Não se aplica"))
        )
        st.session_state.briefing_data['puxador_passante'] = st.radio(
            "Puxador Passante",
            options=["Sim", "Não"],
            index=0 if st.session_state.briefing_data.get('puxador_passante') == "Sim" else 1 if st.session_state.briefing_data.get('puxador_passante') == "Não" else 1
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("Voltar para Etapa 3"):
                previous_step()
                st.rerun()
        with col2:
            submitted4 = st.form_submit_button("Finalizar Briefing e Salvar")
            if submitted4:
                save_briefing_to_csv(st.session_state.briefing_data)
                st.success("Briefing finalizado! Você pode baixar o CSV abaixo.")
                # Botão para download do CSV
                csv_file = "briefings_clientes.csv"
                if os.path.exists(csv_file):
                    with open(csv_file, "rb") as file:
                        btn = st.download_button(
                            label="Baixar CSV dos Briefings",
                            data=file,
                            file_name=csv_file,
                            mime="text/csv"
                        )
                # Reseta o formulário após salvar
                st.session_state.briefing_data = {}
                st.session_state.current_step = 1 # Volta para a primeira etapa
                st.rerun()