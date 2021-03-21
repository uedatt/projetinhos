import requests
import time
import telepot

bot = telepot.Bot('1479518125:AAFKZOSyFMCo75xpbAe2OtjEKmxgcf3aKfk')
url = 'https://api.telegram.org/bot1479518125:AAFKZOSyFMCo75xpbAe2OtjEKmxgcf3aKfk/getUpdates'
lista_id = []
cond = True
while cond:
    time.sleep(2)
    a = requests.post(url)
    result = a.json()
    for item in result['result']:
        id_pessoa = item['message']['from']['id']

    for item in result['result']:
        id_msg = item['message']['message_id']
    lista_id.append(id_msg)

    for item in result['result']:
        pessoa = item['message']['from']['first_name']

    for item in result['result']:
        info = item['message']['text']
    print(info)

    for item in lista_id:
        print(item,'aparece',lista_id.count(item), 'vezes')
        var_count = lista_id.count(item) 

        if var_count > 1:
            print('mensagem ja respondida')
        else:
            if info == 'oi':
                bot.sendMessage(id_pessoa,'Olá '+pessoa)
            elif info == 'bom dia':
                bot.sendMessage(id_pessoa,'bom dia '+pessoa)
            elif info == 'charles':
                bot.sendMessage(id_pessoa,'gayzão.')
            elif info == 'boa noite':
                bot.sendMessage(id_pessoa,'boa noite '+pessoa)
            elif info == 'sla':
                bot.sendMessage(id_pessoa,'num sei '+pessoa)
            elif info == 'sair':
                bot.sendMessage(id_pessoa,'saindo...')
                cond = False
                break
            time.sleep(3)
    if len(lista_id)>50:
        bot.sendMessage(id_pessoa,'Você sumiu...to saindo...')
        break
            
        
            

