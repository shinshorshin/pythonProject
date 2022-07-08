from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = "Sergey"

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys(x)
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys(x)
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys(x)

    file1 = browser.find_element(By.NAME, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file1.send_keys(file_path)

    option3 = browser.find_element(By.CLASS_NAME, "btn")
    option3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()