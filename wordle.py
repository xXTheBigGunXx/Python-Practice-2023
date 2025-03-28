from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.nytimes.com/games/wordle/index.html"

web_driver = webdriver.Chrome()
web_driver.get(url)

def continue_():
    continue_ = WebDriverWait(web_driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "purr-blocker-card__button")))
    continue_.click()

def agree():
    agree = WebDriverWait(web_driver, 5).until(EC.presence_of_element_located((By.ID,"pz-gdpr-btn-accept")))
    agree.click()

def target():
    target = WebDriverWait(web_driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "Welcome-module_button__ZG0Zh")))
    target.click()

def close():
    close = WebDriverWait(web_driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"Modal-module_closeIcon__TcEKb")))
    close.click()
def letters():
    letters = WebDriverWait(web_driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"Tile-module_tile__UWEHN")))
    letters.send_keys("a")


continue_()
agree()
target()
close()
#letters()
time.sleep(1000)