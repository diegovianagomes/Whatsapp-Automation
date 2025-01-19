import os
from dotenv import load_dotenv
from twilio.rest import Client
import schedule
import time
from datetime import datetime


load_dotenv()


account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

print(f"Account SID: {account_sid}")
print(f"Auth Token: {auth_token}")


client = Client(account_sid, auth_token)


mensagem_segunda = """
Bom dia! 🌞
Já são 5 da manhã e hoje é dia de treino:

**Força Total**

## Lembre-se de:
- Beber água.
- Comer algo leve.
- Se arrumar.
- Sair de casa.
- Aquecer antes.

## Seu treino de hoje é:

Foco no fortalecimento geral e ativação dos principais grupos musculares.

- **Aquecimento:** 5 minutos
- **Polichinelos:** 1 minuto
- **Corrida estacionária com elevação de joelhos:** 1 minuto
- **Mobilidade articular:** rotação de braços, quadris e tornozelos | 3 minutos

[Veja o treino completo no Notion](https://www.notion.so/Treino-Segunda-Feira-1808c45aa30180b1a629f38932c6052c?pvs=4)
"""


mensagem_quarta = """
Bom dia! 🌞
Hoje é Quarta-feira, e o treino está focado em exercícios dinâmicos para melhorar resistência e fortalecer o core.

## Lembre-se de:
- Beber água.
- Comer algo leve.
- Se arrumar.
- Sair de casa.
- Aquecer antes.

## Seu treino de hoje é:

**Aquecimento (5 minutos)**
- Polichinelos (1 minuto).
- Chutes frontais alternados (1 minuto).
- Mobilidade: inclinação lateral do tronco, rotação de quadris e alongamento dinâmico (3 minutos).

**Treino Principal (20 minutos)**
Circuito de alta intensidade: 4 rodadas, 30 segundos de exercício, 15 segundos de descanso.
- Burpees: Para explosão e resistência.
- Mountain Climbers: Para core e condicionamento.
- Prancha lateral (15 segundos por lado): Para oblíquos e estabilidade.
- Corrida estacionária com elevação de joelhos: Para cardiorrespiratório.
- Alcance alternado (em prancha): Para core e coordenação.

**Alongamento (5 minutos)**
Foque em alongar o core, os ombros e as pernas.

[Veja o treino completo no Notion](https://www.notion.so/Treino-Quarta-Feira-1808c45aa301803b9b18c7d55c8c4af5?pvs=4)
"""


mensagem_sexta = """
Bom dia! 🌞
Hoje é Sexta-feira, e o treino é mais leve, focado em fortalecer e melhorar a flexibilidade.

## Lembre-se de:
- Beber água.
- Comer algo leve.
- Se arrumar.
- Sair de casa.
- Aquecer antes.

## Seu treino de hoje é:

**Aquecimento (5 minutos)**
- Caminhada estacionária com elevação de joelhos (1 minuto).
- Movimentos circulares para braços, quadris e tornozelos (2 minutos).
- Alongamento dinâmico (2 minutos).

**Treino Principal (20 minutos)**
Circuito de força e mobilidade: 3 rodadas, 40 segundos por exercício, 20 segundos de descanso.
- Agachamento com pausa no final: Segure por 2 segundos na posição mais baixa.
- Flexão de braço lenta: Controle o movimento para foco na força.
- Pontes para glúteos: Eleve os quadris e segure por 2 segundos no topo.
- Alongamento ativo em posição de prancha: Avance o pé para frente e estique o braço oposto.
- Prancha com deslocamento: Movimente-se lateralmente enquanto mantém a posição.

**Alongamento (5 minutos)**
Alongue profundamente os quadríceps, isquiotibiais, glúteos, costas e ombros.

[Veja o treino completo no Notion](https://www.notion.so/Treino-Sexta-Feira-1808c45aa3018062ae36ec41b5cc20be?pvs=4)
"""


def enviar_mensagem_segunda():
    try:
        message = client.messages.create(
            body=mensagem_segunda,
            from_='whatsapp:+14155238886',
            to='whatsapp:+551173534426'
        )
        print(f"Mensagem de Segunda-feira enviada com sucesso! SID: {message.sid}")
    except Exception as e:
        print(f"Erro ao enviar a mensagem de Segunda-feira: {e}")


def enviar_mensagem_quarta():
    try:
        message = client.messages.create(
            body=mensagem_quarta,
            from_='whatsapp:+14155238886',
            to='whatsapp:+551173534426'
        )
        print(f"Mensagem de Quarta-feira enviada com sucesso! SID: {message.sid}")
    except Exception as e:
        print(f"Erro ao enviar a mensagem de Quarta-feira: {e}")


def enviar_mensagem_sexta():
    try:
        message = client.messages.create(
            body=mensagem_sexta,
            from_='whatsapp:+14155238886',
            to='whatsapp:+551173534426'
        )
        print(f"Mensagem de Sexta-feira enviada com sucesso! SID: {message.sid}")
    except Exception as e:
        print(f"Erro ao enviar a mensagem de Sexta-feira: {e}")


schedule.every().monday.at("05:00").do(enviar_mensagem_segunda)  
schedule.every().wednesday.at("05:00").do(enviar_mensagem_quarta)  
schedule.every().friday.at("05:00").do(enviar_mensagem_sexta)  

print("Agendador iniciado. Aguardando o horário programado...")


while True:
    schedule.run_pending()
    time.sleep(1)