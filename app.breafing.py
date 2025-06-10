import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(layout="wide", page_title="Atendimento Marcenaria - Roteiro de Vendas")

st.title("Atendimento Marcenaria - Roteiro de Vendas")

st.markdown("""
    Este roteiro de vendas é uma ferramenta para guiar o atendimento ao cliente,
    garantindo que todas as informações necessárias sejam coletadas para um projeto bem-sucedido.
    Preencha as informações abaixo e exporte para PDF ou CSV.
""")

st.markdown("---")

# --- INFORMAÇÕES DO CLIENTE ---
st.header("👤 Informações do Cliente")
nome_cliente = st.text_input("Nome Completo do Cliente:")
email_cliente = st.text_input("E-mail do Cliente:")
telefone_cliente = st.text_input("Telefone do Cliente:")
endereco_cliente = st.text_input("Endereço Completo (Rua, Número, Bairro):")
cidade_cliente = st.text_input("Cidade:")
uf_cliente = st.text_input("UF:", max_chars=2).upper() # .upper() para garantir que seja em maiúsculas

st.markdown("---")

# --- ETAPA 1: QUEBRA DE GELO E ENTRADA NO ATENDIMENTO ---
st.header("✨ ETAPA 1: Quebra de Gelo e Entrada no Atendimento")
st.markdown("_**Objetivo:** Deixar o cliente confortável e dar contexto._")

st.markdown("""
    "Seja bem-vindo(a)! Eu sou **[Seu Nome]** da **[Nome da Marcenaria]**.
    Para podermos te ajudar da melhor forma, posso te fazer algumas perguntas rápidas?"
""")

nome_marcenaria = st.text_input("Nome da Marcenaria:", "Minha Marcenaria LTDA")
seu_nome = st.text_input("Seu Nome:", "Vendedor(a) Exemplo")

st.markdown("---")

# --- ETAPA 2: PERFIL DO CLIENTE E OBJETIVO DO PROJETO ---
st.header("🎯 ETAPA 2: Perfil do Cliente e Objetivo do Projeto")

ambiente_projeto = st.radio(
    "1. Esse projeto é para qual ambiente?",
    ("Cozinha", "Quarto", "Sala", "Escritório", "Outro")
)
if ambiente_projeto == "Outro":
    ambiente_projeto_outro = st.text_input("Especifique o ambiente:")
else:
    ambiente_projeto_outro = ""

estilo_projeto = st.selectbox(
    "2. Você já tem alguma ideia do estilo que gostaria?",
    ("Ainda não sei", "Moderno", "Clássico", "Rústico", "Minimalista")
)

uso_movel = st.radio(
    "3. Esse móvel vai ser para uso próprio ou investimento (como aluguel ou revenda)?",
    ("Uso próprio", "Investimento (aluguel/revenda)")
)

ambiente_pronto = st.radio(
    "4. Você já tem o ambiente pronto ou está em reforma?",
    ("Ambiente pronto", "Em reforma")
)

st.markdown("---")

# --- ETAPA 3: DETALHAMENTO TÉCNICO E FUNCIONAL ---
st.header("📐 ETAPA 3: Detalhamento Técnico e Funcional")

medida_aproximada = st.text_input("1. Qual é a medida aproximada do ambiente? (Se não souber, oferecer visita técnica ou envio de vídeo)")

consideracao_ambiente = st.text_area("2. Tem algo no ambiente que precisa ser considerado (coluna, janela, ponto de água/luz, etc)?")

quantas_pessoas = st.text_input("3. Quantas pessoas usam esse ambiente diariamente? (Importante para ergonomia e durabilidade)")

exigencia_funcional = st.text_area("4. Tem alguma exigência funcional? (Ex: espaço para eletros, canto inteligente, gavetão, armário alto...)")

st.markdown("---")

# --- ETAPA 4: SONHOS, DESEJOS E EXPECTATIVAS ---
st.header("💭 ETAPA 4: Sonhos, Desejos e Expectativas")

referencia_pinterest = st.radio(
    "1. Tem alguma referência que você ama ou salvou do Pinterest/Instagram?",
    ("Sim", "Não")
)
if referencia_pinterest == "Sim":
    st.info("Pode pedir para o cliente enviar as referências se quiser!")

objetivo_projeto = st.selectbox(
    "2. Qual o principal objetivo com esse projeto?",
    ("Mais organização", "Visual bonito", "Valorização do imóvel", "Um sonho pessoal", "Outro")
)
if objetivo_projeto == "Outro":
    objetivo_projeto_outro = st.text_input("Especifique o principal objetivo:")
else:
    objetivo_projeto_outro = ""

frustracoes = st.multiselect(
    "3. Tem alguma frustração com móveis anteriores que gostaria de evitar?",
    ("Pouco espaço útil", "Má qualidade", "Acabamento ruim", "Demora na entrega", "Outro")
)
if "Outro" in frustracoes:
    frustracoes_outro = st.text_input("Especifique outras frustrações:")
