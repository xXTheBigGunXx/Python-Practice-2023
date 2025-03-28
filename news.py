from bs4 import BeautifulSoup
import requests

url = "https://www.delfi.lt/archive/latest.php"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

headline = soup.find(class_ = "CBarticleTitle")

print (headline.string)


