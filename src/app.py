import streamlit as st
import pandas as pd
import json
import os
import matplotlib.pyplot as plt

from llm import perguntar_rin

st.set_page_config(page_title="Rin IA", page_icon="🚀", layout="wide")
st.title("🚀 Rin IA - Assistente de Empreendedorismo e Finanças")

# ===================== DADOS =====================
@st.cache_data
def carregar_dados():
    base_path = "data"
    df = pd.DataFrame()
    perfil = {}
    produtos = []
    investimentos = []
    dicas = {}
    simulacoes = pd.DataFrame()
    historico = pd.DataFrame()

    # Transações
    try:
        if os.path.exists(f"{base_path}/transacoes.csv"):
            df = pd.read_csv(f"{base_path}/transacoes.csv", on_bad_lines='skip', encoding='utf-8')
    except Exception as e:
        st.warning(f"Erro ao carregar transacoes.csv: {e}")

    # Perfil
    try:
        if os.path.exists(f"{base_path}/perfil_investidor.json"):
            perfil = json.load(open(f"{base_path}/perfil_investidor.json", encoding="utf-8"))
    except Exception as e:
        st.warning(f"Erro ao carregar perfil_investidor.json: {e}")

    # Produtos
    try:
        if os.path.exists(f"{base_path}/produtos_financeiros.json"):
            produtos = json.load(open(f"{base_path}/produtos_financeiros.json", encoding="utf-8"))
    except Exception as e:
        st.warning(f"Erro ao carregar produtos_financeiros.json: {e}")

    # Investimentos
    try:
        if os.path.exists(f"{base_path}/investimentos_detalhados.json"):
            investimentos = json.load(open(f"{base_path}/investimentos_detalhados.json", encoding="utf-8"))
    except Exception as e:
        st.warning(f"Erro ao carregar investimentos_detalhados.json: {e}")

    # Dicas
    try:
        if os.path.exists(f"{base_path}/dicas_economia.json"):
            dicas = json.load(open(f"{base_path}/dicas_economia.json", encoding="utf-8"))
    except Exception as e:
        st.warning(f"Erro ao carregar dicas_economia.json: {e}")

    # Simulações
    try:
        if os.path.exists(f"{base_path}/simulacoes_rendimento.csv"):
            simulacoes = pd.read_csv(f"{base_path}/simulacoes_rendimento.csv", on_bad_lines='skip', encoding='utf-8')
    except Exception as e:
        st.warning(f"Erro ao carregar simulacoes_rendimento.csv: {e}")

    # Histórico
    try:
        if os.path.exists(f"{base_path}/historico_atendimento.csv"):
            historico = pd.read_csv(f"{base_path}/historico_atendimento.csv", on_bad_lines='skip', encoding='utf-8')
    except Exception as e:
        st.warning(f"Erro ao carregar historico_atendimento.csv: {e}")

    return df, perfil, produtos, investimentos, dicas, simulacoes, historico

df, perfil, produtos, investimentos, dicas, simulacoes, historico = carregar_dados()

# Cálculo do resumo
entrada = df[df["tipo"] == "entrada"]["valor"].sum() if not df.empty else 0
saida = abs(df[df["tipo"] == "saida"]["valor"].sum()) if not df.empty else 0
saldo = entrada - saida

# ===================== SIDEBAR =====================
with st.sidebar:
    st.header("👤 Seu Perfil de Negócio")
    if perfil:
        st.write(f"**Nome:** {perfil.get('nome', 'Empreendedor')}")
        st.write(f"**Tipo:** {perfil.get('tipo_negocio', '-')} ({perfil.get('ramo_atividade', '-')})")
        st.write(f"**Faturamento médio mensal:** R$ {perfil.get('faturamento_mensal_medio', 0):,.2f}")
        st.write(f"**Objetivo principal:** {perfil.get('objetivo_principal', '-')}")
        st.write(f"**Necessidades atuais:** {', '.join(perfil.get('necessidades_atuais', [])) or '-'}")
    else:
        st.info("Perfil não carregado")

    st.header("💰 Produtos Disponíveis")
    if produtos:
        for p in produtos[:5]:
            st.write(f"• **{p.get('nome', '')}** ({p.get('risco', '-')})")
    else:
        st.info("Nenhum produto carregado")

# ===================== RESUMO FINANCEIRO + GRÁFICO =====================
st.subheader("📈 Resumo Financeiro do Negócio")
col1, col2, col3 = st.columns(3)
col1.metric("Entradas", f"R$ {entrada:,.2f}")
col2.metric("Saídas", f"R$ {saida:,.2f}")
col3.metric("Saldo Atual", f"R$ {saldo:,.2f}", delta=f"R$ {saldo:,.2f}", delta_color="normal" if saldo >= 0 else "inverse")

