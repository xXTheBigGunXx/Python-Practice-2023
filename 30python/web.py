import requests
from bs4 import BeautifulSoup
from typing import List

url = "https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/"

req = requests.get(url)
page = BeautifulSoup(req.content, 'html.parser')

info = page.find_all("a", class_ = "title")
year = page.find_all("span", class_ = "year")

Names:List[str] = []
Year:List[str] = []

for details in info:
    text_content = ''.join([str(item).strip() for item in details.contents if isinstance(item, str)])
    Names.append(text_content)

for i in year:
    text_content = ''.join([str(item).strip() for item in i.contents if isinstance(item, str)])
    Year.append(text_content)   

for i in range(len(Names)):
    print(f"Movie name is {Names[i]}, year is {Year[i]}.")

