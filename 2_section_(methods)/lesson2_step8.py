from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/file_input.html"

try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти вводные данные для вычисления
    x_value = browser.find_element_by_id("input_value")

    # Вычислить значение выражения
    result = calc(x_value.text)

    # Найти панель ввода результата и отправить результат вычислений
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(result)

    # Найти чекбокс, пролистать до него страницу и поставить флажок
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    # Отметить радиокнопку
    robot_radio = browser.find_element_by_id("robotsRule")
    robot_radio.click()

    # Найти кнопку и отправить ответ
    button = browser.find_element_by_tag_name("button")
    button.click()
    
finally:
    # Десятичекундная пауза
    time.sleep(10)
    # Закрыть браузер
    browser.quit()

# Пустая строка в конце
