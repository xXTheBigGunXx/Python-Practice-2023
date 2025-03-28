from bs4 import BeautifulSoup
import requests

new_list= []

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    
    movies = soup.find("ul", class_ = "ipc-metadata-list ipc-metadata-list--dividers-between sc-3a353071-0 wTPeg compact-list-view ipc-metadata-list--base")#.find_all("li",)
    for movie in movies:
        
        name = movie.find("div", class_ = "ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-14dd939d-7 fjdYTb cli-title").a.text
        
        year = movie.find("div", class_ = "sc-14dd939d-5 cPiUKY cli-title-metadata").span.text.strip('()')

        rate = movie.find("span", class_ = "ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").get_text(strip = True)

        print (name, year, rate)
        new_list.append([name, year, rate])

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
except requests.exceptions.RequestException as e:
    print("Error:", e)

file_path = r"C:\Users\matas\Desktop\projects\imdb250.txt"
with open(file_path, "a+", encoding="utf-8") as file:
    for item in new_list:
        file.write(", ".join(item) + "\n")