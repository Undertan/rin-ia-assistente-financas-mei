# 🚀 Rin IA - Assistente de Empreendedorismo e Finanças

**Projeto final da trilha de IA Generativa – DIO Lab BIA do Futuro**

## 📌 Sobre o Projeto

**Rin IA** é uma assistente inteligente especializada em **empreendedorismo e finanças para pequenos negócios, MEI e startups**.  
Ela analisa dados financeiros reais do usuário, responde perguntas contextualizadas e oferece orientações seguras com foco em:

- Fluxo de caixa e controle financeiro
- Planejamento de captação de recursos
- Empréstimos PJ e linhas de crédito
- Análise básica de investimentos para crescimento

O sistema usa abordagem **híbrida** (regras determinísticas + IA local) para minimizar alucinações e garantir respostas confiáveis.

## 🎯 Objetivo

Criar uma experiência digital segura e personalizada que ajude empreendedores a tomar decisões financeiras mais conscientes, aplicando boas práticas de IA, Python, dados e UX.

## 🚀 Funcionalidades Principais

- 📊 Resumo financeiro automático (entradas, saídas, saldo)
- 💬 Chat inteligente com memória de contexto
- 🛡️ Mecanismo anti-alucinação (validação + fallback)
- 📦 Apresentação de produtos financeiros disponíveis
- 🔍 Análise contextualizada com base no perfil do empreendedor

## 🧠 Arquitetura Híbrida

- **Regras fixas** → Respostas rápidas sobre gastos e produtos
- **IA local (Ollama)** → Perguntas abertas e complexas
- **Filtro de validação** → Bloqueia respostas fora do escopo
- **Contexto injetado** → Perfil, transações, histórico e produtos

## 🛠️ Tecnologias

- Python 3.10+
- Streamlit (interface)
- Pandas (manipulação de dados)
- Ollama + modelo Phi (LLM local e gratuito)
- Requests (comunicação com Ollama)

## 📂 Estrutura do Projeto
lab-rin-ia/
├── src/
│   ├── app.py               # Interface principal (Streamlit)
│   └── llm.py               # Lógica de chamada à IA + filtros
├── data/
│   ├── transacoes.csv
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   ├── historico_atendimento.csv     (opcional – desafio DIO)
│   ├── investimentos_detalhados.json
│   ├── dicas_economia.json
│   └── simulacoes_rendimento.csv
├── docs/
│   └── documentacao-agente.md
├── README.md
└── requirements.txt
text## ⚙️ Como Executar

1. Clone o repositório
   ```bash
   git clone <seu-repo>
   cd <pasta-do-projeto>

Crie e ative ambiente virtual (recomendado)Bashpython -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
Instale dependênciasBashpip install -r requirements.txt
Inicie o modelo Ollama (em outro terminal)Bashollama run phi
Rode a aplicaçãoBashstreamlit run src/app.py

Acesse: http://localhost:8501
💬 Exemplos de Perguntas e Respostas
Pergunta: Meu fluxo de caixa está negativo, o que faço?
Rin IA: Analisei suas últimas transações: saídas superam entradas em R$ X. Sugiro cortar gastos fixos não essenciais e buscar uma linha de crédito PJ com juros baixos.
Pergunta: Quais produtos financeiros vocês oferecem para MEI?
Rin IA: Para MEI, temos:

Conta Digital PJ (sem tarifa)
CDB com liquidez diária
Empréstimo PJ a partir de R$ 5.000

Pergunta: Como captar investimento anjo?
Rin IA: Baseado no seu perfil growth, prepare um pitch com: problema resolvido, TAM, tração atual e ask financeiro. Posso ajudar a simular cenários.
🛡️ Diferenciais do Projeto

IA 100% local (privacidade total)
Respostas validadas contra alucinações
Contexto persistente do negócio do usuário
Totalmente alinhado ao desafio "BIA do Futuro" da DIO

📈 Próximos Passos / Melhorias Planejadas

Integração com LangChain (melhor memória e RAG)
Gráficos interativos (matplotlib + Plotly)
Simulador de empréstimo / projeção de caixa
Exportar relatório em PDF
Deploy na Streamlit Community Cloud

👨‍💻 Autor
Leandro – Parauapebas, PA
Estudante de IA e empreendedorismo digital
Status: 🚀 Em evolução contínua
Feito com ❤️ para empreendedores que querem crescer com segurança financeira.