from bs4 import BeautifulSoup
import requests
import datetime

time_today = x = datetime.datetime.now()
time_today = (f"{x:%B%w}").lower()

url = f"https://www.famousbirthdays.com/{time_today}.html"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

all_bdays = soup.find_all(class_ = "tile__item")

for bday in all_bdays:
    bday_name = bday.find(class_ = "type-16-18-small").text.strip()
    known_for = bday.find(class_ = "tile__description type-14-16").text
    if "(" in bday_name:
        index = bday_name.index("(")
        bday_name = bday_name[:index]
        print(f"{bday_name} was known for being a {known_for}")
    else:
        comma = bday_name.index(",")
        print(f"{bday_name[:comma]} is known for being a {known_for}")