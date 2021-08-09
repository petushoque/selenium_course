from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить поля
    input_first_name = browser.find_element_by_name("firstname")
    input_first_name.send_keys("Hello")
    input_last_name = browser.find_element_by_name("lastname")
    input_last_name.send_keys("World")
    input_email = browser.find_element_by_name("email")
    input_email.send_keys("email@email.ru")

    # Загрузить фаил
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')   
    input_file = browser.find_element_by_name(file_path)
    

    # Найти кнопку и отправить ответ
    button = browser.find_element_by_tag_name("button")
    button.click()
    
finally:
    # Десятичекундная пауза
    time.sleep(10)
    # Закрыть браузер
    browser.quit()

# Пустая строка в конце
