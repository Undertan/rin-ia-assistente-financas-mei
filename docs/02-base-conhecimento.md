# 📚 Base de Conhecimento da Rin IA

A Rin IA foi projetada para oferecer respostas **seguras, confiáveis e 100% baseadas nos dados reais do usuário**.  
Ela **não possui acesso à internet**, não faz buscas externas e **nunca inventa informações**.

## 📊 Fontes de Dados Internas (únicas fontes permitidas)

Todas as respostas são construídas exclusivamente a partir destes arquivos localizados na pasta `data/`:

- **`transacoes.csv`**  
  Movimentações financeiras do negócio (entradas e saídas).  
  Usado para calcular saldo atual, analisar fluxo de caixa e identificar padrões de gastos.

- **`perfil_investidor.json`**  
  Informações pessoais e estratégicas do empreendedor:  
  - Nome  
  - Perfil de risco (conservador, moderado, arrojado)  
  - Objetivos de curto/médio/longo prazo  
  - Porte do negócio (MEI, microempresa, startup, etc.)

- **`produtos_financeiros.json`**  
  Lista completa de produtos e serviços financeiros disponíveis para oferta.  
  Exemplo: Conta PJ, CDB, empréstimo PJ, cartão de crédito empresarial, etc.

- **`historico_atendimento.csv`** (opcional)  
  Registro de interações anteriores com o usuário.  
  Ajuda a manter contexto e evitar repetição de perguntas.

- Arquivos complementares (customizados para o projeto):  
  - `investimentos_detalhados.json` → Detalhes de opções de investimento  
  - `dicas_economia.json` → Dicas práticas de redução de custos  
  - `simulacoes_rendimento.csv` → Exemplos de projeções de rendimento

## 🛡️ Regras Rígidas de Resposta (sempre obedecidas)

1. **Não inventar nada**  
   - Números, produtos, taxas, prazos ou cenários que não estejam explicitamente nos arquivos acima são proibidos.

2. **Priorizar dados reais e contexto atual**  
   - Sempre injetar no prompt: saldo calculado, últimas transações, perfil do usuário e produtos disponíveis.

3. **Respostas seguras e conservadoras**  
   - Evitar recomendações de alto risco sem base no perfil do usuário.  
   - Se faltar informação: responder com frases como  
     “Não tenho dados suficientes no seu perfil para responder com precisão. Pode me dar mais detalhes?”

4. **Idioma e tom fixos**  
   - Sempre em português brasileiro  
   - Tom motivador, direto, profissional e acessível  
   - Máximo 6–8 linhas por resposta (para clareza)

5. **Anti-alucinação reforçada**  
   - Filtro pós-resposta verifica comprimento e palavras fora de contexto  
   - Fallback para respostas padronizadas e seguras quando a IA local falhar

## 🚫 Limitações Técnicas e de Escopo

- Não possui conexão com a internet nem APIs externas  
- Não realiza cálculos financeiros avançados (ex: juros compostos complexos, análise de risco estatístico)  
- Não armazena dados entre sessões diferentes (memória limitada à conversa atual)  
- Depende do modelo Ollama local (Phi ou similar) → performance pode variar conforme hardware  
- Não substitui consultoria financeira profissional ou contabilidade

## 🔄 Como a Base de Conhecimento é Usada

1. Os arquivos são carregados no início da aplicação (com cache e tratamento de erro).  
2. Um resumo financeiro é calculado em tempo real (entradas, saídas, saldo).  
3. Todo prompt enviado à IA inclui:  
   - Perfil do empreendedor  
   - Saldo e últimas transações  
   - Produtos disponíveis  
   - Histórico recente da conversa  
4. A IA só pode “olhar” para esses dados → zero risco de informação externa ou inventada.

Essa abordagem garante que a Rin IA seja uma ferramenta **confiável e ética**, ideal para empreendedores que buscam orientação inicial segura e personalizada.

**Atualizado em:** Março 2026  
**Projeto alinhado ao desafio:** DIO Lab BIA do Futuro