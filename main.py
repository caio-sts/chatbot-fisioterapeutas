from gevent import monkey

monkey.patch_all()

from gevent.pywsgi import WSGIServer
import json
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
#from threading import Thread
import threading
from apscheduler.schedulers.background import BackgroundScheduler
import dicasDor
import descVideoMov
import notif
from datetime import datetime
import numpy as np

sched = BackgroundScheduler()
sched.start()

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask is running now!"


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    print(request.values)
    reg = np.zeros(11, dtype=object)

    reg[0] = request.values.get('ProfileName','')
    reg[1] = request.values.get('WaId','')
    reg[2] = 1
    reg[10] = str(datetime.now()).replace(" ","_")

    arq = "control"+request.values.get('WaId', '')
  
    # Resetar o json a cada 4 minutos após a primeira interação
    t = threading.Timer(240.0, resetJson, args=[arq])
    t.start()

    # Pegar as informações do JSON
    f = open(f'{arq}.json', "r+")
    data = json.load(f)
    f.close()

    id = data["id"]
    ano = data["ano"]
    mes = data["mes"]
    dia = data["dia"]
    horas = data["horas"]
    minutos = data["minutos"]
    plano = data["plano"]
    data_notif = datetime(ano, mes, dia, horas, minutos, 10)
    
# Ativar thread da notificação 
    try:
      sched.add_job(id=id, name='teste',func=exercise_notification, trigger='date', run_date= data_notif, args=[arq], max_instances=1, next_run_time=data_notif)
    except:
      print("\n")

    # Fluxos de interação
    if '1' in incoming_msg and data["start_message"] == "1" and data["EVA"] == "0":
        msg.body("Qual o nome do exercício que você gostaria de lembrar?")
        reg[3] = 1
        with open(f'{arq}.json', "r+") as f:
            data = json.load(f)
            data["first_message"] = "1"
            json.dump(data, open(f'{arq}.json', "w"), indent=4)

    elif data["start_message"] == "1" and data["first_message"] == "1" and data["EVA"] == "0":
        remembMovVid = descVideoMov.msgVideoMov(incoming_msg)
        reg[4] = incoming_msg
      
        msg.body(remembMovVid)
        # Agradece pelo uso e reseta o json
        if "Não entendi" not in remembMovVid:
          resetJson(arq)

    elif '2' in incoming_msg and data["start_message"] == "1" and data["EVA"] == "0":
        msg.body("Em que parte do corpo você está sentindo dor?")
        reg[5] = 1
        with open(f'{arq}.json') as f:
            data = json.load(f)
            data["second_message"] = "1"
            json.dump(data, open(f'{arq}.json', "w"), indent=4)

    elif data["start_message"] == "1" and data["second_message"] == "1" and data["EVA"] == "0":
        tipMessage = dicasDor.msgDor(incoming_msg)
        reg[6] = incoming_msg
        msg.body(tipMessage)

        # Agradece pelo uso e reseta o json
        if "Não entendi" not in tipMessage:
          reg[9] = 1
          resetJson(arq)

    elif '3' in incoming_msg and data["start_message"] == "1" and data["EVA"] == "0":
        reg[7] = 1
        msg.body(
            "Vamos encaminhar o pedido para seu fisioterapeuta e ele entrará em contato. Obrigado por entrar em contato e esperamos que dê tudo certo no seu tratamento."
        )
        resetJson(arq)

    elif '4' in incoming_msg and data["start_message"] == "1" and data["EVA"] == "0":
        reg[8]
        msg.body(
            f"Segue o link do pdf com o plano de atividades.\n{plano}"
        )
        resetJson(arq)

    elif data["start_message"] == "0" and data["EVA"] == "0":
        resetJson(arq)

        msg.body(
            'Olá, para que eu possa te ajudar da melhor forma, digite o número que corresponda à sua situação atual.\n 1 - Não lembro como realizar um movimento.\n 2 - Estou sentindo dor após realizar um movimento. \n 3 - Quero falar com o fisioterapeuta. \n 4 - Plano de atividades.'
        )
        
        with open(f'{arq}.json') as f:
            data = json.load(f)
            data["start_message"] = "1"
            json.dump(data, open(f'{arq}.json', "w"), indent=4)

    elif data["EVA"] == "1" and "2" in incoming_msg:
        resetJson(arq)
        msg.body('Tudo bem. Continue a praticar seus exercícios regularmente para obter os melhores resultados!')
    
    elif data["EVA"] == "1" and "1" in incoming_msg:
      msg.body("ainda n foi configurado")# Pergunta 1 do questionário
      resetJson(arq) # Depois excluir
    elif data["EVA"] == "1" and "2" in incoming_msg:
      msg.body("ainda n foi configurado")
      resetJson(arq) # Depois excluir

    else:
      msg.body("Não entendi. Por favor, tente de novo.")
      reg[9] = 1
      resetJson(arq) # Depois excluir

    with open("registro.txt", "a+") as f:
      f.write(np.array2string(reg)+"\n")
  
      
    return str(resp)


def resetJson(arq):
    with open(f'{arq}.json', "r+") as f:
        data = json.load(f)
        data["start_message"] = "0"
        data["first_message"] = "0"
        data["second_message"] = "0"
        data["EVA"] = "0"
        json.dump(data, open(f'{arq}.json', "w+"), indent=4)


def adjustDatetime(ano, mes, dia):
    dia += 1
    if mes == 2 and dia == 29:
        mes = 3
        dia = 1
    elif mes == 2 and dia == 30:
        mes = 3
        dia = 2

    elif mes in [4, 6, 9, 11] and dia == 31:
        mes += 1
        dia = 1
    elif mes in [4, 6, 9, 11] and dia == 32:
        mes += 1
        dia = 2

    elif mes in [1, 3, 5, 7, 8, 10, 12] and dia == 32:
        mes += 1
        dia = 1
        if mes == 13:
            mes = 1
            if ano == 2022:
                ano = 2023

    elif mes in [1, 3, 5, 7, 8, 10, 12] and dia == 33:
        mes += 1
        dia = 2
        if mes == 13:
            mes = 1
            if ano == 2022:
                ano = 2023

    return ano, mes, dia


def exercise_notification(arq):
    # Checar a tabela de notificações que tem o número da pessoa, com as notificações cadastradas para cada exercício e a data-limite
    resetJson(arq)
    notif.notify(arq)

    f = open(f'{arq}.json', "r+")
    data = json.load(f)
    f.close()
  
    ano, mes, dia = adjustDatetime(data["ano"], data["mes"], data["dia"])
    with open(f'{arq}.json', "r+") as f:
        data = json.load(f)
        data["ano"] = ano
        data["mes"] = mes
        data["dia"] = dia
        json.dump(data, open(f'{arq}.json', "w+"), indent=4)

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8080), app)
    http_server.serve_forever()
