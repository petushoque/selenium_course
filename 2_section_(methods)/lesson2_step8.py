from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/file_input.html"

try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти панель ввода результата и отправить результат вычислений
    input_first_name = browser.find_element_by_name("firstname")
    input_first_name.send_keys("Hello")

    # Найти кнопку и отправить ответ
    button = browser.find_element_by_tag_name("button")
    button.click()
    
finally:
    # Десятичекундная пауза
    time.sleep(10)
    # Закрыть браузер
    browser.quit()

# Пустая строка в конце
