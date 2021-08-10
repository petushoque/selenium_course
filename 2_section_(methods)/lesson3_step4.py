from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/alert_accept.html"

try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти и нажать на основную кнопку
    button = browser.find_element_by_css_selector("button")
    button.click()
    
finally:
    # Десятичекундная пауза
    time.sleep(10)
    # Закрыть браузер
    browser.quit()

# Пустая строка в конце
