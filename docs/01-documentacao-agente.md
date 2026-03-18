# 🤖 Documentação do Agente - Rin IA

## 🧠 Descrição Geral

**Rin IA** é um agente conversacional inteligente especializado em **empreendedorismo e finanças para pequenos negócios, MEI e startups**.  

Seu principal objetivo é oferecer suporte personalizado e seguro na tomada de decisões financeiras, analisando dados reais do usuário (perfil, transações, produtos disponíveis) e minimizando riscos de respostas inventadas (alucinações).

O agente foi desenvolvido como projeto final da trilha de IA Generativa – **DIO Lab BIA do Futuro**.

## 🎯 Público-alvo

- Empreendedores individuais (MEI)
- Pequenos negócios e microempresas
- Pessoas iniciando startups ou buscando crescimento
- Quem precisa de orientação prática em fluxo de caixa, captação e crédito PJ

## ⚙️ Arquitetura e Funcionamento

### Abordagem Híbrida (Regras + IA)

O sistema combina duas camadas para maior confiabilidade:

1. **Regras determinísticas** (rápidas e 100% controladas)
   - Detecta palavras-chave como "produto", "produtos", "gasto", "gastos"
   - Responde imediatamente com cálculos reais ou listas fixas dos dados fornecidos
   - Exemplo: soma de entradas/saídas, listagem de produtos financeiros

2. **IA generativa local** (Ollama + modelo Phi)
   - Usada para perguntas abertas e mais complexas
   - Recebe **contexto rico** injetado em todo prompt:
     - Perfil do empreendedor (nome, perfil de risco, objetivo)
     - Saldo atual e últimas transações
     - Produtos financeiros disponíveis
     - Histórico recente de atendimentos (quando disponível)
   - Temperatura baixa (~0.2) para respostas mais factuais
   - Prompt de sistema reforçado com restrições anti-alucinação

3. **Camada de segurança (anti-alucinação)**
   - Filtro pós-resposta verifica comprimento mínimo e palavras fora de contexto
   - Fallback para respostas padronizadas seguras quando a IA falha
   - Nunca inventa valores, produtos ou cenários que não estejam nos dados

### Fluxo de uma interação típica

1. Usuário digita pergunta no chat
2. Sistema calcula resumo financeiro em tempo real (entradas, saídas, saldo)
3. Verifica regras rápidas (ex: menção a "produto" ou "gasto")
   - Se sim → responde imediatamente com dados reais
4. Caso contrário → monta contexto completo + histórico recente da conversa
5. Envia prompt estruturado para Ollama (localhost:11434)
6. Recebe resposta → aplica filtro de validação
7. Se inválida → usa fallback simples e seguro
8. Exibe resposta no chat com formatação markdown

## 📊 Dados Utilizados (fontes de contexto)

- `transacoes.csv` → Movimentações financeiras (entrada/saída)
- `perfil_investidor.json` → Nome, perfil de risco, objetivos do empreendedor
- `produtos_financeiros.json` → Lista de produtos/serviços disponíveis
- `historico_atendimento.csv` → (opcional) interações anteriores
- Arquivos extras (customizados): investimentos_detalhados, dicas_economia, simulacoes_rendimento

Todos os dados são carregados com tratamento de erro (arquivo inexistente não quebra a aplicação).

## 🛡️ Medidas de Segurança e Confiabilidade

- IA 100% local (Ollama) → sem envio de dados para nuvem
- Contexto sempre limitado aos dados reais do usuário
- Prompt com instruções explícitas: "Nunca invente nada", "Use apenas o contexto"
- Validação pós-resposta + fallback determinístico
- Temperatura baixa para reduzir criatividade indesejada

## 🔧 Limitações Atuais

- Depende de Ollama rodando localmente
- Modelo Phi é leve, mas pode ser menos preciso em perguntas muito complexas
- Não faz cálculos financeiros avançados (ex: projeções compostas) → planejado para próxima versão
- Memória de conversa limitada ao histórico da sessão atual

## 📈 Próximas Evoluções Planejadas

- Integração com LangChain (melhor RAG e memória longa)
- Cálculos interativos (simulador de empréstimo, projeção de fluxo de caixa)
- Gráficos (matplotlib/Plotly no Streamlit)
- Exportação de resumo em PDF
- Suporte a modelos mais potentes (Llama 3.2, Gemma 2, etc.)

---

**Versão do agente:** 1.0 (baseada na trilha BIA do Futuro – DIO)  
**Autor:** Leandro  
**Última atualização:** Março 2026

Feito com foco em ajudar empreendedores reais a crescerem com mais segurança financeira.