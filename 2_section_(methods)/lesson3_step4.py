from selenium import webdriver
import time
import os
import math

# Функция для вычисления значения выражения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти и нажать на основную кнопку
    button = browser.find_element_by_css_selector("button")
    button.click()

    # Найти и принять alert
    alert = browser.switch_to.alert
    alert.accept()
    
finally:
    # Десятичекундная пауза
    time.sleep(10)
    # Закрыть браузер
    browser.quit()

# Пустая строка в конце
