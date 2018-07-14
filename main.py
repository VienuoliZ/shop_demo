import requests

# Выведет HTML страницы моего курса
url = "https://api.telegram.org/bot684387669:AAGLlY7kaiNPKQaEWl1a99M4yMD4PgaAYmg/getMe"

response = requests.get(url)

# форматируем json в словарь
decoded = response.json()
print(decoded)

bot_result = decoded['result']
bot_id = bot_result['id']

# также можем сделать это сразу
bot_id = decoded['result']['id']
