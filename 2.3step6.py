from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CLASS_NAME, "trollface")
    btn.click()
    time.sleep(1)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    time.sleep(1)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    btn = browser.find_element(By. CLASS_NAME, "btn")
    btn.click()

finally:
    print(browser.switch_to.alert.text)
    time.sleep(5)
    browser.quit()