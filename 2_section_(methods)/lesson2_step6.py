from selenium import webdriver
import time
import math

# Функция для вычисления значения выражения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

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
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#спустая строка в конце
