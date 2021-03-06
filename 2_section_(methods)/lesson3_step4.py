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

    # Найти вводные данные для вычисления
    x_value = browser.find_element_by_id("input_value")

    # Вычислить результат
    result = calc(x_value.text)

    # Найти поле ввода ответа
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(result)

    # Найти кнопку submit и отправить ответ
    confirm_button = browser.find_element_by_css_selector("button.btn-primary")
    confirm_button.click()
    
finally:
    # Десятичекундная пауза
    time.sleep(10)
    # Закрыть браузер
    browser.quit()

# Пустая строка в конце
