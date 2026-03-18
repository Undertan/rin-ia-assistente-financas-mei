# 🚀 Rin IA - Assistente de Empreendedorismo e Finanças para MEI

**Projeto final da trilha de IA Generativa – DIO Lab BIA do Futuro**

[<image-card alt="Python" src="https://img.shields.io/badge/Python-3.10+-blue.svg" ></image-card>](https://www.python.org/)
[<image-card alt="Streamlit" src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B.svg" ></image-card>](https://streamlit.io/)
[<image-card alt="Ollama" src="https://img.shields.io/badge/Ollama-Local%20LLM-green" ></image-card>](https://ollama.com/)

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


Fluxo de Interação do Usuário com Rin IA

```mermaid


#mermaid-diagram-mermaid-tagy6l2{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-diagram-mermaid-tagy6l2 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-diagram-mermaid-tagy6l2 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-diagram-mermaid-tagy6l2 .error-icon{fill:#a44141;}#mermaid-diagram-mermaid-tagy6l2 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-diagram-mermaid-tagy6l2 .edge-thickness-normal{stroke-width:1px;}#mermaid-diagram-mermaid-tagy6l2 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-diagram-mermaid-tagy6l2 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-diagram-mermaid-tagy6l2 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-diagram-mermaid-tagy6l2 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-diagram-mermaid-tagy6l2 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-diagram-mermaid-tagy6l2 .marker{fill:lightgrey;stroke:lightgrey;}#mermaid-diagram-mermaid-tagy6l2 .marker.cross{stroke:lightgrey;}#mermaid-diagram-mermaid-tagy6l2 svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#mermaid-diagram-mermaid-tagy6l2 p{margin:0;}#mermaid-diagram-mermaid-tagy6l2 .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#ccc;}#mermaid-diagram-mermaid-tagy6l2 .cluster-label text{fill:#F9FFFE;}#mermaid-diagram-mermaid-tagy6l2 .cluster-label span{color:#F9FFFE;}#mermaid-diagram-mermaid-tagy6l2 .cluster-label span p{background-color:transparent;}#mermaid-diagram-mermaid-tagy6l2 .label text,#mermaid-diagram-mermaid-tagy6l2 span{fill:#ccc;color:#ccc;}#mermaid-diagram-mermaid-tagy6l2 .node rect,#mermaid-diagram-mermaid-tagy6l2 .node circle,#mermaid-diagram-mermaid-tagy6l2 .node ellipse,#mermaid-diagram-mermaid-tagy6l2 .node polygon,#mermaid-diagram-mermaid-tagy6l2 .node path{fill:#1f2020;stroke:#ccc;stroke-width:1px;}#mermaid-diagram-mermaid-tagy6l2 .rough-node .label text,#mermaid-diagram-mermaid-tagy6l2 .node .label text,#mermaid-diagram-mermaid-tagy6l2 .image-shape .label,#mermaid-diagram-mermaid-tagy6l2 .icon-shape .label{text-anchor:middle;}#mermaid-diagram-mermaid-tagy6l2 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-diagram-mermaid-tagy6l2 .rough-node .label,#mermaid-diagram-mermaid-tagy6l2 .node .label,#mermaid-diagram-mermaid-tagy6l2 .image-shape .label,#mermaid-diagram-mermaid-tagy6l2 .icon-shape .label{text-align:center;}#mermaid-diagram-mermaid-tagy6l2 .node.clickable{cursor:pointer;}#mermaid-diagram-mermaid-tagy6l2 .root .anchor path{fill:lightgrey!important;stroke-width:0;stroke:lightgrey;}#mermaid-diagram-mermaid-tagy6l2 .arrowheadPath{fill:lightgrey;}#mermaid-diagram-mermaid-tagy6l2 .edgePath .path{stroke:lightgrey;stroke-width:2.0px;}#mermaid-diagram-mermaid-tagy6l2 .flowchart-link{stroke:lightgrey;fill:none;}#mermaid-diagram-mermaid-tagy6l2 .edgeLabel{background-color:hsl(0, 0%, 34.4117647059%);text-align:center;}#mermaid-diagram-mermaid-tagy6l2 .edgeLabel p{background-color:hsl(0, 0%, 34.4117647059%);}#mermaid-diagram-mermaid-tagy6l2 .edgeLabel rect{opacity:0.5;background-color:hsl(0, 0%, 34.4117647059%);fill:hsl(0, 0%, 34.4117647059%);}#mermaid-diagram-mermaid-tagy6l2 .labelBkg{background-color:rgba(87.75, 87.75, 87.75, 0.5);}#mermaid-diagram-mermaid-tagy6l2 .cluster rect{fill:hsl(180, 1.5873015873%, 28.3529411765%);stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-diagram-mermaid-tagy6l2 .cluster text{fill:#F9FFFE;}#mermaid-diagram-mermaid-tagy6l2 .cluster span{color:#F9FFFE;}#mermaid-diagram-mermaid-tagy6l2 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:hsl(20, 1.5873015873%, 12.3529411765%);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-diagram-mermaid-tagy6l2 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-diagram-mermaid-tagy6l2 rect.text{fill:none;stroke-width:0;}#mermaid-diagram-mermaid-tagy6l2 .icon-shape,#mermaid-diagram-mermaid-tagy6l2 .image-shape{background-color:hsl(0, 0%, 34.4117647059%);text-align:center;}#mermaid-diagram-mermaid-tagy6l2 .icon-shape p,#mermaid-diagram-mermaid-tagy6l2 .image-shape p{background-color:hsl(0, 0%, 34.4117647059%);padding:2px;}#mermaid-diagram-mermaid-tagy6l2 .icon-shape rect,#mermaid-diagram-mermaid-tagy6l2 .image-shape rect{opacity:0.5;background-color:hsl(0, 0%, 34.4117647059%);fill:hsl(0, 0%, 34.4117647059%);}#mermaid-diagram-mermaid-tagy6l2 :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}faz perguntaenvia prompt + contextoconsulta / validaretorna dados reaisgera resposta seguraexibe no chatmostra respostaUsuárioStreamlitOllama - LLM Local
llama3.2:1bBase de Conhecimento
dados mockados: CSV/JSONResposta Educativa
para o usuário

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

Pergunta: Como captar investimento anjo?
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
(Adicione aqui prints reais do app rodando)

Tela inicial com resumo e gráfico
Exemplo de chat com pergunta complexa
Sidebar com perfil e produtos

👨‍💻 Autor
Leandro da Silva – Parauapebas, PA
Estudante de IA e empreendedorismo digital
Status: 🚀 Em evolução contínua
Feito com ❤️ para empreendedores que querem crescer com segurança financeira.
Vídeo de Demonstração
O vídeo foi dividido em duas partes:
Parte 1 – Demonstração completa do app (introdução, tela inicial, funcionalidades básicas e chat simples)

Parte 2 – Complemento: Resposta a pergunta complexa (exemplo de análise de fluxo negativo + plano de ação)

Clique nas thumbnails acima para assistir (total ~5-7 minutos).
Qualquer dúvida, abra uma issue! 💬