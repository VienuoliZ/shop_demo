import requests

# Выведет HTML страницы моего курса
result = requests.get("https://api.cryptonator.com/api/ticker/btc-usd")
print(result.text)

