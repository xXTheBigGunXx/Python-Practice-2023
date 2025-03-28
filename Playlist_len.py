from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from lxml import etree
import time

time_list = []

web_driver = webdriver.Chrome()
url = "https://www.youtube.com/playlist?list=PLV3E38slEl0ltSBZ23t11a87st7EO7VOH"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
response = requests.get(url, headers=headers)
response.raise_for_status()

web_driver.get(url)
time.sleep(2)

content = web_driver.page_source.encode("utf-8").strip()
time.sleep(2)

soup = BeautifulSoup(content, "lxml")
minutes_count = 0
seconds_count = 0

playlist_title = soup.find(id = "text", class_ = "style-scope yt-dynamic-sizing-formatted-string yt-sans-28").text
print(f"Playlist title: {playlist_title}")

vidoes_info = soup.find_all(class_ = "style-scope ytd-playlist-video-list-renderer")
for video in vidoes_info:
    rank = video.find(id = "index", class_ = "style-scope ytd-playlist-video-renderer")
    artist = video.find("a", class_ = "yt-simple-endpoint style-scope yt-formatted-string")
    name = video.find(id = "video-title", class_ = "yt-simple-endpoint style-scope ytd-playlist-video-renderer")
    time_video = video.find(id = "text", class_ = "style-scope ytd-thumbnail-overlay-time-status-renderer")
    if rank or artist or name:
        print(f"{rank.text}.{name.text.strip()} by {artist.text}. Song is {time_video.text.strip()} long.")
        time_vid = time_video.text.strip().split(":")
        minutes_count += float(time_vid[0])*60
        seconds_count += float(time_vid[1])

minutes_count += float(seconds_count // 60)
seconds_count = float(seconds_count%60)
hour_count = minutes_count // 3600
minutes_count = minutes_count % 60
print(f"Playlist is {int(hour_count)} hour, {int(minutes_count)} minutes and {int(seconds_count)} seconds long.")

web_driver.quit()

