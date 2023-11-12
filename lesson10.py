import requests
from bs4 import BeautifulSoup

def get_coin_price(coin_name):
    coins = {}
    response = requests.get("https://coinmarketcap.com/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        coin_list_soup = soup.find_all('div', {"class": "sc-adbfcfff-2"})
        coin_list = []

        for data in coin_list_soup:
            coin = data.find('p', {'class': "sc-4984dd93-0"}).text

            if coin == 'Tether USDt':
                coin = 'tether'
            elif coin == 'USDC':
                coin = 'usd-coin'

            coin_list.append(coin)

        for coin in coin_list:
            if coin.lower() == coin_name.lower():
                soup_list = soup.find_all("a", {"href": f"/currencies/{coin.lower()}/#markets"})
                kurs = soup_list[0].find("span").text
                coins[coin] = kurs
                break

    return coins

user_input = input("Enter the name of coin: ")
result = get_coin_price(user_input)

if result:
    print(f"The price of {user_input} is {result[user_input]}")
else:
    print(f"Couldn't find information for {user_input}")





