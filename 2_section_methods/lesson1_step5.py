from selenium import webdriver
import time

import math

# Функция для вычисления значения выражения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти вводные данные для вычисления
    x_value = browser.find_element_by_id("input_value")

    # Вычислить результат
    result = calc(x_value.text)

    # Найти поле ввода ответа
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(result)

    # Отметить чекбокс
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    # Отметить радиокнопку
    robot_radio = browser.find_element_by_id("robotsRule")
    robot_radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#спустая строка в конце
