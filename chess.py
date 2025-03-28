from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

web_driver = webdriver.Chrome()

url = "https://www.chess.com/play/computer/artemisia-gentileschi"
web_driver.get(url)
sleep(4)

e2 = web_driver.find_element(By.CLASS_NAME, "square-52")
e2.click()
sleep(2)  

updated_html = web_driver.page_source
wait = WebDriverWait(web_driver, 10)
try:
    e4 = web_driver.find_element(By.CLASS_NAME, "square-54")
    e4.click()
except Exception as e:
    print("Error while clicking:", e)

web_driver.quit()

sleep(5)