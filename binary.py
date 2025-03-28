from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

number = input("What is the number you want to convert? ")
while not number.isdigit():
    number = input("Invalid input. Please enter a valid integer: ")
number = int(number)
print(f"Your number is {number}")

for x in range(0, 20):
    turned_number = int(2**x)
    if number > turned_number:
        True
    else:
        break

binary = []
for integers in range(0, x+1):
    if number % 2 == 0:
        number = number / 2
        binary.append("0")
    else:
        number = number - 1
        number = number /2
        binary.append("1")

reversed_binary_list = binary[::-1]
binary_number = ''.join(reversed_binary_list)
print(binary_number)

url = "https://www.rapidtables.com/convert/number/binary-to-decimal.html"

web_driver = webdriver.Chrome()
web_driver.get(url)

click_submit = WebDriverWait(web_driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "fc-button-label")))
click_submit.click()

input_field = WebDriverWait(web_driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "form-control.form-control-lg")))
input_field.send_keys(binary_number)

button = WebDriverWait(web_driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-success")))
button.click()

time.sleep(60)
web_driver.quit()
