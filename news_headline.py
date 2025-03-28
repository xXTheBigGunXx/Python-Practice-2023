from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://abcnews.go.com/US/live-updates/trump-2020-election-indictment-charges/?id=101943446"

web_driver = webdriver.Chrome()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

title_code = soup.find_all(class_="ContentList__Item")

for headline in title_code:
    text = headline.find(class_="News__Item__Headline enableHeadlinePremiumLogo").text
    print(text)

    
