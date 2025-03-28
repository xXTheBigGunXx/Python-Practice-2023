from bs4 import BeautifulSoup
import requests
import time

url = "https://time.is/"
CLEAR = "\033[2J"
CLEAR_AND_RETURN ="\033[H"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}


def clock():

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    all_data = soup.find(id = "clock0_bg")

    clock_time = all_data.find(id = "clock").text
    return clock_time

print(CLEAR)

while True:
    print(CLEAR_AND_RETURN)
    print(clock())
    time.sleep(1)