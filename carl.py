from bs4 import BeautifulSoup
import requests

new_list= []

url = "https://www.livecoinwatch.com/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

all = soup.find("tbody")
def prices(all):
    price = soup.find(class_='filter-item table-item main-price').text
    up_down = all.find(class_ = "percent").text
    new_list.append(price)
    new_list.append(up_down)
    print (new_list)
prices(all)