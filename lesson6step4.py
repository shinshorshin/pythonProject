from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import select


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    select = Select(browser.find_element(By.ID, "answer"))
    select.select_by_value(value=str(y))
    button = browser.find_element(By.CLASS_NAME, "btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
        # успеваем скопировать код за 30 секунд
    time.sleep(10)
        # закрываем браузер после всех манипуляций
    browser.quit()
