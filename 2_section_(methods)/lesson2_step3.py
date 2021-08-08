from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти вводные данные для вычисления
    num_1 = browser.find_element_by_id("num1").text
    num_2 = browser.find_element_by_id("num2").text
    
    # Вычислить результат
    result = num_1 + num_2

    # Найти селектор и выбрать нужный вариант
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(result)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#спустая строка в конце