if not df.empty:
    st.subheader("Fluxo de Caixa - Últimos Registros")
    resumo_mensal = df.copy()
    resumo_mensal['data'] = pd.to_datetime(resumo_mensal['data'])
    resumo_mensal['mes'] = resumo_mensal['data'].dt.to_period('M')
    grouped = resumo_mensal.groupby(['mes', 'tipo'])['valor'].sum().unstack().fillna(0)
    grouped['saldo'] = grouped.get('entrada', 0) - grouped.get('saida', 0).abs()

    fig, ax = plt.subplots()
    grouped[['entrada', 'saida']].plot(kind='bar', ax=ax, color=['green', 'red'])
    ax.set_title("Entradas vs Saídas por Mês")
    ax.set_ylabel("R$")
    st.pyplot(fig)
else:
    st.info("Sem dados de transações para exibir gráfico.")

# ===================== CHAT =====================
st.subheader("💬 Converse com Rin IA")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! 👋 Sou a Rin IA, sua assistente para finanças e crescimento do negócio.\nComo posso ajudar hoje? (ex: fluxo de caixa, crédito PJ, investimentos, redução de custos...)"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Digite sua pergunta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    pergunta_lower = prompt.lower()
    resposta = None

    # REGRAS RÁPIDAS - com fallback mais claro
    if any(palavra in pergunta_lower for palavra in ["produto", "produtos", "oferta", "disponível", "tem para mei"]):
        if produtos:
            resposta = "Aqui estão os principais produtos financeiros disponíveis:\n\n"
            for p in produtos[:6]:
                risco = p.get('risco', '-')
                desc = p.get('descricao', 'Sem descrição detalhada')
                resposta += f"**{p.get('nome')}** ({risco}): {desc}\n\n"
        else:
            resposta = "Nenhum produto carregado no momento. Verifique o arquivo produtos_financeiros.json."

    elif any(palavra in pergunta_lower for palavra in ["economizar", "reduzir custo", "cortar gasto", "economia", "baratear"]):
        if dicas:
            categoria = "gestao_financeira_geral"
            if "fixo" in pergunta_lower:
                categoria = "reducao_custos_fixos"
            elif "marketing" in pergunta_lower:
                categoria = "marketing_e_vendas_economico"
            if categoria in dicas and dicas[categoria]:
                resposta = f"Dicas práticas para {categoria.replace('_', ' ')}:\n"
                for dica in dicas[categoria][:5]:
                    resposta += f"- {dica}\n"
                resposta += "\nQuer adaptar para o seu tipo de negócio?"
            else:
                resposta = "Não encontrei dicas específicas para essa categoria. Tente perguntar sobre 'custos fixos' ou 'marketing'."
        else:
            resposta = "Nenhuma dica de economia carregada. Verifique dicas_economia.json."

    elif "simula" in pergunta_lower or "rendimento" in pergunta_lower or "quanto rende" in pergunta_lower:
        if not simulacoes.empty:
            produto = None
            if "cdb" in pergunta_lower:
                produto = "CDB Liquidez Diária PJ"
            elif "lci" in pergunta_lower or "lca" in pergunta_lower:
                produto = "LCI/LCA PJ Isento IR"
            if produto:
                df_sim = simulacoes[simulacoes['nome_investimento'] == produto]
                if not df_sim.empty:
                    resposta = f"Simulações para **{produto}** (valor inicial R$ {df_sim['valor_inicial'].iloc[0]:,.0f}):\n"
                    for _, row in df_sim.iterrows():
                        resposta += f"- {row['periodo_meses']} meses → R$ {row['valor_final']:,.0f}\n"
                    resposta += "\nQuer simular outro valor ou produto?"
                else:
                    resposta = f"Não encontrei simulações para {produto}."
            else:
                resposta = "Especifique o produto (ex: CDB, LCI, LCA)."
        else:
            resposta = "Nenhuma simulação carregada. Verifique simulacoes_rendimento.csv."

    # Se nenhuma regra rápida pegou → chama a IA
    if resposta is None:
        contexto = f"""
Perfil do negócio:
{json.dumps(perfil, ensure_ascii=False, indent=2) if perfil else 'Perfil não carregado'}

Saldo atual: R$ {saldo:,.2f} (Entradas: R$ {entrada:,.2f} | Saídas: R$ {saida:,.2f})

Últimas transações (mais recentes):
{df.tail(4).to_string(index=False) if not df.empty else 'Sem transações'}

Produtos financeiros disponíveis:
{json.dumps([p['nome'] + ' - ' + p.get('descricao','') for p in produtos[:4]], ensure_ascii=False) if produtos else 'Nenhum produto'}

Dicas de economia recentes:
{json.dumps({k: v[:2] for k,v in dicas.items()}, ensure_ascii=False) if dicas else 'Nenhuma dica'}

Histórico recente:
{historico.tail(2).to_string(index=False) if not historico.empty else 'Sem histórico'}
"""

        resposta = perguntar_rin(prompt, contexto, st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)