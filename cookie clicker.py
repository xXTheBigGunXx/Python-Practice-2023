from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://orteil.dashnet.org/cookieclicker/"

web_driver = webdriver.Chrome()
web_driver.get(url)

click_submit = WebDriverWait(web_driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "fc-button-label")))
click_submit.click()

click_lang = WebDriverWait(web_driver, 5).until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
click_lang.click()

cookie_button = WebDriverWait(web_driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))
click = 0

while click < 1000:
    cookie_button.click()
    click += 1

time.sleep(60)
web_driver.close()