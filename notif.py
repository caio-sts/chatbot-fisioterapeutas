from twilio.rest import Client
import os, json

#'AC332c936836a070c76edf8c7422367e76'
#'fa4f2cf2eddb652d5b4eee31852b4876'


def notify(arq):
    account_sid = os.environ['account_sid']
    auth_token = os.environ['auth_token']
    client = Client(account_sid, auth_token)
  
    with open(f'{arq}.json', "r+") as f:
        data = json.load(f)
        data["start_message"] = "0"
        data["first_message"] = "0"
        data["second_message"] = "0"
        data["EVA"] = "1"
        data["minutos"] = data["minutos"]+1 # Depois excluir
        telefone = data["telefone"]
        json.dump(data, open(f'{arq}.json', "w+"), indent=4)
      
    client.messages.create(from_='whatsapp:+14155238886',
                           body='Olá, tem uns minutos para contar como foi seu dia de exercícios?\n1 - Sim\n2 - Não',
                           to=f'whatsapp:{telefone}')
