from bs4 import BeautifulSoup
import requests
import time

file_path = "Desktop\projects\crypto.txt"

url = "https://www.livecoinwatch.com/"
CLEAR = "\033[2J"
CLEAR_AND_RETURN ="\033[H"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

price_list = []
name_list = []
percent_list = []
index_list =[]
change_list = []

print(CLEAR)

def Prices():

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    all_data = soup.find("tbody")
    prices = all_data.find_all(class_ = "filter-item table-item main-price")
    name_token = all_data.find_all(class_ = "abr text-truncate")
    up_down = all_data.find_all(class_ = "percent")

    index = 0
    with open(file_path , "r") as file:
        file_content = file.read().strip().split()
    for price in prices:
        price = price.text
        price = price.replace("$", "")
        price_list.append(price)
        if float(file_content[index]) < float(price):
            status = "rissen"

        if float(file_content[index]) > float(price):
            status = "fell"

        if float(file_content[index]) == float(price):
            status = "not changed"

        change = (float(price) - float(file_content[index]))
        change = abs(change)
        change_list.append(change)
        index +=1
        index_list.append(status)

    for name in name_token:
        name_list.append(name.text)

    for percent in up_down:
        percent_list.append(percent.text)

    result = zip(name_list, price_list, percent_list, index_list, change_list)
    for name, price, percent, index, change in result:
        print(f"{name}'s current price is {price}$. Change in position durring the last update is {percent} and the price has {index} by {change:.4f}")
    
    with open(file_path, "w") as files:
        for price in prices:
            price_str = str(price.get_text())
            price_str = price_str.replace("$", "")
            files.write(price_str + "\n")
    print(CLEAR_AND_RETURN)
     
Prices()