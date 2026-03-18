import requests
import os
import re  # para limpeza simples de texto

def pergunta_valida(pergunta: str) -> bool:
    """Filtro básico para evitar chamadas desnecessárias ou perigosas."""
    pergunta_lower = pergunta.lower()
    proibidas = ["golpe", "fraude", "lavar dinheiro", "esquema", "pirâmide", "remédio", "doença", "cura"]
    if any(p in pergunta_lower for p in proibidas):
        return False
    return len(pergunta.strip()) > 5

def resposta_valida(resposta: str) -> bool:
    """Filtro pós-resposta: evita respostas muito curtas ou vazias."""
    if not resposta:
        return False
    if len(resposta.strip()) < 40:
        return False
    ruins = ["hotel", "viagem", "namoro", "amor", "saúde", "médico", "política"]
    if any(r in resposta.lower() for r in ruins):
        return False
    return True

def perguntar_rin(pergunta: str, contexto: str, messages_history: list) -> str:
    if not pergunta_valida(pergunta):
        return "Desculpe, não posso responder perguntas desse tipo ou que não façam sentido no contexto do seu negócio."

    # Histórico reduzido ao máximo (só últimas 2 mensagens)
    historico_str = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in messages_history[-2:]])

    # Prompt reforçado (mantido fiel à Rin IA)
    prompt = f"""Você é Rin IA, assistente financeira especializada em EMPREENDEDORISMO para MEI, pequenos negócios e startups.

REGRAS ESTRITAS (obedeça sempre, sem exceção):
- Responda exclusivamente em português brasileiro claro e direto.
- Use APENAS os dados fornecidos no contexto e no histórico. Nunca invente números, valores, produtos, taxas, nomes ou cenários.
- Nunca dê conselhos financeiros de alto risco.
- Se a pergunta for sobre algo não coberto pelos dados: responda exatamente: "Não tenho informação suficiente nos seus dados para responder com segurança. Pode me fornecer mais detalhes do seu negócio?"
- Máximo 6–8 linhas. Seja conciso, use bullets quando ajudar.
- Foque em: fluxo de caixa, controle de gastos, crédito PJ, reserva de emergência, redução de custos operacionais, planejamento de crescimento.

Contexto completo do negócio:
{contexto}

Histórico recente da conversa (use para manter coerência):
{historico_str}

Pergunta do empreendedor:
{pergunta}

Resposta da Rin IA (siga todas as regras acima):
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:1b",        # ← O MAIS LEVE POSSÍVEL (agora vai rodar rápido)
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.15,
                    "num_ctx": 2048,           # ← Reduzido ao máximo para sua RAM
                    "top_p": 0.9,
                    "top_k": 40
                }
            },
            timeout=300
        )
        response.raise_for_status()
        raw_resposta = response.json().get("response", "").strip()

        raw_resposta = re.sub(r'\n\s*\n+', '\n', raw_resposta)
        raw_resposta = raw_resposta.split("Resposta da Rin IA:")[-1].strip() if "Resposta da Rin IA:" in raw_resposta else raw_resposta

        if not resposta_valida(raw_resposta):
            return "Não encontrei dados suficientes ou a resposta não foi clara. Pode explicar melhor a situação do seu negócio?"

        return raw_resposta

    except requests.exceptions.Timeout:
        return "A pergunta foi complexa demais pro seu notebook (timeout de 5 min). Tente frases mais curtas ou simplifique."
    except requests.exceptions.ConnectionError:
        return "Não consegui conectar ao Ollama. Certifique-se de que ele está rodando em http://localhost:11434"
    except Exception as e:
        return f"Erro inesperado: {str(e)}\nTente novamente mais tarde."