else:
    frustracoes_outro = ""

st.markdown("---")

# --- ETAPA 5: ORÇAMENTO, PRAZO E PRÓXIMOS PASSOS ---
st.header("💲 ETAPA 5: Orçamento, Prazo e Próximos Passos")

expectativa_prazo = st.text_input("1. Você tem alguma expectativa de prazo para esse projeto?")

orcamento_estimado = st.radio(
    "2. Tem um orçamento estimado ou prefere que eu monte algo com base no melhor custo-benefício?",
    ("Tenho orçamento estimado", "Prefiro custo-benefício")
)
if orcamento_estimado == "Tenho orçamento estimado":
    valor_orcamento = st.text_input("Qual o valor do orçamento estimado?")
else:
    valor_orcamento = "Prefere custo-benefício"

preferencia_proposta = st.radio(
    "3. Prefere que a proposta seja enviada por WhatsApp ou email?",
    ("WhatsApp", "Email")
)

st.markdown("---")

# --- ETAPA FINAL: ENGAJAMENTO E ENCERRAMENTO ---
st.header("✅ ETAPA FINAL: Engajamento e Encerramento")

enviar_portfolio = st.radio(
    "1. Posso te enviar um portfólio com projetos semelhantes ao seu para você se inspirar?",
    ("Sim", "Não")
)

agendar_visita = st.radio(
    "2. Vamos agendar uma visita técnica (ou uma videochamada) para evoluirmos com o projeto?",
    ("Sim, agendar", "Não, obrigado")
)

# --- MODELO DE ENCERRAMENTO ---
st.subheader("💬 Modelo de Encerramento com Autoridade e Cuidado")
prazo_envio = st.text_input("Em até [X horas/dia] te envio nossa prévia e próximos passos, tudo bem?", "24 horas")

encerramento_final = f"""
"Muito obrigado por compartilhar suas ideias comigo. Com essas informações, consigo montar algo 100% alinhado com o que você precisa e com o padrão de qualidade que oferecemos aqui na {nome_marcenaria}. Em até {prazo_envio} te envio nossa prévia e próximos passos, tudo bem?"
"""
st.markdown(encerramento_final)

st.markdown("---")

resumo_atendimento_final = st.text_area(
    "**Resumo final da conversa (use para revisar antes do envio do projeto):**",
    height=150
)

st.markdown("---")

