from selenium import webdriver
import time
import os
import math

# Функция для вычисления значения выражения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти и нажать прыгающую кнопку
    button = browser.find_element_by_css_selector("button.trollface")
    button.click()

    # Перейти в новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
