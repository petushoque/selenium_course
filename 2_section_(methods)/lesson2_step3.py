from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти вводные данные для вычисления
    treasure = browser.find_element_by_id("treasure")
    x_value = treasure.get_attribute("valuex")

    # Вычислить результат
    result = calc(x_value)

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
