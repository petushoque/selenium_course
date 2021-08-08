from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

def sum_func(a, b):
  return a + b

try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти вводные данные для вычисления
    num_1 = browser.find_element_by_id("num1")
    num_2 = browser.find_element_by_id("num2")
    
    # Вычислить результат
    result = sum_func(num_1.text, num_2.text)

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
