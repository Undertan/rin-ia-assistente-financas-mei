# 🚀 Rin IA - Assistente de Empreendedorismo e Finanças para MEI

**Projeto final da trilha de IA Generativa – DIO Lab BIA do Futuro**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-green)](https://ollama.com/)

**Rin IA** é uma assistente inteligente especializada em **finanças e empreendedorismo para MEI, pequenos negócios e startups**.  
Ela analisa dados financeiros do usuário (mockados em CSV/JSON), responde perguntas contextualizadas e oferece orientações seguras, com foco em:

- Fluxo de caixa e controle de gastos
- Redução de custos operacionais
- Crédito PJ e linhas de empréstimo
- Reserva de emergência e planejamento de crescimento
- Produtos financeiros adequados para MEI

O sistema usa abordagem **híbrida** (regras determinísticas + IA local via Ollama) para garantir respostas confiáveis e minimizar alucinações.

## 🎯 Objetivo

Criar uma ferramenta prática, segura e 100% local que ajude empreendedores a tomar decisões financeiras mais conscientes, aplicando conceitos de IA generativa, Python, manipulação de dados e UX simples.

## 🚀 Funcionalidades Principais

- 📊 Resumo financeiro automático (entradas, saídas, saldo atual + gráfico mensal)
- 💬 Chat inteligente com contexto do negócio (perfil, transações, produtos)
- 🛡️ Mecanismo anti-alucinação + fallback quando faltam dados
- Lista de produtos financeiros disponíveis para MEI
- Análise personalizada baseada em dados reais (sem invenções)

## 🧠 Arquitetura Híbrida

- **Regras fixas** (no `app.py`): respostas instantâneas para perguntas comuns (produtos, dicas de economia, simulações)
- **IA local (Ollama)**: respostas complexas e personalizadas (usando modelo leve `llama3.2:1b`)
- **Filtros de validação** (no `llm.py`): bloqueia conteúdo fora do escopo ou perigoso
- **Contexto injetado**: perfil do negócio + últimas transações + histórico + produtos

## 🛠️ Tecnologias

- Python 3.10+
- Streamlit (interface web simples)
- Pandas + Matplotlib (manipulação e visualização de dados)
- Ollama (LLM local gratuito) + modelo **llama3.2:1b** (leve para notebooks comuns)
- Requests (comunicação com Ollama API)

## 📂 Estrutura do Projeto

```mermaid
mindmap
  root((rin-ia-assistente-financas-mei))
    src["src" ::icon(fa:fa-folder-open)]
      app["app.py - Interface principal (Streamlit)"]
      llm["llm.py - Lógica de IA + filtros"]
    data["data" ::icon(fa:fa-database)]
      transacoes["transacoes.csv"]
      perfil["perfil_investidor.json"]
      produtos["produtos_financeiros.json"]
      historico["historico_atendimento.csv (Opcional)"]
      investimentos["investimentos_detalhados.json"]
      dicas["dicas_economia.json"]
      simulacoes["simulacoes_rendimento.csv"]
    docs["docs" ::icon(fa:fa-book)]
      doc["documentacao-agente.md - Detalhes técnicos"]
    readme["README.md" ::icon(fa:fa-file-alt)]
    req["requirements.txt" ::icon(fa:fa-list)]

```


⚙️ Como Executar

Clone o repositório:Bashgit clone https://github.com/Undertan/rin-ia-assistente-financas-mei.git
cd rin-ia-assistente-financas-mei
Crie e ative um ambiente virtual (recomendado):Bashpython -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
Instale as dependências:Bashpip install -r requirements.txt
Inicie o Ollama em outra janela do terminal:Bashollama serve(Baixe o modelo primeiro, se ainda não tiver:)Bashollama pull llama3.2:1b
Rode a aplicação:Bashstreamlit run src/app.py
Acesse no navegador: http://localhost:8501

Nota de performance: Em notebook com 8 GB RAM (CPU only), respostas complexas demoram 15–30 segundos. Em hardware melhor (GPU), é quase instantâneo.



```markdown
## Fluxo de Interação do Usuário com Rin IA


```mermaid

graph LR
    A[Usuário] -->|faz pergunta| B[Streamlit]
    B -->|envia prompt + contexto| C[Ollama - LLM Local<br>llama3.2:1b]
    C -->|consulta / valida| D[Base de Conhecimento<br>dados mockados: CSV/JSON]
    D -->|retorna dados reais| C
    C -->|gera resposta segura| E[Resposta Educativa<br>para o usuário]
    E -->|exibe no chat| B
    B -->|mostra resposta| A

```


Esse diagrama mostra o fluxo completo:
Usuário interage via interface → Streamlit monta o prompt → Ollama processa com o modelo local → Base de Conhecimento fornece dados reais → Resposta volta educativa e segura.

💬 Exemplos de Perguntas e Respostas

Pergunta: Meu fluxo de caixa está negativo, o que faço?
Rin IA: Analisei suas últimas transações: saídas superam entradas em R$ X. Sugiro cortar gastos fixos não essenciais e buscar uma linha de crédito PJ com juros baixos. (ou pede mais detalhes se faltar info)
Pergunta: Quais produtos financeiros vocês oferecem para MEI?
Rin IA: Para MEI, temos:
Conta Digital PJ (sem tarifa)
CDB com liquidez diária
Empréstimo PJ a partir de R$ 5.000

Pergunta: Como captar investimento?
Rin IA: Baseado no seu perfil growth, prepare um pitch com: problema resolvido, TAM, tração atual e ask financeiro. Posso ajudar a simular cenários.

🛡️ Diferenciais do Projeto

IA 100% local (privacidade total, sem envio de dados para nuvem)
Respostas validadas contra alucinações e conselhos de alto risco
Contexto persistente do negócio do usuário
Totalmente alinhado ao desafio "BIA do Futuro" da DIO

📈 Próximos Passos / Melhorias Planejadas

Integração com LangChain (melhor memória e RAG)
Gráficos interativos (Plotly)
Simulador de empréstimo / projeção de caixa
Exportar relatório em PDF
Deploy na Streamlit Community Cloud (versão demo)

Capturas de Tela
Aqui estão algumas imagens reais do app rodando:
Tela inicial com resumo financeiro, gráfico e perfil do negócio
<img src="docs/screenshots/tela-inicial.png" alt="Tela Inicial">
Exemplo de pergunta sobre produtos financeiros disponíveis para MEI
<img src="docs/screenshots/produtos-mei.png" alt="Produtos para MEI">
Resposta com dicas de redução de custos fixos
<img src="docs/screenshots/reducao-custos.png" alt="Redução de Custos">
👨‍💻 Autor
Leandro da Silva – Parauapebas, PA
Estudante de IA e empreendedorismo digital
Status: 🚀 Em evolução contínua
Feito com ❤️ para empreendedores que querem crescer com segurança financeira.
Vídeo de Demonstração
O vídeo foi dividido em duas partes:
Parte 1 – Demonstração completa do app (introdução, tela inicial, funcionalidades básicas e chat simples)
<img src="https://img.youtube.com/vi/3o_yfGKsQtw/0.jpg" alt="Parte 1 - Demo Rin IA">
Parte 2 – Complemento: Resposta a pergunta complexa (exemplo de análise de fluxo negativo + plano de ação)
<img src="https://img.youtube.com/vi/M4WBA1hd4JU/0.jpg" alt="Parte 2 - Pergunta Complexa Rin IA">
Clique nas thumbnails acima para assistir (total ~5-7 minutos).
Qualquer dúvida, abra uma issue! 💬