if st.button("Salvar e Exportar Atendimento"):
    st.success("Atendimento registrado com sucesso! Gerando arquivo para download...")

    # --- Coleta dos dados para exportação ---
    data_exportacao = {
        "Campo": [
            "Nome da Marcenaria",
            "Seu Nome (Atendente)",
            "Nome Cliente",
            "Email Cliente",
            "Telefone Cliente",
            "Endereço Cliente",
            "Cidade Cliente",
            "UF Cliente",
            "1. Ambiente do Projeto",
            "   (Outro Ambiente)",
            "2. Estilo do Projeto",
            "3. Uso do Móvel",
            "4. Ambiente Pronto/Reforma",
            "1. Medida Aproximada",
            "2. Considerações do Ambiente",
            "3. Quantidade Pessoas",
            "4. Exigência Funcional",
            "1. Referência (Pinterest/Instagram)",
            "2. Principal Objetivo",
            "   (Outro Objetivo)",
            "3. Frustrações Anteriores",
            "   (Outras Frustrações)",
            "1. Expectativa de Prazo",
            "2. Orçamento Estimado",
            "   (Valor Orçamento)",
            "3. Preferência de Envio Proposta",
            "1. Enviar Portfólio",
            "2. Agendar Visita/Videochamada",
            "Prazo de Envio da Prévia",
            "Resumo Final do Atendimento"
        ],
        "Valor": [
            nome_marcenaria,
            seu_nome,
            nome_cliente,
            email_cliente,
            telefone_cliente,
            endereco_cliente,
            cidade_cliente,
            uf_cliente,
            ambiente_projeto,
            ambiente_projeto_outro,
            estilo_projeto,
            uso_movel,
            ambiente_pronto,
            medida_aproximada,
            consideracao_ambiente,
            quantas_pessoas,
            exigencia_funcional,
            referencia_pinterest,
            objetivo_projeto,
            objetivo_projeto_outro,
            ", ".join(frustracoes), # Junta as múltiplas seleções
            frustracoes_outro,
            expectativa_prazo,
            orcamento_estimado,
            valor_orcamento,
            preferencia_proposta,
            enviar_portfolio,
            agendar_visita,
            prazo_envio,
            resumo_atendimento_final
        ]
    }

    df_export = pd.DataFrame(data_exportacao)

    # --- Exportar para CSV ---
    csv_output = df_export.to_csv(index=False, encoding='utf-8-sig') # 'utf-8-sig' para compatibilidade com Excel
    st.download_button(
        label="📥 Baixar como CSV",
        data=csv_output,
        file_name=f"atendimento_marcenaria_{nome_cliente.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        help="Baixa todas as respostas em um arquivo de planilha (CSV)."
    )

    # --- Exportar para PDF ---
    from fpdf import FPDF

    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", 'B', 15)
            self.cell(0, 10, "Roteiro de Vendas - Atendimento Marcenaria", 0, 1, 'C')
            self.ln(5)

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", 'I', 8)
            self.cell(0, 10, f"Página {self.page_no()}/{{nb}}", 0, 0, 'C')

        def chapter_title(self, title):
            self.set_font("Arial", 'B', 12)
            self.set_fill_color(220, 220, 220)
            self.cell(0, 8, title, 0, 1, 'L', 1)
            self.ln(4)

        def chapter_body(self, label, content):
            self.set_font("Arial", 'B', 10)
            self.multi_cell(0, 6, f"{label}:", 0, 'L')
            self.set_font("Arial", '', 10)
            self.multi_cell(0, 6, content if content else "Não informado", 0, 'L')
            self.ln(2)

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Adicionar as informações do Cliente ao PDF
    pdf.chapter_title("👤 Informações do Cliente")
    pdf.chapter_body("Nome Completo", nome_cliente)
    pdf.chapter_body("E-mail", email_cliente)
    pdf.chapter_body("Telefone", telefone_cliente)
    pdf.chapter_body("Endereço", endereco_cliente)
    pdf.chapter_body("Cidade/UF", f"{cidade_cliente}/{uf_cliente}")
    pdf.ln(5)

    # Adicionar as informações gerais do Atendimento ao PDF
    pdf.chapter_title("✨ Dados Gerais do Atendimento")
    pdf.chapter_body("Nome da Marcenaria", nome_marcenaria)
    pdf.chapter_body("Seu Nome (Atendente)", seu_nome)
    pdf.ln(5)

    pdf.chapter_title("🎯 ETAPA 2: Perfil do Cliente e Objetivo do Projeto")
    pdf.chapter_body("1. Ambiente do Projeto", ambiente_projeto + (f" ({ambiente_projeto_outro})" if ambiente_projeto == "Outro" else ""))
    pdf.chapter_body("2. Estilo do Projeto", estilo_projeto)
    pdf.chapter_body("3. Uso do Móvel", uso_movel)
    pdf.chapter_body("4. Ambiente Pronto/Reforma", ambiente_pronto)
    pdf.ln(5)

    pdf.chapter_title("📐 ETAPA 3: Detalhamento Técnico e Funcional")
    pdf.chapter_body("1. Medida Aproximada", medida_aproximada)
    pdf.chapter_body("2. Considerações do Ambiente", consideracao_ambiente)
    pdf.chapter_body("3. Quantidade Pessoas", quantas_pessoas)
    pdf.chapter_body("4. Exigência Funcional", exigencia_funcional)
    pdf.ln(5)

    pdf.chapter_title("💭 ETAPA 4: Sonhos, Desejos e Expectativas")
    pdf.chapter_body("1. Referência (Pinterest/Instagram)", referencia_pinterest)
    pdf.chapter_body("2. Principal Objetivo", objetivo_projeto + (f" ({objetivo_projeto_outro})" if objetivo_projeto == "Outro" else ""))
    pdf.chapter_body("3. Frustrações Anteriores", ", ".join(frustracoes) + (f" ({frustracoes_outro})" if "Outro" in frustracoes else ""))
    pdf.ln(5)

    pdf.chapter_title("💲 ETAPA 5: Orçamento, Prazo e Próximos Passos")
    pdf.chapter_body("1. Expectativa de Prazo", expectativa_prazo)
    pdf.chapter_body("2. Orçamento Estimado", orcamento_estimado + (f" ({valor_orcamento})" if orcamento_estimado == "Tenho orçamento estimado" else ""))
    pdf.chapter_body("3. Preferência de Envio Proposta", preferencia_proposta)
    pdf.ln(5)

    pdf.chapter_title("✅ ETAPA FINAL: Engajamento e Encerramento")
    pdf.chapter_body("1. Enviar Portfólio", enviar_portfolio)
    pdf.chapter_body("2. Agendar Visita/Videochamada", agendar_visita)
    pdf.chapter_body("Prazo de Envio da Prévia", prazo_envio)
    pdf.ln(5)

    pdf.chapter_title("Resumo Final do Atendimento")
    pdf.chapter_body("", resumo_atendimento_final)


    pdf_output_bytes = pdf.output(dest='S').encode('latin1') # 'S' para string em bytes, encoding para compatibilidade

    st.download_button(
        label="📄 Baixar como PDF",
        data=pdf_output_bytes,
        file_name=f"atendimento_marcenaria_{nome_cliente.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
        mime="application/pdf",
        help="Baixa um resumo formatado do atendimento em PDF."
    )