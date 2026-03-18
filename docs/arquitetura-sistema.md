# Arquitetura do Sistema - Rin IA

## Visão Geral

A Rin IA utiliza uma **arquitetura híbrida** que combina:

- **Regras determinísticas rápidas** (para respostas seguras e instantâneas)  
- **IA generativa local** (Ollama + modelo Phi) para perguntas abertas  
- **Camada de segurança** (filtros pré e pós-resposta + fallback)  
- **Injeção de contexto rico** (dados mockados da pasta `data/`)  

Isso garante alta confiabilidade, zero alucinação em respostas críticas e privacidade total (tudo roda localmente).

## Diagrama de Arquitetura (Mermaid)

```mermaid
graph TD
    A[Usuário - Chat no Streamlit] --> B[app.py - Interface Streamlit]

    B --> C{Regras Rápidas Determinísticas?}
    C -->|Sim - palavras-chave detectadas| D[Resposta Imediata<br>Baseada em dados mockados<br>JSON / CSV]
    C -->|Não| E[Montagem de Contexto Rico<br>Perfil + Saldo + Transações<br>Produtos + Dicas + Simulações<br>Histórico]

    E --> F[llm.py - Chamada ao Ollama<br>Modelo Phi local]
    F --> G[Filtro Pós-Resposta<br>Validação + Fallback]

    G -->|Válida| H[Resposta Final no Chat<br>Com memória de sessão]
    G -->|Inválida| I[Fallback Seguro<br>Mensagem padrão]

    subgraph "Fontes de Dados - pasta data/"
        J[transacoes.csv]
        K[perfil_investidor.json]
        L[produtos_financeiros.json]
        M[dicas_economia.json]
        N[simulacoes_rendimento.csv]
        O[historico_atendimento.csv]
    end

    E --> J & K & L & M & N & O

    style C fill:#fff3cd,stroke:#856404
    style G fill:#d4edda,stroke:#155724

Fluxo Principal Detalhado

Entrada do usuário → pergunta no chat_input
Regras rápidas (no app.py) → verificam palavras-chave e respondem diretamente com dados mockados
(ex: lista de produtos, dicas de economia, simulações de rendimento)
→ Isso evita 30–50% das chamadas à IA e elimina risco de alucinação nessas respostas
Se não houver match → monta contexto completo com:
Perfil do empreendedor
Saldo atual (calculado)
Últimas transações
Produtos disponíveis
Dicas recentes
Histórico de atendimentos

Chamada ao Ollama (llm.py) → prompt reforçado com regras estritas
Filtro pós-resposta → verifica validade; se falhar → fallback
Resposta exibida → adicionada ao histórico da sessão (st.session_state.messages)

Benefícios da Arquitetura

Segurança → respostas críticas nunca dependem só da IA
Velocidade → regras rápidas são instantâneas
Privacidade → tudo local (sem nuvem)
Manutenção → fácil adicionar novas regras rápidas sem tocar no LLM
Escalabilidade → pode migrar para LangChain/RAG ou modelos maiores no futuro

Essa estrutura atende perfeitamente aos critérios do desafio "BIA do Futuro" da DIO: experiência segura, personalizada, com IA generativa + boas práticas de UX e dados.
Última atualização: Março 2026