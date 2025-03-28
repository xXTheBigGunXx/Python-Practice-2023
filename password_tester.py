from selenium import webdriver
from selenium.webdriver.common.by import By

file = "Desktop/projects/password_v5.txt"

words_list = []
with open(file, "r") as word:
    content = word.read()
    words_list = content.splitlines()
lenght = len(words_list)

web_driver = webdriver.Chrome()

url = "https://www.passwordmonster.com/"

web_driver.get(url)

def time_spent():
    all = 0
    for words in words_list:
        input_field = web_driver.find_element(By.ID, "lgd_out_pg_pass")
        input_field.send_keys(words)

        time_took_element = web_driver.find_element(By.ID, "first_estimate")
        time_took = time_took_element.text

        time_value, time_unit = time_took.split()
        time_value = float(time_value)

        if time_unit == "days":
            time = time_value * 86400
        elif time_unit == "hours":
            time = time_value * 3600
        elif time_unit == "minutes":
            time = time_value * 60
        else:
            time = time_value

        all += time

        input_field.clear()
    average = float(all / lenght)
    print("{:.2f}".format(average) + "seconds")
        
time_spent()

web_driver.quit()


