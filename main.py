import requests
from config import token
url = 'https://api.telegram.org/bot'
defaut_message = 'Я бот, который покажет вам стоимоть Bitcoin и Ethereum в Euro \n\nKоманды:\n /btc - цена за Bitcoin\n /eth - цена за Ethereum'

# Function for updates
def get_bot_updates(limit, offset):
    method_url = url + token + '/getUpdates'

    # записываем параметры в словарь
    par = {'limit': limit, 'offset': offset}
    
    # передаем словарь в аргумент функции
    result = requests.get(method_url, params=par)
    
    # форматируем json в словарь
    decoded = result.json()
    return decoded['result']

def sendMessage(chat_id, text):
    method_url = url + token + '/sendMessage'
    par = {'chat_id': chat_id, 'text': text}
    requests.post(method_url, params=par)

# Function to get Cryptocurrencies exchange rates
def get_crypto_rates(currency):
    param = currency + '-eur'
    method_url = 'https://api.cryptonator.com/api/ticker/'+param
    result = requests.get(method_url)
    # форматируем json в словарь
    decoded = result.json()
    result = decoded['ticker']
    return result['price']

def listenBot(offset):
    result = get_bot_updates(5, offset)
    chat_id = item['message']['chat']['id']
    text = item['message']['text']
    if text == '/start':
        text = defaut_message
        sendMessage(chat_id, text)
    elif text == '/btc':
        text = '1 биткойн стоит ' + get_crypto_rates('btc') + ' Eur.'
        sendMessage(chat_id, text)
    elif text == '/eth':
        text = '1 эфириум стоит ' + get_crypto_rates('etc') + ' Eur.'
        sendMessage(chat_id, text)

while True:
    result = get_bot_updates(5, 0)
    for item in result:
        text = item['message']['text']
        update_id = item['update_id']
        new_offset = update_id + 1
        listenBot(new_offset)
        break
